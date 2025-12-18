# CyborgDB Secure Healthcare Demo

This repository demonstrates a HIPAA-oriented secure RAG/search application
using CyborgDB's encrypted vector search. It emphasizes client-side encryption,
per-tenant (per-hospital) keys via KMS, immutable audit logs, and secure deployment patterns.

## Contents
- `src/`: application source (FastAPI backend, ingestion, cyborg client wrapper)
- `docs/`: architecture, compliance notes, benchmarks
- `scripts/`: helper scripts to run locally and on k8s
- `Dockerfile`, `k8s/` manifests
- `requirements.txt`

## Quickstart (local)
1. Copy `config/env.sample` to `.env` and fill credentials.
2. Start CyborgDB locally per vendor templates.
3. Build and run the app:
   ```bash
   docker build -t cyborgdb-healthcare:local .
   docker run --env-file .env -p 8000:8000 cyborgdb-healthcare:local
   ```
4. Open API docs: http://localhost:8000/docs

## Notes
- This demo includes synthetic data generators for testing.
- It is intended for evaluation and demonstration purposes only.
