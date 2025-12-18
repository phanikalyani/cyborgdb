import os, requests, json
CYBORG_URL = os.environ.get('CYBORGDB_ENDPOINT', 'http://localhost:8080')
API_KEY = os.environ.get('CYBORGDB_API_KEY', '')

class CyborgClient:
    def __init__(self, endpoint: str = CYBORG_URL, api_key: str = API_KEY):
        self.endpoint = endpoint
        self.api_key = api_key

    def upsert_vectors(self, tenant_id, docs):
        url = f"{self.endpoint}/v1/upsert"
        payload = {'tenant_id': tenant_id, 'docs': docs}
        headers = {'Authorization': f"Bearer {self.api_key}"}
        r = requests.post(url, json=payload, headers=headers, timeout=30)
        try:
            r.raise_for_status()
        except Exception as e:
            return {'error': str(e), 'status_code': r.status_code, 'text': r.text}
        return r.json()

    def search_encrypted(self, tenant_id, q_emb, top_k=5):
        url = f"{self.endpoint}/v1/search"
        payload = {'tenant_id': tenant_id, 'query_embedding': q_emb, 'top_k': top_k}
        headers = {'Authorization': f"Bearer {self.api_key}"}
        r = requests.post(url, json=payload, headers=headers, timeout=30)
        try:
            r.raise_for_status()
        except Exception as e:
            return {'error': str(e), 'status_code': r.status_code, 'text': r.text}
        return r.json()
