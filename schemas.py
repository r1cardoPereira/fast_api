from pydantic import BaseModel
from models import Curso

class CursoBase(BaseModel):
    """
    Define a classe base para representar um curso.

    Attributes:
        titulo (str): O título do curso.
        descricao (str): A descrição do curso.
        carga_horaria (int): A carga horária do curso em horas.
        qtd_exercicios (int): A quantidade de exercícios no curso.
    """
    titulo: str
    descricao: str
    carga_horaria: int
    qtd_exercicios: int

class CursoRequest(CursoBase):
    """
    Define a classe para representar a requisição de criação de um curso.

    Inherits:
        CursoBase
    """
    pass

class CursoResponse(CursoBase):
    """
    Define a classe para representar a resposta de um curso.

    Inherits:
        CursoBase

    Attributes:
        id (int): O ID do curso.
    """
    id: int

    @classmethod
    def from_orm(cls, curso_orm: Curso):
        """
        Cria uma instância de CursoResponse a partir de um objeto Curso do banco de dados.

        Args:
            curso_orm (Curso): O objeto Curso do banco de dados.

        Returns:
            CursoResponse: A instância de CursoResponse criada.
        """
        return cls(
            id=curso_orm.id,
            titulo=curso_orm.titulo,
            descricao=curso_orm.descricao,
            carga_horaria=curso_orm.carga_horaria,
            qtd_exercicios=curso_orm.qtd_exercicios
        )

    class Config:
        orm_mode = True
