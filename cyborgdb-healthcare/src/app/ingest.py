import hashlib, uuid, json
from .cyborg_client import CyborgClient
from .utils import chunk_text, embed_text, encrypt_vector, upload_audit_event

client = CyborgClient()

def process_and_upsert(tenant_id: str, filename: str, file_bytes: bytes):
    # simplistic text extraction placeholder
    text = file_bytes.decode('utf-8', errors='ignore')[:10000]
    chunks = chunk_text(text, chunk_size=512)
    docs = []
    for c in chunks:
        emb = embed_text(c)
        enc = encrypt_vector(emb, tenant_id)
        doc_id = str(uuid.uuid4())
        docs.append({'id': doc_id, 'text': c, 'embedding': enc, 'metadata': {'filename': filename}})
    resp = client.upsert_vectors(tenant_id, docs)
    upload_audit_event(tenant_id, 'ingest', len(docs))
    return {'status':'ok', 'upserted': len(docs), 'response': resp}
