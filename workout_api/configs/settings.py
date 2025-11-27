from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = Field(
        default="postgresql+asyncpg://workout:workout@localhost:5433/workoutdb",
        env="DB_URL",
    )


settings = Settings()







# from pydantic import Field
# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     DB_URL: str = Field(
#         default="postgresql+asyncpg://workout:workout@localhost:5433/workoutdb", env="DB_URL"
#     )

# settings = Settings()