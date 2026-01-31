from fastapi import FastAPI, HTTPException
import aiohttp
from models import Objava, ObjavaCreate, AuthKorisnik
from typing import List
import os
from dotenv import load_dotenv
load_dotenv()
PORT = os.getenv("PORT_1")

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
async def get_objave_korisnika(korisnik: str, auth: AuthKorisnik):
    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "http://modest_torvalds:${PORT}/login",
            json={"korisnicko_ime": auth.korisnicko_ime, "lozinka": auth.lozinka}
        ) as odgovor:
            data = await odgovor.json()

            if not data.get("authorized"):
                raise HTTPException(status_code=401, detail="Krivi korisnički podaci")

    korisničke_objave = [o for o in objave if o.korisnik == korisnik]

    if not korisničke_objave:
        raise HTTPException(status_code=404, detail="Korisnik nema objava ili ne postoji")

    return korisničke_objave


@app.get("/")
def read_root():
    return {"message": "Hello, socialAPI!"}
