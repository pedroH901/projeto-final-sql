from fastapi import FastAPI
from typing import List
import json

app = FastAPI()

@app.get("/pets")
def listar_pets():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, endereco, descricao, status, imagem_url FROM Pets")
    
    pets = []
    for row in cursor.fetchall():
        pets.append({
            "id": row.id,
            "nome": row.nome,
            "endereco": row.endereco,
            "descricao": row.descricao,
            "status": row.status,
            "imagem_url": row.imagem_url
        })
    
    conn.close()
    return pets
