# workout_api/atleta/schemas.py

from typing import Annotated, Optional
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome completo do atleta", example="João Silva", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="12345678900",max_length=14)]
    idade: Annotated[int, Field(description="Idade do atleta",example=30)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta",example=70.5)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta",example=1.75)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)]

    # ESTES DOIS PRECISAM EXISTIR AQUI,
    # porque o AtletaModel exige e são NOT NULL no banco
    categoria_id: Annotated[int, Field(description="ID da categoria",example=1)]
    centro_treinamento_id: Annotated[int, Field(description="ID do centro de treinamento",example=1)]


class AtletaIn(Atleta):
    """Campos de entrada (POST/PUT)"""
    pass


class AtletaOut(Atleta, OutMixin):
    """Resposta (GET/POST) – herda pk_id, created_at etc. do OutMixin"""
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(description="Nome completo do atleta", example="João Silva", max_length=50)]
    idade: Annotated[Optional[int], Field(description="Idade do atleta",example=30)]



    pass



# from typing import Annotated
# from pydantic import Field, PositiveFloat
# from workout_api.categorias.schemas import CategoriaIn
# from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta

# from workout_api.contrib.schemas import BaseSchema, OutMixin

# class Atleta(BaseSchema):
#     nome: Annotated[str, Field(description="Nome completo do atleta", example="João Silva", max_length=50)]
#     cpf: Annotated[str, Field(description="CPF do atleta", example="123.456.789-00", max_length=14)]
#     idade: Annotated[int, Field(description="Idade do atleta", example="30")]
#     peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example="70.5")]
#     altura: Annotated[PositiveFloat, Field(description="Altura do atleta", example="1.75")]
#     sexo: Annotated[str, Field(description="Sexo do atleta", example="M ou F", max_length=1)]
#     # Estes dois são obrigatórios no modelo
#     categoria_id: Annotated[CategoriaIn, Field(description="categoria do atleta")]
#     centro_treinamento_id: Annotated[CentroTreinamentoAtleta, Field(description="centro de treinamento do atleta", example=1)]



# class AtletaIn(Atleta):
#     pass

# class AtletaOut(Atleta, OutMixin):
#     pass
