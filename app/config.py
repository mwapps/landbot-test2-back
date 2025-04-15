
import os


class Config:
    def __init__(self):
        self.settings = {
            "ENV": os.getenv("ENV", "development"),
            "DEBUG": os.getenv("DEBUG", "True") == "True",
            "DATABASE_URL": os.getenv("DATABASE_URL", "sqlite:///campaigns.db"),
            "LOGGING_LEVEL": os.getenv("LOGGING_LEVEL", "INFO")
        }

    def get(self, key, default=None):
        return self.settings.get(key, default)
