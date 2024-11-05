from sqlalchemy.orm import Session
import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

def get_usuario_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    hashed_password = pwd_context.hash(usuario.password)
    db_usuario = models.Usuario(email=usuario.email, nombre=usuario.nombre, telefono=usuario.telefono, hashed_password=hashed_password)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def get_reservas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reserva).offset(skip).limit(limit).all()

def crear_reserva(db: Session, reserva: schemas.ReservaCreate):
    try:
        # Verifica si el usuario existe
        usuario = db.query(models.Usuario).filter(models.Usuario.id == reserva.usuario_id).first()
        if not usuario:
            raise ValueError(f"Usuario con id {reserva.usuario_id} no encontrado")
        
        db_reserva = models.Reserva(**reserva.dict())
        db.add(db_reserva)
        db.commit()
        db.refresh(db_reserva)
        return db_reserva
    except Exception as e:
        db.rollback()
        print(f"Error al crear reserva: {str(e)}")
        raise

def get_reserva(db: Session, reserva_id: int):
    return db.query(models.Reserva).filter(models.Reserva.id == reserva_id).first()

def eliminar_reserva(db: Session, reserva_id: int):
    try:
        reserva = db.query(models.Reserva).filter(models.Reserva.id == reserva_id).first()
        if reserva:
            db.delete(reserva)
            db.commit()
            return True
        return False
    except Exception as e:
        db.rollback()
        print(f"Error al eliminar reserva: {str(e)}")
        raise

def modificar_reserva(db: Session, reserva_id: int, nueva_info: schemas.ReservaCreate):
    reserva = db.query(models.Reserva).filter(models.Reserva.id == reserva_id).first()
    if reserva:
        for key, value in nueva_info.dict().items():
            setattr(reserva, key, value)
        db.commit()
        db.refresh(reserva)
        return reserva
    return None 
