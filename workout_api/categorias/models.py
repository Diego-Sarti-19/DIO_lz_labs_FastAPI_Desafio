from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel

class CategoriaModel(BaseModel):
    __tablename__ = "categorias"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    
    # se quiser a lista de atletas:
    atletas: Mapped[list["AtletaModel"]] = relationship(back_populates="categoria")





























###### ###### ######  ############  ############  ######
# class CategoriaModel(BaseModel):
#     __tablename__ = "categorias"

#     pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     nome: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
#     categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.pk_id"), nullable=False)
# #    atleta: Mapped["AtletaModel"] = relationship(back_populates="categoria")