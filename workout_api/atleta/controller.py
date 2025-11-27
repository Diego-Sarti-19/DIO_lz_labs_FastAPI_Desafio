from datetime import datetime

from fastapi import APIRouter, Body, status, HTTPException
from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from workout_api.contrib.dependencias import Databasedependency
from workout_api.atleta.schemas import AtletaIn, AtletaOut,AtletaUpdate
from workout_api.atleta.models import AtletaModel
from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento.models import CentroTreinamentoModel

# 👇 define prefixo e tag aqui
router = APIRouter(
    prefix="/atletas",
    tags=["atletas"],
)


@router.post(
    "/",
    summary="Criar um novo atleta",
    description="Cria um novo atleta no sistema.",
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut,
)
async def post(
    atleta_in: AtletaIn = Body(...),
    db_session: Databasedependency = None,  # type: ignore
) -> AtletaOut:
    session: AsyncSession = db_session

    # valida categoria
    categoria_result = await session.execute(
        select(CategoriaModel).where(CategoriaModel.pk_id == atleta_in.categoria_id)
    )
    if not categoria_result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Categoria não encontrada.")

    # valida centro de treinamento
    ct_result = await session.execute(
        select(CentroTreinamentoModel).where(
            CentroTreinamentoModel.pk_id == atleta_in.centro_treinamento_id
        )
    )
    if not ct_result.scalar_one_or_none():
        raise HTTPException(
            status_code=404, detail="Centro de treinamento não encontrado."
        )

    atleta = AtletaModel(
        nome=atleta_in.nome,
        cpf=atleta_in.cpf,
        idade=atleta_in.idade,
        peso=atleta_in.peso,
        altura=atleta_in.altura,
        sexo=atleta_in.sexo,
        created_at=datetime.utcnow(),
        categoria_id=atleta_in.categoria_id,
        centro_treinamento_id=atleta_in.centro_treinamento_id,
    )

    session.add(atleta)
    await session.commit()
    await session.refresh(atleta)

    return AtletaOut.model_validate(atleta)


@router.get(
    "/",
    summary="Consultar todos os atletas",
    description="Consulta todos os atletas no sistema.",
    status_code=status.HTTP_200_OK,
    response_model=list[AtletaOut],
)
async def query(db_session: Databasedependency) -> list[AtletaOut]:
    session: AsyncSession = db_session

    result = await session.execute(select(AtletaModel))
    atletas = result.scalars().all()

    return [AtletaOut.model_validate(c) for c in atletas]


@router.get(
    "/{id}",
    summary="Consultar um atleta",
    description="Consulta um atleta no sistema.",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def query(id: UUID4, db_session: Databasedependency) -> AtletaOut:
    atletas: AtletaOut = (
        await db_session.execute(select(AtletaModel).where(AtletaModel.id == id))
        ).scalars().first()
    
    if not atletas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Atleta não encontrado{id}")
    return AtletaOut.model_validate(atletas)  
@router.patch(
    "/{pk_id}",
    summary="Editar um atleta",
    description="Edita parcialmente um atleta no sistema.",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def update(
    pk_id: int,
    atleta_update: AtletaUpdate = Body(...),
    db_session: Databasedependency = None  # type: ignore
) -> AtletaOut:
    session: AsyncSession = db_session

    atleta: AtletaModel | None = await session.get(AtletaModel, pk_id)

    if not atleta:
        raise HTTPException(status_code=404, detail=f"Atleta {pk_id} não encontrado")

    # Atualiza somente campos enviados
    if atleta_update.nome is not None:
        atleta.nome = atleta_update.nome

    if atleta_update.idade is not None:
        atleta.idade = atleta_update.idade

    await session.commit()
    await session.refresh(atleta)

    return AtletaOut.model_validate(atleta)


@router.delete(
    "/{pk_id}",
    summary="Remover um atleta",
    description="Remove um atleta do sistema pelo ID (pk_id).",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_atleta(
    pk_id: int,
    db_session: Databasedependency = None,  # type: ignore
) -> None:
    session: AsyncSession = db_session

    atleta: AtletaModel | None = await session.get(AtletaModel, pk_id)

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atleta {pk_id} não encontrado",
        )

    await session.delete(atleta)
    await session.commit()
    # 204 → sem body, só status mesmo
    return



### Versão simplificada sem validações adicionais ###   

# from datetime import datetime
# from fastapi import APIRouter, Body, status
# from workout_api.contrib.dependencias import Databasedependency
# from workout_api.atleta.schemas import AtletaIn, AtletaOut
# from workout_api.atleta.models import AtletaModel
# from sqlalchemy.future import select
# from workout_api.categorias.models import CategoriaModel
# from workout_api.centro_treinamento.models import CentroTreinamentoModel
# from uuid import uuid4

# router = APIRouter()

# @router.post(
#         "/", summary="Criar um novo atleta",
#         description="Cria um novo atleta no sistema.",  
#         status_code= status.HTTP_201_CREATED
# )        


# async def post(
#     db_session : Databasedependency, 
#     atleta_in: AtletaIn =Body(...)
    
#     ):
#     categotia = (await db_session.execute(
#         select(CategoriaModel).where(CategoriaModel.pk_id == atleta_in.categoria_id)
#                                           )).first()
#     centro_treinamento = (await db_session.execute(
#         select(CentroTreinamentoModel).where(CentroTreinamentoModel.pk_id == atleta_in.centro_treinamento_id)
#     )).first()
          
#     atleta_out = AtletaOut(id=uuid4(),created_at=datetime.utcnow(),  **atleta_in.model_dump()) 
#     atleta_model = AtletaModel(**atleta_out.model_dump())

#     db_session.add(atleta_model)
#     await db_session.commit()

#     return atleta_out     


    