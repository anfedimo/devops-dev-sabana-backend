from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from enum import Enum
from pydantic import BaseModel, Field
import logging
from app.config import settings
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG
)

Instrumentator().instrument(app).expose(app)   # pragma: no cover

# Sirve archivos estáticos (imágenes) desde el directorio /static
STATIC_DIR = str((Path(__file__).parent / "static").resolve())
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Configura Jinja2 para templates
TEMPLATES_DIR = str((Path(__file__).parent.parent / "templates").resolve())
templates = Jinja2Templates(directory=TEMPLATES_DIR)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sabana")

class DifficultyLevel(str, Enum):
    BASICO = "básico"
    INTERMEDIO = "intermedio"
    AVANZADO = "avanzado"

class Challenge(BaseModel):
    title: str = Field(..., example="Ahorrar 10% de tu ingreso mensual")
    description: str
    difficulty: DifficultyLevel

challenges = []

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/challenges")
def list_challenges():
    return challenges

@app.post("/challenges", status_code=201)
def create_challenge(challenge: Challenge):
    challenges.append(challenge)
    logger.info(f"Nuevo reto: {challenge.title}")
    return challenge

if __name__ == "__main__":  # pragma: no cover
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9000)