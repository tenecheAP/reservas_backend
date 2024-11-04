from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    telefono = Column(String)
    hashed_password = Column(String)

    reservas = relationship("Reserva", back_populates="usuario")

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    cantidad_personas = Column(Integer)
    tipo_reserva = Column(String)
    capacidad_carpa = Column(Integer, nullable=True)
    cantidad_comidas = Column(Integer, default=0)
    costo_total = Column(Float)
    estado = Column(String, default="Confirmada")
    ubicacion_camping = Column(String, nullable=True)

    usuario = relationship("Usuario", back_populates="reservas")

class CarpaHabitacion(Base):
    __tablename__ = "carpas_habitaciones"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)
    capacidad = Column(Integer, nullable=False)
    disponibilidad = Column(Boolean, default=True)

class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    reserva_id = Column(Integer, ForeignKey("reservas.id"), nullable=False)
    monto = Column(Float, nullable=False)
    metodo_pago = Column(String, nullable=False)
    estado_pago = Column(String, default="Pendiente")

    reserva = relationship("Reserva")

class ServicioAdicional(Base):
    __tablename__ = "servicios_adicionales"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    costo = Column(Float, nullable=False)

class ReservaServicio(Base):
    __tablename__ = "reserva_servicios"

    reserva_id = Column(Integer, ForeignKey("reservas.id"), primary_key=True)
    servicio_id = Column(Integer, ForeignKey("servicios_adicionales.id"), primary_key=True)
    cantidad = Column(Integer, nullable=False)

    reserva = relationship("Reserva")
    servicio = relationship("ServicioAdicional")
