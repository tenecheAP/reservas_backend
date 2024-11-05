from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine
import models, schemas, crud
from passlib.context import CryptContext

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Esto permite todos los métodos HTTP, incluyendo DELETE
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "¡La API está en línea!"}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Nuevo endpoint para login
@app.post("/usuarios/login")
async def login(email: str, password: str, db: Session = Depends(get_db)):
    try:
        # Buscar usuario por email
        usuario = crud.get_usuario_by_email(db, email=email)
        print(f"Usuario encontrado: {usuario}")
        print(f"Email recibido: {email}")
        print(f"Contraseña recibida: {password}")
        
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        # Verificar contraseña usando pwd_context.verify
        verificacion = pwd_context.verify(password, usuario.hashed_password)
        print(f"Resultado de verificación: {verificacion}")
        
        if not verificacion:
            raise HTTPException(status_code=400, detail="Contraseña incorrecta")
        
        return {
            "id": usuario.id, 
            "email": usuario.email, 
            "nombre": usuario.nombre,
            "telefono": usuario.telefono
        }
    except Exception as e:
        print(f"Error en login: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/usuarios/", response_model=schemas.Usuario)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario_by_email(db, email=usuario.email)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    return crud.crear_usuario(db=db, usuario=usuario)

@app.get("/usuarios/", response_model=List[schemas.Usuario])
def leer_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    usuarios = crud.get_usuarios(db, skip=skip, limit=limit)
    return usuarios

@app.get("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def leer_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@app.post("/reservas/", response_model=schemas.Reserva)
def crear_reserva(reserva: schemas.ReservaCreate, db: Session = Depends(get_db)):
    try:
        return crud.crear_reserva(db=db, reserva=reserva)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/reservas/", response_model=List[schemas.Reserva])
def leer_reservas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reservas = crud.get_reservas(db, skip=skip, limit=limit)
    return reservas

@app.get("/reservas/{reserva_id}", response_model=schemas.Reserva)
def leer_reserva(reserva_id: int, db: Session = Depends(get_db)):
    db_reserva = crud.get_reserva(db, reserva_id=reserva_id)
    if db_reserva is None:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return db_reserva

@app.delete("/reservas/{reserva_id}")
async def eliminar_reserva(reserva_id: int, db: Session = Depends(get_db)):
    try:
        # Usar la función eliminar_reserva del módulo crud
        resultado = crud.eliminar_reserva(db, reserva_id)
        if resultado:
            return {"message": f"Reserva {reserva_id} eliminada exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Reserva no encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
