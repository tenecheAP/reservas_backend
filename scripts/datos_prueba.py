import requests
import json
from datetime import datetime

# Datos de prueba - 10 usuarios
usuarios_prueba = [
    {
        "nombre": "Ana Martínez",
        "email": "ana@camping.com",
        "telefono": "3001234567",
        "password": "ana123"
    },
    {
        "nombre": "Luis Rodriguez",
        "email": "luis@camping.com",
        "telefono": "3109876543",
        "password": "luis456"
    },
    {
        "nombre": "Sofia Vargas",
        "email": "sofia@camping.com",
        "telefono": "3205555555",
        "password": "sofia789"
    },
    {
        "nombre": "Diego Castro",
        "email": "diego@camping.com",
        "telefono": "3157777777",
        "password": "diego321"
    },
    {
        "nombre": "Valentina Ruiz",
        "email": "vale@camping.com",
        "telefono": "3008888888",
        "password": "vale654"
    },
    {
        "nombre": "Carlos Pérez",
        "email": "carlos@camping.com",
        "telefono": "3112223333",
        "password": "carlos987"
    },
    {
        "nombre": "María López",
        "email": "maria@camping.com",
        "telefono": "3223334444",
        "password": "maria123"
    },
    {
        "nombre": "Juan Gómez",
        "email": "juan@camping.com",
        "telefono": "3134445555",
        "password": "juan456"
    },
    {
        "nombre": "Laura Torres",
        "email": "laura@camping.com",
        "telefono": "3145556666",
        "password": "laura789"
    },
    {
        "nombre": "Pedro Ramírez",
        "email": "pedro@camping.com",
        "telefono": "3156667777",
        "password": "pedro321"
    }
]

# Datos de prueba - Reservas para cada usuario
reservas_prueba = [
    # Reservas para Usuario 1 (Ana)
    {
        "fecha_inicio": "2024-11-01",
        "fecha_fin": "2024-11-05",  # 4 días de estancia
        "cantidad_personas": 2,
        "tipo_reserva": "carpa",
        "capacidad_carpa": 2,
        "cantidad_comidas": 2,
        "costo_total": 80000.0,
        "estado": "Confirmada",
        "ubicacion_camping": "A",
        "usuario_id": 1
    },
    {
        "fecha_inicio": "2024-12-24",
        "fecha_fin": "2024-12-28",  # 4 días de estancia
        "cantidad_personas": 4,
        "tipo_reserva": "cabaña",
        "capacidad_carpa": 4,
        "cantidad_comidas": 3,
        "costo_total": 350000.0,
        "estado": "Pendiente",
        "ubicacion_camping": "B",
        "usuario_id": 1
    },
    # Reservas para Usuario 2 (Luis)
    {
        "fecha_inicio": "2024-11-15",
        "fecha_fin": "2024-11-20",  # 5 días de estancia
        "cantidad_personas": 3,
        "tipo_reserva": "carpa",
        "capacidad_carpa": 3,
        "cantidad_comidas": 2,
        "costo_total": 120000.0,
        "estado": "Confirmada",
        "ubicacion_camping": "C",
        "usuario_id": 2
    },
    # Reservas para Usuario 3 (Sofia)
    {
        "fecha_inicio": "2024-12-01",
        "fecha_fin": "2024-12-05",
        "cantidad_personas": 5,
        "tipo_reserva": "cabaña",
        "capacidad_carpa": 5,
        "cantidad_comidas": 3,
        "costo_total": 450000.0,
        "estado": "Confirmada",
        "ubicacion_camping": "A",
        "usuario_id": 3
    },
    # Reservas para Usuario 4 (Diego)
    {
        "fecha_inicio": "2024-12-30",
        "fecha_fin": "2025-01-02",
        "cantidad_personas": 6,
        "tipo_reserva": "cabaña",
        "capacidad_carpa": 6,
        "cantidad_comidas": 3,
        "costo_total": 500000.0,
        "estado": "Pendiente",
        "ubicacion_camping": "B",
        "usuario_id": 4
    },
    # Reservas para Usuario 5 (Valentina)
    {
        "fecha_inicio": "2025-01-15",
        "fecha_fin": "2025-01-20",
        "cantidad_personas": 4,
        "tipo_reserva": "carpa",
        "capacidad_carpa": 4,
        "cantidad_comidas": 2,
        "costo_total": 200000.0,
        "estado": "Confirmada",
        "ubicacion_camping": "C",
        "usuario_id": 5
    },
    # Reservas para Usuario 6 (Carlos)
    {
        "fecha_inicio": "2025-02-01",
        "fecha_fin": "2025-02-03",
        "cantidad_personas": 2,
        "tipo_reserva": "carpa",
        "capacidad_carpa": 2,
        "cantidad_comidas": 1,
        "costo_total": 90000.0,
        "estado": "Confirmada",
        "ubicacion_camping": "A",
        "usuario_id": 6
    },
    # Reservas para Usuario 7 (María)
    {
        "fecha_inicio": "2025-02-14",
        "fecha_fin": "2025-02-16",
        "cantidad_personas": 2,
        "tipo_reserva": "cabaña",
        "capacidad_carpa": 2,
        "cantidad_comidas": 2,
        "costo_total": 250000.0,
        "estado": "Pendiente",
        "ubicacion_camping": "B",
        "usuario_id": 7
    },
    # Reservas para Usuario 8 (Juan)
    {
        "fecha_inicio": "2025-03-01",
        "fecha_fin": "2025-03-05",
        "cantidad_personas": 8,
        "tipo_reserva": "cabaña",
        "capacidad_carpa": 8,
        "cantidad_comidas": 3,
        "costo_total": 600000.0,
        "estado": "Confirmada",
        "ubicacion_camping": "C",
        "usuario_id": 8
    },
    # Reservas para Usuario 9 (Laura)
    {
        "fecha_inicio": "2025-04-10",
        "fecha_fin": "2025-04-15",
        "cantidad_personas": 3,
        "tipo_reserva": "carpa",
        "capacidad_carpa": 3,
        "cantidad_comidas": 2,
        "costo_total": 150000.0,
        "estado": "Pendiente",
        "ubicacion_camping": "A",
        "usuario_id": 9
    },
    # Reservas para Usuario 10 (Pedro)
    {
        "fecha_inicio": "2025-05-01",
        "fecha_fin": "2025-05-03",
        "cantidad_personas": 4,
        "tipo_reserva": "cabaña",
        "capacidad_carpa": 4,
        "cantidad_comidas": 3,
        "costo_total": 300000.0,
        "estado": "Confirmada",
        "ubicacion_camping": "B",
        "usuario_id": 10
    }
]

def crear_datos_prueba():
    base_url = 'http://localhost:8000'
    
    print("\n=== Creando Usuarios ===")
    for usuario in usuarios_prueba:
        try:
            response = requests.post(f'{base_url}/usuarios/', json=usuario)
            if response.status_code == 200:
                print(f"✓ Usuario creado: {usuario['nombre']}")
            else:
                print(f"✗ Error al crear usuario {usuario['nombre']}: {response.text}")
        except Exception as e:
            print(f"✗ Error: {str(e)}")
    
    print("\n=== Creando Reservas ===")
    for reserva in reservas_prueba:
        try:
            # Validar fechas antes de enviar
            fecha_inicio = datetime.strptime(reserva['fecha_inicio'], "%Y-%m-%d")
            fecha_fin = datetime.strptime(reserva['fecha_fin'], "%Y-%m-%d")
            
            if fecha_fin < fecha_inicio:
                print(f"✗ Error: Fechas inválidas para reserva de usuario {reserva['usuario_id']}")
                continue
                
            response = requests.post(f'{base_url}/reservas/', json=reserva)
            if response.status_code == 200:
                dias_estancia = (fecha_fin - fecha_inicio).days
                print(f"✓ Reserva creada: {reserva['fecha_inicio']} - Usuario {reserva['usuario_id']} ({dias_estancia} días)")
            else:
                print(f"✗ Error al crear reserva: {response.text}")
        except Exception as e:
            print(f"✗ Error: {str(e)}")

if __name__ == "__main__":
    print("Iniciando creación de datos de prueba...")
    crear_datos_prueba()
    print("\n¡Proceso completado!")
