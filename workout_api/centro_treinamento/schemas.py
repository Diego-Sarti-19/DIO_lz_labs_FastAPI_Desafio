
from datetime import datetime
from typing import Annotated
from pydantic import Field,UUID4
from workout_api.contrib.schemas import BaseSchema, OutMixin

class CentroTreinamentoIN(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", example="Body in Shape", max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento", example="Rua das Flores, 123", max_length=60)]
    proprietario: Annotated[str, Field(description="Nome do proprietário do centro de treinamento", example="João Silva", max_length=30)]


class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", example="Body in Shape", max_length=20)]


class CentroTreinamentoOut(CentroTreinamentoIN, OutMixin):
    pk_id: Annotated[int, Field(description="Identificador único do centro de treinamento", example=1)]
    created_at: datetime | None = None  # agora não é obrigatório



############ Versão antiga comentada ############
# from typing import Annotated
# from pydantic import Field, UIID4
# from workout_api.contrib.schemas import BaseSchema

# class CentroTreinamentoIN(BaseSchema):
#     nome: Annotated[str, Field(description="Nome do centro de treinamento", example="Body in Shape", max_length=20)]
#     endereço: Annotated[str, Field(description="Endereço do centro de treinamento", example="Rua das Flores, 123", max_length=60)]
#     proprietario: Annotated[str, Field(description="Nome do proprietário do centro de treinamento", example="João Silva", max_length=30)]


# class CentroTreinamentoAtleta(BaseSchema):
#     nome: Annotated[str, Field(description="Nome do centro de treinamento", example="Body in Shape", max_length=20)]

# class CentroTreinamentoOut(CentroTreinamentoIN):
#     id: Annotated[UIID4, Field(description="Identificador único do centro de treinamento")]
