from dataclasses import dataclass
from os import getenv


@dataclass
class DatabaseConfig:
    db_uri: str

    @staticmethod
    def from_env() -> "DatabaseConfig":
        uri = getenv(
            "DB_URI",
            "postgresql+psycopg://postgres:postgres@localhost:5432/caFastapi",
        )
        return DatabaseConfig(db_uri=uri)
