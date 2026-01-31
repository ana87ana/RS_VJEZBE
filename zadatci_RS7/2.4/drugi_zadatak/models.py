from pydantic import BaseModel, Field
from datetime import datetime

class ObjavaCreate(BaseModel):
    korisnik: str = Field(..., max_length=20)
    tekst: str = Field(..., max_length=280)
    vrijeme: datetime

class Objava(ObjavaCreate):
    id: int

class AuthKorisnik(BaseModel): 
    korisnicko_ime: str 
    lozinka: str