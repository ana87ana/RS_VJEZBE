from fastapi import FastAPI, HTTPException
from models import Objava, ObjavaCreate
from typing import List

app = FastAPI()

objave: List[Objava] = []
next_id = 1

@app.post("/objava", response_model=Objava)
async def post_objava(nova_objava: ObjavaCreate):
    global next_id

    objava = Objava(
        id=next_id,
        korisnik=nova_objava.korisnik,
        tekst=nova_objava.tekst,
        vrijeme=nova_objava.vrijeme
    )

    objave.append(objava)
    next_id += 1

    return objava

@app.get("/objava/{id}", response_model=Objava)
async def get_objava(id: int):
    for objava in objave:
        if objava.id == id:
            return objava

    raise HTTPException(status_code=404, detail="Objava nije pronađena")

@app.get("/korisnici/{korisnik}/objave", response_model=List[Objava])
async def get_objave_korisnika(korisnik: str):
    korisnikove_objave = [o for o in objave if o.korisnik == korisnik]

    if not korisnikove_objave:
        raise HTTPException(status_code=404, detail="Korisnik nema objava ili ne postoji")

    return korisnikove_objave

@app.get("/")
def read_root():
    return {"message": "Hello, socialAPI!"}
