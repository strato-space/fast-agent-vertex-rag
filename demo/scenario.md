gh repo clone strato-space/fast-agent-vertex-rag

cd fast-agent-vertex-rag

cp fastagent.secrets.yaml.example fastagent.secrets.yaml

uv run fast-agent go --card agents --watch

Find challenges. Google Drive: 1J3ubtdkmFuWDjfW3_qT2Fhsdn2pbtv-8. Search 50 items, summarize them to 5 short. Add References section.

=== Edit: ===

model: gemini25
---
say: hi, repl! 
and stop execution.

=== New Terminal ===

cd fast-agent-vertex-rag

cat > agents/sizer.md

---
type: agent
name: sizer
---
Given an object, respond only with an estimate of its size.

a mouse
the moon

/exit
