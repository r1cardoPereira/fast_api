from sqlalchemy import Column, Integer, String
from database import Base

class Curso(Base):
    """
    Define a classe Curso que herda de Base, que é uma classe de modelo do SQLAlchemy.

    Attributes:
        id (int): Campo ID, chave primária.
        titulo (str): Campo título, string de até 100 caracteres, não pode ser nulo.
        descricao (str): Campo descrição, string de até 225 caracteres, não pode ser nulo.
        carga_horaria (int): Campo carga horária, inteiro, não pode ser nulo.
        qtd_exercicios (int): Campo quantidade de exercícios, inteiro, não pode ser nulo.
    """
    __tablename__ = "cursos"

    id: int = Column(Integer, primary_key=True, index=True)  # Campo ID, chave primária.
    titulo: str = Column(String(100), nullable=False)  # Campo título, string de até 100 caracteres, não pode ser nulo.
    descricao: str = Column(String(225), nullable=False)  # Campo descrição, string de até 225 caracteres, não pode ser nulo.
    carga_horaria: int = Column(Integer, nullable=False)  # Campo carga horária, inteiro, não pode ser nulo.
    qtd_exercicios: int = Column(Integer, nullable=False)  # Campo quantidade de exercícios, inteiro, não pode ser nulo.
