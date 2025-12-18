from .cyborg_client import CyborgClient
from .utils import embed_text, decrypt_result, upload_audit_event

client = CyborgClient()

def search_and_answer(tenant_id: str, query: str, top_k: int = 5):
    q_emb = embed_text(query)
    # encrypt query vector
    resp = client.search_encrypted(tenant_id, q_emb, top_k=top_k)
    # decrypt results (identifiers/text may be encrypted)
    results = [decrypt_result(r, tenant_id) for r in resp.get('matches', [])]
    upload_audit_event(tenant_id, 'query', {'q_hash': hash(query), 'returned': len(results)})
    # For demo: return matches directly
    return {'matches': results}
