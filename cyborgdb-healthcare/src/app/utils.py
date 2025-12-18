import numpy as np
from sentence_transformers import SentenceTransformer
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os, base64, hashlib

model = SentenceTransformer('all-MiniLM-L6-v2')

def chunk_text(text, chunk_size=512):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def embed_text(text):
    emb = model.encode(text).tolist()
    return emb

# Simplified encryption helpers: in production use KMS + proper key management
def _get_key_for_tenant(tenant_id: str):
    # derive a key from tenant id for demo ONLY
    h = hashlib.sha256((tenant_id + os.environ.get('KMS_KEY_ID','demo')).encode()).digest()
    return h[:32]

def encrypt_vector(vector, tenant_id: str):
    key = _get_key_for_tenant(tenant_id)
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    raw = (','.join(map(str, vector))).encode()
    ct = aesgcm.encrypt(nonce, raw, None)
    return {'nonce': base64.b64encode(nonce).decode(), 'ct': base64.b64encode(ct).decode()}

def decrypt_result(match, tenant_id: str):
    # demo decrypt - in real use, avoid returning raw sensitive text
    import base64
    key = _get_key_for_tenant(tenant_id)
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    aesgcm = AESGCM(key)
    nonce = base64.b64decode(match['embedding']['nonce'])
    ct = base64.b64decode(match['embedding']['ct'])
    raw = aesgcm.decrypt(nonce, ct, None)
    text = raw.decode()
    return {'id': match.get('id'), 'text': text, 'score': match.get('score')}
