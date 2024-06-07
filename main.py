from fastapi import  FastAPI
import requests

app = FastAPI()

#pegar valores das API
#criar rotas com logica de acordo com a acao desejada

@app.get("/")
def root():
    return {"Hello": "World"}