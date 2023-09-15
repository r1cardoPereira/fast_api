from sqlalchemy.orm import Session
from models import Curso
from typing import List


class CursoRepository:
    """
    Classe responsável por gerenciar operações relacionadas ao modelo Curso no banco de dados.

    Methods:
        find_all(db: Session) -> List[Curso]: Retorna todos os cursos do banco de dados.
        save(db: Session, curso: Curso) -> Curso: Salva um curso no banco de dados.
        find_by_id(db: Session, curso_id: int) -> Curso: Retorna um curso pelo seu ID.
        exists_by_id(db: Session, curso_id: int) -> bool: Verifica se um curso existe pelo seu ID.
        delete_by_id(db: Session, curso_id: int) -> None: Deleta um curso pelo seu ID.

    Attributes:
        None
    """

    @staticmethod
    def find_all(db: Session) -> List[Curso]:
        """
        Retorna todos os cursos do banco de dados.

        Args:
            db (Session): Sessão do banco de dados.

        Returns:
            List[Curso]: Lista de cursos.
        """
        return db.query(Curso).all()

    @staticmethod
    def save(db: Session, curso: Curso) -> Curso:
        """
        Salva um curso no banco de dados.

        Args:
            db (Session): Sessão do banco de dados.
            curso (Curso): Objeto do tipo Curso.

        Returns:
            Curso: O curso salvo no banco de dados.
        """
        if curso.id:
            db.merge(curso)
        else:
            db.add(curso)
        db.commit()
        return curso

    @staticmethod
    def find_by_id(db: Session, curso_id: int) -> Curso:
        """
        Retorna um curso pelo seu ID.

        Args:
            db (Session): Sessão do banco de dados.
            curso_id (int): ID do curso.

        Returns:
            Curso: O curso correspondente ao ID.
        """
        return db.query(Curso).filter(Curso.id == curso_id).first()

    @staticmethod
    def exists_by_id(db: Session, curso_id: int) -> bool:
        """
        Verifica se um curso existe pelo seu ID.

        Args:
            db (Session): Sessão do banco de dados.
            curso_id (int): ID do curso.

        Returns:
            bool: True se o curso existe, False caso contrário.
        """
        return db.query(Curso.id).filter(Curso.id == curso_id).scalar() is not None

    @staticmethod
    def delete_by_id(db: Session, curso_id: int) -> None:
        """
        Deleta um curso pelo seu ID.

        Args:
            db (Session): Sessão do banco de dados.
            curso_id (int): ID do curso.

        Returns:
            None
        """
        curso = db.query(Curso).filter(Curso.id == curso_id).first()
        if curso is not None:
            db.delete(curso)
            db.commit()
