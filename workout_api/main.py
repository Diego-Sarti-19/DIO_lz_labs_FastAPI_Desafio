from fastapi import APIRouter, FastAPI
from workout_api.routers import api_router


# Primeiro cria o app
app = FastAPI(
    title="Workout API",
    version="1.0.3"
)

# Depois declara a rota raiz
@app.get("/")
async def root():
    return {"message": "API funcionando!"}

app.include_router(api_router)




# carregar servido no terminal com: uvicorn workout_api.main:app --reload
# http://127.0.0.1:8000/docs

# app = FastAPI(title="Workout API", version="1.0.0")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", reload=True) 



# ######################### CHAT GPT #########################
# from fastapi import FastAPI

# from workout_api.categorias.controller import router as categorias_router
# from workout_api.atleta.controller import router as atleta_router
# from workout_api.centro_treinamento.controller import router as centros_router

# # 👇 ISSO É O QUE O Uvicorn PROCURA:
# app = FastAPI(title="Workout API")


# @app.get("/")
# async def root():
#     return {"message": "OK"}


# # Registrando as rotas
# app.include_router(
#     categorias_router,
#     prefix="/categorias",
#     tags=["Categorias"],
# )

# app.include_router(
#     atleta_router,
#     prefix="/atletas",
#     tags=["Atletas"],
# )

# app.include_router(
#     centros_router,
#     prefix="/centros-treinamento",
#     tags=["Centros de Treinamento"],
# )