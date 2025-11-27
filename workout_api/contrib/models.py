from uuid import uuid4
from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

# Criar colunas nos bancos de dados
class BaseModel(DeclarativeBase):
    id:Mapped[UUID] = mapped_column(PG_UUID( as_uuid=True), default=uuid4, unique=True, nullable=False)