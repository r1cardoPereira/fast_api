# Importando os componentes necessários do FastAPI
from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
# Importando a classe de modelo Curso do SQLAlchemy
from models import Curso

# Importando a engine, a base de modelos e a função para obter a sessão do banco de dados
from database import engine, Base, get_db

# Importando o repositório CursoRepository para operações no banco de dados
from repositories import CursoRepository

# Importando os esquemas para validação e serialização de dados
from schemas import CursoRequest, CursoResponse

# Importando o tipo List para indicar listas
from typing import List

# Criando as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inicializando a aplicação FastAPI
app = FastAPI()

# Rota para criar um novo curso
@app.post("/cursos", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
def create_curso(curso_request: CursoRequest, db: Session = Depends(get_db)):
    # Salvando o curso no banco de dados e recebendo a instância atualizada
    curso = CursoRepository.save(db, Curso(**curso_request.dict()))
    # Retornando o curso como CursoResponse
    return CursoResponse.from_orm(curso)

# Rota para listar todos os cursos
@app.get("/cursos", response_model=List[CursoResponse])
def find_all(db: Session = Depends(get_db)):
    # Encontrando todos os cursos no banco de dados
    cursos = CursoRepository.find_all(db)
    # Convertendo os cursos para o formato CursoResponse
    return [CursoResponse.from_orm(curso) for curso in cursos]

# Rota para encontrar um curso pelo ID
@app.get("/cursos/{id}", response_model=CursoResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    # Encontrando o curso pelo ID
    curso = CursoRepository.find_by_id(db, id)
    # Verificando se o curso foi encontrado
    if not curso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    # Retornando o curso como CursoResponse
    return CursoResponse.from_orm(curso)

# Rota para excluir um curso pelo ID
@app.delete("/cursos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    # Verificando se o curso com o ID especificado existe
    if not CursoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    # Excluindo o curso do banco de dados
    CursoRepository.delete_by_id(db, id)
    # Retornando uma resposta de sucesso sem conteúdo
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Rota para atualizar um curso pelo ID
@app.put("/cursos/{id}", response_model=CursoResponse)
def update(id: int, curso_request: CursoRequest, db: Session = Depends(get_db)):
    # Verificando se o curso com o ID especificado existe
    if not CursoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    # Obtendo os dados do curso_request
    curso_data = curso_request.dict()
    # Adicionando o ID ao dicionário
    curso_data['id'] = id
    # Salvando o curso atualizado no banco de dados e recebendo a instância atualizada
    curso = CursoRepository.save(db, Curso(**curso_data))
    # Retornando o curso como CursoResponse
    return CursoResponse.from_orm(curso)
