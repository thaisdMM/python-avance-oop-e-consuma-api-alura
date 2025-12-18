from fastapi import FastAPI

# app: objeto de FastAPI
app = FastAPI()


# 1- Criando a primeira rota Hello World
#  servidor rodando localmente na nossa máquina
@app.get("/api/hello")
def hello_world():
    return {"Hello": "World"}
