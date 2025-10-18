import os
from dotenv import load_dotenv

# Carga variables desde un archivo .env si existe
load_dotenv()

class Settings:
    PROJECT_NAME: str = "sabana API"
    VERSION: str = "1.0.0"
    API_PREFIX: str = ""
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    PORT: int = int(os.getenv("PORT", 9000))

    # Seguridad / CORS / Keys
    ALLOWED_ORIGINS: list[str] = os.getenv("ALLOWED_ORIGINS", "*").split(",")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "mysecretkey")

settings = Settings()
