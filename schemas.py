from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class ReservaBase(BaseModel):
    fecha_inicio: date
    fecha_fin: date
    cantidad_personas: int
    tipo_reserva: str
    capacidad_carpa: Optional[int] = None
    cantidad_comidas: int = 0
    costo_total: float
    estado: str = "Confirmada"
    ubicacion_camping: Optional[str] = None

class ReservaCreate(ReservaBase):
    usuario_id: int

class Reserva(ReservaBase):
    id: int
    usuario_id: int

    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    nombre: str
    email: str
    telefono: Optional[str] = None

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int
    reservas: List[Reserva] = []

    class Config:
        orm_mode = True

class LoginData(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    id: int
    email: str
    nombre: str
    telefono: str
