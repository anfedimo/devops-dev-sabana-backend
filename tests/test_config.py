import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    @property
    def PROJECT_NAME(self):
        return "sabana API"

    @property
    def VERSION(self):
        return "1.0.0"

    @property
    def API_PREFIX(self):
        return ""

    @property
    def DEBUG(self):
        return os.getenv("DEBUG", "False").lower() == "true"

    @property
    def ENVIRONMENT(self):
        return os.getenv("ENVIRONMENT", "development")

    @property
    def PORT(self):
        return int(os.getenv("PORT", 9000))

    @property
    def ALLOWED_ORIGINS(self):
        return os.getenv("ALLOWED_ORIGINS", "*").split(",")

    @property
    def SECRET_KEY(self):
        return os.getenv("SECRET_KEY", "mysecretkey")

settings = Settings()
