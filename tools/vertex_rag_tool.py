import google.auth
import vertexai
from googleapiclient.discovery import build
from vertexai import rag

from fast_agent.config import get_settings

# RAG quickstart: Required roles, Prepare your Google Cloud console, Run Vertex AI RAG Engine
# https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-quickstart
#
# Vertex AI RAG Engine overview: Overview, Supported regions, ...
# https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview
#
# Install the Vertex AI SDK for Python
# https://docs.cloud.google.com/vertex-ai/docs/start/install-sdk
#
# Admin console
# https://console.cloud.google.com/vertex-ai/rag

CONFIG_PATH = "fastagent.secrets.yaml"
EMBEDDING_MODEL = "text-embedding-005"
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

_vertex_initialized = False


def _load_vertex_settings() -> tuple[str, str]:
    settings = get_settings(CONFIG_PATH)
    vertex_cfg = getattr(settings.google, "vertex_ai", {}) if settings.google else {}
    project_id = vertex_cfg.get("project_id")
    location = vertex_cfg.get("location")
    if not project_id or not location:
        raise ValueError(
            "Missing google.vertex_ai.project_id/location in fastagent.secrets.yaml"
        )
    return project_id, location


def _ensure_vertexai_init(project_id: str, location: str) -> None:
    global _vertex_initialized
    if not _vertex_initialized:
        vertexai.init(project=project_id, location=location)
        _vertex_initialized = True


def _drive_folder_name(folder_id: str) -> str:
    credentials, _ = google.auth.default(scopes=SCOPES)
    drive_service = build("drive", "v3", credentials=credentials)
    payload = (
        drive_service.files()
        .get(
            fileId=folder_id,
            fields="id,name,mimeType",
            supportsAllDrives=True,
        )
        .execute()
    )
    return payload["name"]


def _create_and_import_corpus(display_name: str, paths: list[str]) -> rag.RagCorpus:
    embedding_model_config = rag.RagEmbeddingModelConfig(
        vertex_prediction_endpoint=rag.VertexPredictionEndpoint(
            publisher_model=f"publishers/google/models/{EMBEDDING_MODEL}"
        )
    )
    rag_corpus = rag.create_corpus(
        display_name=display_name,
        backend_config=rag.RagVectorDbConfig(
            rag_embedding_model_config=embedding_model_config
        ),
    )
    rag.import_files(
        rag_corpus.name,
        paths,
        transformation_config=rag.TransformationConfig(
            chunking_config=rag.ChunkingConfig(
                chunk_size=512,
                chunk_overlap=100,
            ),
        ),
        max_embedding_requests_per_min=1000,
    )
    return rag_corpus


def mini_rag(query: str, drive_id: str, top_k: int = 5) -> object:
    """Query Vertex RAG using a Google Drive folder ID."""
    project_id, location = _load_vertex_settings()
    _ensure_vertexai_init(project_id, location)
    if not drive_id:
        raise ValueError("drive_id must be a non-empty Google Drive ID.")

    paths = [f"https://drive.google.com/drive/folders/{drive_id}"]
    folder_name = _drive_folder_name(drive_id)
    key = drive_id
    display_name = f"{folder_name} | {key}"

    existing_corpus = None
    for corpus in rag.list_corpora():
        if corpus.display_name and key in corpus.display_name:
            existing_corpus = corpus
            break

    if existing_corpus:
        rag_corpus = existing_corpus
    else:
        rag_corpus = _create_and_import_corpus(display_name, paths)

    rag_retrieval_config = rag.RagRetrievalConfig(
        top_k=top_k,
        filter=rag.Filter(vector_distance_threshold=0.5),
    )
    return rag.retrieval_query(
        rag_resources=[
            rag.RagResource(
                rag_corpus=rag_corpus.name,
            )
        ],
        text=query,
        rag_retrieval_config=rag_retrieval_config,
    )
