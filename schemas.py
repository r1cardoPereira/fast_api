from pydantic import BaseModel
from models import Curso

# Definindo uma classe chamada CursoBase que herda de BaseModel.
class CursoBase(BaseModel):
    titulo: str          # Um campo para o título do curso (str).
    descricao: str       # Um campo para a descrição do curso (str).
    carga_horaria: int   # Um campo para a carga horária do curso (int).
    qtd_exercicios: int  # Um campo para a quantidade de exercícios do curso (int).

# Definindo uma classe chamada CursoRequest que herda de CursoBase.
class CursoRequest(CursoBase):
    pass  # Aqui você pode adicionar campos adicionais específicos para requisições de criação ou atualização de cursos.

# Definindo uma classe chamada CursoResponse que herda de CursoBase.
class CursoResponse(CursoBase):
    id: int  # Adicionando um campo ID para a resposta.

    # Método de classe para criar uma instância de CursoResponse a partir de um objeto Curso (ORM).
    @classmethod
    def from_orm(cls, curso_orm: Curso):
        return cls(
            id=curso_orm.id,
            titulo=curso_orm.titulo,
            descricao=curso_orm.descricao,
            carga_horaria=curso_orm.carga_horaria,
            qtd_exercicios=curso_orm.qtd_exercicios
        )

    # Configuração para indicar que este modelo (CursoResponse) é para uso com ORM (Object Relational Mapping).
    class Config:
        orm_mode = True
