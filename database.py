# Importando o método de criação de engine do SQLAlchemy
from sqlalchemy import create_engine

# Importando a classe base declarativa do SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

# Importando o gerenciador de sessões do SQLAlchemy
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///db.sqlite3"

# Criando uma engine de banco de dados
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Criando uma instância da base declarativa
Base = declarative_base()

# Criando uma classe para obter uma sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Definindo uma função geradora que fornece uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
