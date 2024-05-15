from sqlalchemy.ext.declarative import declarative_base


class Settings:
    BASE = declarative_base()

settings: Settings = Settings()
