# fast-agent-vertex-rag

Minimal AgentCard repo that wraps Google Vertex RAG as a function tool for fast-agent.

This repo follows the AgentCard RFC:
<https://github.com/evalstate/fast-agent/blob/main/plan/agent-card-rfc.md>

## Design (why this is minimal)

- `vertex-rag.md` is the AgentCard.
- `function_tools` loads `vertex_rag_tool.py:mini_rag` via the function tool loader.
- `pyproject.toml` declares all runtime dependencies, e.g. the fast-agent.ai runtime.
- `fastagent.secrets.yaml` supplies Vertex AI project/region for the tool.

## Setup

1. Install dependencies:

```bash
uv sync
```

2. Configure Vertex AI settings:

```bash
cp fastagent.secrets.yaml.example fastagent.secrets.yaml
```

Update `fastagent.secrets.yaml` with your Google Cloud project and region. Authenticate with Google (for example, `gcloud auth application-default login`) and ensure the Drive folder is accessible by your credentials.

## Run

```bash
uv run fast-agent go --card vertex-rag.md --message "Produce a short top 5 prioritized list about customer pain points. From RAG, select 50 relevant chunks about customer pain points. Deduplicate. Links: [name](<link>). Compact output. Drive ID: 1J3ubtdkmFuWDjfW3_qT2Fhsdn2pbtv-8."
```

## Notes

- Vertex RAG quickstart: <https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-quickstart>
- Vertex RAG overview: <https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview>
- Vertex RAG console: <https://console.cloud.google.com/vertex-ai/rag>
