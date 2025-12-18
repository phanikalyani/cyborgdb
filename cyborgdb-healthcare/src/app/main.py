from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from app import ingest, retrieval, audit
import uvicorn

app = FastAPI(title='CyborgDB Healthcare Secure Demo')

@app.post('/ingest')
async def ingest_file(tenant_id: str, file: UploadFile = File(...)):
    contents = await file.read()
    try:
        result = ingest.process_and_upsert(tenant_id, file.filename, contents)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/search')
async def search(tenant_id: str, q: str):
    return retrieval.search_and_answer(tenant_id, q)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
