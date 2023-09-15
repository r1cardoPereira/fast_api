from sqlalchemy.orm import Session
from models import Curso
from typing import List

# Definindo uma classe chamada CursoRepository que será responsável por lidar com operações de banco de dados relacionadas a entidade Curso.
class CursoRepository:

    # Método estático para encontrar todos os cursos no banco de dados.
    @staticmethod
    def find_all(db: Session) -> List[Curso]:
        return db.query(Curso).all()

    # Método estático para salvar um curso no banco de dados.
    @staticmethod
    def save(db: Session, curso: Curso) -> Curso:
        # Verifica se o curso já possui um ID (ou seja, se já está no banco de dados).
        if curso.id:
            # Se o curso já possui um ID, mescla (merge) com o objeto no banco de dados.
            db.merge(curso)
        else:
            # Se o curso não possui um ID, adiciona ao banco de dados.
            db.add(curso)
        # Comita a transação no banco de dados.
        db.commit()
        # Retorna o curso (pode ser útil para obter o ID após a inserção, por exemplo).
        return curso

    # Método estático para encontrar um curso pelo seu ID.
    @staticmethod
    def find_by_id(db: Session, curso_id: int) -> Curso:
        return db.query(Curso).filter(Curso.id == curso_id).first()

    # Método estático para verificar se um curso com um determinado ID existe no banco de dados.
    @staticmethod
    def exists_by_id(db: Session, curso_id: int) -> bool:
        return db.query(Curso.id).filter(Curso.id == curso_id).scalar() is not None

    # Método estático para excluir um curso pelo seu ID.
    @staticmethod
    def delete_by_id(db: Session, curso_id: int) -> None:
        curso = db.query(Curso).filter(Curso.id == curso_id).first()
        if curso is not None:
            # Se o curso existe, exclui do banco de dados.
            db.delete(curso)
            # Comita a transação no banco de dados.
            db.commit()
