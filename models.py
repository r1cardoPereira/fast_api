from sqlalchemy import Column, Integer, String
from database import Base

# Define a classe Curso que herda de Base, que é uma classe de modelo do SQLAlchemy.
class Curso(Base):

    # Define o nome da tabela no banco de dados associada a esta classe.
    __tablename__ = "cursos"

    # Define os campos (colunas) da tabela cursos.
    id: int = Column(Integer, primary_key=True, index=True)  # Campo ID, chave primária.
    titulo: str = Column(String(100), nullable=False)  # Campo título, string de até 100 caracteres, não pode ser nulo.
    descricao: str = Column(String(225), nullable=False)  # Campo descrição, string de até 225 caracteres, não pode ser nulo.
    carga_horaria: int = Column(Integer, nullable=False)  # Campo carga horária, inteiro, não pode ser nulo.
    qtd_exercicios: int = Column(Integer, nullable=False)  # Campo quantidade de exercícios, inteiro, não pode ser nulo.

