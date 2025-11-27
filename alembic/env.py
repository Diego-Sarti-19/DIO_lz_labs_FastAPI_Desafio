from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# 👉 Base central do projeto
from workout_api.contrib.models import BaseModel

# 👉 IMPORTAR AS MODELS AQUI (apenas para registrar no metadata)
#    Ajuste os caminhos conforme seus arquivos reais.
from workout_api.atleta.models import AtletaModel 
from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento.models import CentroTreinamentoModel


# Objeto de configuração do Alembic (alembic.ini)
config = context.config

# Logging do Alembic
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata usada para autogenerate
target_metadata = BaseModel.metadata


def run_migrations_offline() -> None:
    """
    Executa migrações em modo offline.
    Gera o SQL sem abrir conexão real com o banco.
    """
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    Executa migrações conectando no banco (modo normal).
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# Router: escolhe offline ou online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()