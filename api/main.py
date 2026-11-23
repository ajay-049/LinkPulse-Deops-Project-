import os
import string
import random
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI(title="LinkPulse API")

# Temporary in-memory store (replaced by Redis + MySQL in Phase 2)
url_db = {}

class URLRequest(BaseModel):
    url: str

@app.get("/health")
def health_check():
    return {"status": "healthy", "hostname": os.uname().nodename}

@app.post("/shorten")
def shorten_url(req: URLRequest):
    code = "".join(random.choices(string.ascii_letters + string.digits, k=6))
    url_db[code] = req.url
    return {"short_code": code, "original_url": req.url}

@app.get("/{code}")
def redirect_url(code: str):
    if code not in url_db:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(url=url_db[code])
