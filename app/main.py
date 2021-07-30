from fastapi import FastAPI
import uvicorn

from routers import (
    searchengine
)

app = FastAPI(
    title = 'SoloAutónomos Legal Chat'
)

app.include_router(searchengine.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host = "0.0.0.0", 
        port = 5000, 
        log_level = "debug"
    )