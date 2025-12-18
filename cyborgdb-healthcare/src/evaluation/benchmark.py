import time, random, asyncio
from src.cyborg_integration.cyborg_client import CyborgClient
from src.app.utils import embed_text

client = CyborgClient()

async def single_query(q):
    q_emb = embed_text(q)
    start = time.perf_counter()
    resp = client.search_encrypted('demo_tenant', q_emb, top_k=5)
    end = time.perf_counter()
    return (end-start)*1000, resp

async def run_batch(queries, concurrency=50):
    sem = asyncio.Semaphore(concurrency)
    lat = []
    async def worker(q):
        async with sem:
            l, _ = await single_query(q)
            lat.append(l)
    await asyncio.gather(*(worker(q) for q in queries))
    lat.sort()
    return {'count': len(lat), 'p50': lat[int(0.5*len(lat))], 'p95': lat[int(0.95*len(lat))]}

if __name__ == '__main__':
    queries = ['find patient with diagnosis diabetes']*100
    res = asyncio.run(run_batch(queries, concurrency=20))
    print(res)
