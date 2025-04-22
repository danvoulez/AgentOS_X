# promptos_backend/app/main.py
from fastapi import FastAPI
from app.api.v1.api import router as api_router
from loguru import logger
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

load_dotenv()

app = FastAPI(title="PromptOS Backend")

# Include API router
app.include_router(api_router, prefix="/api/v1")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up PromptOS Backend service")
    # Add startup logic here

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down PromptOS Backend service")
    # Add shutdown logic here
