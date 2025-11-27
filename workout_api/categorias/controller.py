from fastapi import APIRouter, Body, status, HTTPException
from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from workout_api.contrib.dependencias import Databasedependency
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.categorias.models import CategoriaModel

router = APIRouter()


@router.post(
    "/",
    summary="Criar uma nova categoria",
    description="Cria uma nova categoria no sistema.",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def post(
    categoria_in: CategoriaIn = Body(...),
    db_session: Databasedependency = None,  # type: ignore
) -> CategoriaOut:

    session: AsyncSession = db_session

    # Criar instância ORM
    categoria = CategoriaModel(
        nome=categoria_in.nome
    )

    session.add(categoria)
    await session.commit()
    await session.refresh(categoria)

    # ORM → Schema (Pydantic v2)
    return CategoriaOut.model_validate(categoria)


@router.get(
    "/",
    summary="Consultar todos as categorias",
    description="Consulta todas as categorias no sistema.",
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut],
)
async def query(db_session: Databasedependency) -> list[CategoriaOut]:
    session: AsyncSession = db_session

    result = await session.execute(select(CategoriaModel))
    categorias = result.scalars().all()

    return [CategoriaOut.model_validate(c) for c in categorias]



@router.get(
    "/{id}",
    summary="Consultar uma categoria",
    description="Consulta uma categoria no sistema.",
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
)
async def query(id: UUID4, db_session: Databasedependency) -> CategoriaOut:
    categorias: CategoriaOut = (
        await db_session.execute(select(CategoriaModel).where(CategoriaModel.id == id))
        ).scalars().first()
    
    if not categorias:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Categoria não encontrada{id}")
    return CategoriaOut.model_validate(categorias)  