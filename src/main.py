from fastapi import FastAPI
from src import routers as app_router
from src.cron_handler import router as cron_router

app = FastAPI()

app.include_router(app_router.router)
app.include_router(cron_router, prefix="/api")

@app.get("/", tags=["Home"])
async def root():
    return {"message": "FastAPI server running fine 🚀"}
