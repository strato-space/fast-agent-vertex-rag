# fast-agent-vertex-rag

AgentCard example that wraps Google Vertex RAG as a function tool for fast-agent.

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
uv run fast-agent go --card vertex-rag.md --message "Summarize customer pain points. Drive ID: <YOUR_DRIVE_ID>"
```

## Notes

- Vertex RAG quickstart: <https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-quickstart>
- Vertex RAG overview: <https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview>
- Vertex RAG console: <https://console.cloud.google.com/vertex-ai/rag>
