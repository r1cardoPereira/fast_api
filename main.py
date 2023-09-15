from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import Curso
from database import engine, Base, get_db
from repositories import CursoRepository
from schemas import CursoRequest, CursoResponse
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/cursos", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
def create_curso(curso_request: CursoRequest, db: Session = Depends(get_db)):
    """
    Cria um novo curso.

    Args:
        curso_request (CursoRequest): As informações do curso a ser criado.
        db (Session, opcional): A sessão do banco de dados. Defaults to Depends(get_db).

    Returns:
        CursoResponse: O curso criado.
    """
    curso = CursoRepository.save(db, Curso(**curso_request.dict()))
    return CursoResponse.from_orm(curso)


@app.get("/cursos", response_model=List[CursoResponse])
def find_all(db: Session = Depends(get_db)):
    """
    Retorna todos os cursos.

    Args:
        db (Session, opcional): A sessão do banco de dados. Defaults to Depends(get_db).

    Returns:
        List[CursoResponse]: Uma lista de cursos.
    """
    cursos = CursoRepository.find_all(db)
    return [CursoResponse.from_orm(curso) for curso in cursos]


@app.get("/cursos/{id}", response_model=CursoResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    """
    Retorna um curso pelo seu ID.

    Args:
        id (int): O ID do curso.
        db (Session, opcional): A sessão do banco de dados. Defaults to Depends(get_db).

    Raises:
        HTTPException: Retorna 404 se o curso não for encontrado.

    Returns:
        CursoResponse: O curso encontrado.
    """
    curso = CursoRepository.find_by_id(db, id)
    if not curso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    return CursoResponse.from_orm(curso)


@app.delete("/cursos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    """
    Deleta um curso pelo seu ID.

    Args:
        id (int): O ID do curso.
        db (Session, opcional): A sessão do banco de dados. Defaults to Depends(get_db).

    Raises:
        HTTPException: Retorna 404 se o curso não for encontrado.

    Returns:
        Response: Retorna uma resposta vazia.
    """
    if not CursoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    CursoRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/cursos/{id}", response_model=CursoResponse)
def update(id: int, curso_request: CursoRequest, db: Session = Depends(get_db)):
    """
    Atualiza um curso pelo seu ID.

    Args:
        id (int): O ID do curso.
        curso_request (CursoRequest): As novas informações do curso.
        db (Session, opcional): A sessão do banco de dados. Defaults to Depends(get_db).

    Raises:
        HTTPException: Retorna 404 se o curso não for encontrado.

    Returns:
        CursoResponse: O curso atualizado.
    """
    if not CursoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    curso_data = curso_request.dict()
    curso_data['id'] = id
    curso = CursoRepository.save(db, Curso(**curso_data))
    return CursoResponse.from_orm(curso)
