import json
import aiofiles
from fastapi import FastAPI

app = FastAPI()

@app.get("/logs")

async def get_logs():
    """Fetches and returns the processed log data."""
    try:
        async with aiofiles.open("processed_logs.json", mode='r') as f:
            contents = await f.read()
            return json.loads(contents)
    except FileNotFoundError:
        return {"error": "Log data not found. Please run log processing first."}

