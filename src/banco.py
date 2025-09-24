import sqlite3
from pathlib import Path

# Caminho do arquivo do banco de dados
DB_PATH = Path(__file__).with_name("alunos.db")

# Caminho do arquivo schema.sql
SCHEMA_FILE = Path(__file__).with_name("schema.sql")


def get_connection():
    """Abre uma conexão com o banco de dados SQLite."""
    conn = sqlite3.connect(DB_PATH)
    return conn


def init_db():
    """Inicializa o banco de dados executando o schema.sql."""
    with get_connection() as conn:
        with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
