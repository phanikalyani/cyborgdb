# Architecture (Healthcare)

Components:
- FastAPI backend (ingest, retrieval, audit)
- CyborgDB encrypted vector proxy (deployed in VPC/on-prem)
- Customer KMS (AWS KMS / GCP KMS / Vault) for per-tenant CMKs
- LLM (on-prem or enterprise provider)
- Audit log store (append-only, e.g., object storage with signed manifests)

Dataflow:
1. Ingest: PDF -> text extraction -> chunk -> local embedding -> client-side encryption -> upsert
2. Query: user query -> embedding -> encrypted query -> CyborgDB search -> decrypt identifiers -> RAG prompt -> LLM -> response
