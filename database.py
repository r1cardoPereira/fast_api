from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///db.sqlite3"

# Cria um mecanismo de banco de dados
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria uma base de dados declarativa
Base = declarative_base()

# Cria uma fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Retorna uma instância do banco de dados.

    Yields:
        Session: Uma sessão do banco de dados.

    Finally:
        Fecha a sessão após o uso.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
