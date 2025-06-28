import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.example_bg_task import write_random_log, background_task_running
from src import routers as app_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting background log task...")
    asyncio.create_task(write_random_log())
    yield

    # Shutdown
    global background_task_running
    background_task_running = False
    print("Background log task stopped.")


app = FastAPI(lifespan=lifespan)

app.include_router(app_router.router)


@app.get("/", tags=["Home"])
async def root():
    return {"message": "FastAPI server running fine 🚀"}
