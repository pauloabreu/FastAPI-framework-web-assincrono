from fastapi import FastAPI
from pydantic import BaseModel

class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False


app = FastAPI()

produtos = [
    Produto(id=1, nome="Playstation 5", preco=5700.49, em_oferta=True),
    Produto(id=2, nome="Nintento Wii", preco=1450.49),
    Produto(id=3, nome="Xbox 360", preco=1800.49, em_oferta=True),
    Produto(id=4, nome="Playstation 4", preco=2000.50),
    Produto(id=5, nome="Xbox One", preco=5500.49, em_oferta=True),
]


@app.get('/')
async def index():
    return {"message": "Hello World!"}

@app.get('/produtos/{id}')
async def buscar_produto(id: int):
    for produto in produtos:
        if produto.id == id:
            return produto
    return None


@app.put('/produtos/{id}')
async def atualizar_produto(id: int, produto: Produto):
    for prod in produtos:
        if prod.id == id:
            prod = produto
            return prod
    return None