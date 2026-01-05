# fast-agent-vertex-rag

Minimal AgentCard repo that wraps Google Vertex RAG as a function tool for fast-agent.

This repo follows the AgentCard RFC:
<https://github.com/evalstate/fast-agent/blob/main/plan/agent-card-rfc.md>

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
Enable Vertex AI RAG + Google Drive APIs and required roles in your project. If access is denied, share the Drive folder with the Google service account from the error message.

## Run

### Batch

```bash
uv run fast-agent go --card agents --message "Produce a short top 5 prioritized list about customer pain points. From RAG, select 50 relevant chunks about customer pain points. Deduplicate. Links: [name](<link>). Compact output. Drive ID: 1J3ubtdkmFuWDjfW3_qT2Fhsdn2pbtv-8."
```

### Interactive (with Read-Eval-Print-Loop)

```bash
uv run fast-agent go --card agents --watch
```

### Video: AgentCard: fast-agent-vertex-rag sample

[![AgentCard: fast-agent-vertex-rag sample](https://img.youtube.com/vi/bP19txX3Mpk/hqdefault.jpg)](https://youtu.be/bP19txX3Mpk)

## Design (why this is minimal)

- `agents/vertex-rag.md` is the AgentCard.
- `function_tools` loads `agents/vertex_rag_tool.py:mini_rag` via the function tool loader.
- `pyproject.toml` declares all runtime dependencies, including `fast-agent-mcp`.
- `fastagent.secrets.yaml` supplies Vertex AI project/region for the tool.

## References

### AgentCard

- AgentCard at the Summit: The Multi-Agent Standardization Revolution: <https://github.com/evalstate/fast-agent/blob/main/plan/agentcard-standards-mini-article.md>
- AgentCard RFC: <https://github.com/evalstate/fast-agent/blob/main/plan/agent-card-rfc.md>

### fast-agent.ai

- fast-agent docs: <https://fast-agent.ai>
- fast-agent repo: <https://github.com/evalstate/fast-agent>

### Google Vertex RAG

- Vertex RAG quickstart: <https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-quickstart>
- Vertex RAG overview: <https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview>
- Vertex RAG supported regions: <https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview#supported-regions>
- Vertex AI SDK install: <https://docs.cloud.google.com/vertex-ai/docs/start/install-sdk>
- Vertex RAG console: <https://console.cloud.google.com/vertex-ai/rag>
