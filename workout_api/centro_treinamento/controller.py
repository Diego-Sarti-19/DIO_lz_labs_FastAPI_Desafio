from datetime import datetime
from fastapi import APIRouter, Body, status, HTTPException
from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from workout_api.contrib.dependencias import Databasedependency
from workout_api.centro_treinamento.schemas import CentroTreinamentoIN, CentroTreinamentoOut
from workout_api.centro_treinamento.models import CentroTreinamentoModel

#router = APIRouter(prefix="/centro_treinamento", tags=["centro_treinamento"])
router = APIRouter()

@router.post(
    "/",
    summary="Criar um novo centro de treinamento",
    description="Cria um novo centro de treinamento no sistema.",
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def post(
    centro_treinamento_in: CentroTreinamentoIN = Body(...),
    db_session: Databasedependency = None,  # type: ignore
) -> CentroTreinamentoOut:

    session: AsyncSession = db_session

    centro_treinamento = CentroTreinamentoModel(
        nome=centro_treinamento_in.nome,
        endereco=centro_treinamento_in.endereco,
        proprietario=centro_treinamento_in.proprietario,
    )

    session.add(centro_treinamento)
    await session.commit()
    await session.refresh(centro_treinamento)

    return CentroTreinamentoOut.model_validate(centro_treinamento)

@router.get(
    "/",
    summary="Consultar todas as categorias",
    description="Consulta todas as categorias no sistema.",
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut],
)
async def query(db_session: Databasedependency) -> list[CentroTreinamentoOut]:
    session: AsyncSession = db_session

    result = await session.execute(select(CentroTreinamentoModel))
    centro_treinamentos = result.scalars().all()

    return [CentroTreinamentoOut.model_validate(c) for c in centro_treinamentos]



@router.get(
    "/{id}",
    summary="Consultar uma categoria",
    description="Consulta uma categoria no sistema.",
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut,
)
async def query(id: UUID4, db_session: Databasedependency) -> CentroTreinamentoOut:
    centro_treinamento: CentroTreinamentoOut = (
        await db_session.execute(select(CentroTreinamentoModel).where(CentroTreinamentoModel.id == id))
        ).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Centro de treinamento não encontrado{id}")
    return CentroTreinamentoOut.model_validate(centro_treinamento )  


################################################################################################################

# from fastapi import APIRouter, Body, status
# from sqlalchemy.ext.asyncio import AsyncSession

# from workout_api.contrib.dependencias import Databasedependency
# from workout_api.centro_treinamento.schemas import (
#     CentroTreinamentoIN,
#     CentroTreinamentoOut,
# )
# from workout_api.centro_treinamento.models import CentroTreinamentoModel

# router = APIRouter()


# @router.post(
#     "/",
#     summary="Criar um novo centro de treinamento",
#     description="Cria um novo centro de treinamento no sistema.",
#     status_code=status.HTTP_201_CREATED,
#     response_model=CentroTreinamentoOut,
# )
# async def post(
#     centro_treinamento_in: CentroTreinamentoIN = Body(...),
#     db_session: Databasedependency = None,  # type: ignore
# ) -> CentroTreinamentoOut:

#     session: AsyncSession = db_session

#     ct = CentroTreinamentoModel(
#         nome=centro_treinamento_in.nome,
#         endereco=centro_treinamento_in.endereco,
#         proprietario=centro_treinamento_in.proprietario,
#     )

#     session.add(ct)
#     await session.commit()
#     await session.refresh(ct)

#     return CentroTreinamentoOut.model_validate(ct)



