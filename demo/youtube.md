## Description
In this demo I show fast-agent AgentCards + hot reload in action with a Vertex RAG tool. We start the REPL from an AgentCard folder, run a Drive-backed RAG query, then add a brand-new AgentCard (`sizer`) while the session is running and switch to it immediately.

Commands used:
```bash
gh repo clone strato-space/fast-agent-vertex-rag
cd fast-agent-vertex-rag
cp fastagent.secrets.yaml.example fastagent.secrets.yaml
uv run fast-agent go --card agents --watch
```

Prompt:
```
Find challenges. Google Drive: 1J3ubtdkmFuWDjfW3_qT2Fhsdn2pbtv-8. Search 50 items, summarize them to 5 short. Add References section.
```

Edit (inside REPL):
```
model: gemini25
say: hi, repl!
```

New terminal - add a new AgentCard:
```bash
cat > agents/sizer.md
---
type: agent
name: sizer
---
Given an object, respond only with an estimate of its size.
```

Try it:
```
a mouse
the moon
/exit
```

## Tags
fast-agent, AgentCards, RAG, Vertex AI, Google Drive, MCP, ACP, LLM, REPL, hot reload, AI agents, agent tools, Gemini, python, developer tools, multi-agent, prompt engineering, open source

## Hashtags
#FastAgent #AgentCards #RAG #VertexAI #GoogleDrive #MCP #ACP #LLM #AI #OpenSource #REPL #HotReload
