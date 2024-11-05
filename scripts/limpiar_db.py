import requests

def limpiar_base_datos():
    base_url = 'http://localhost:8000'
    try:
        # Primero eliminar todas las reservas
        print("\nEliminando reservas...")
        response = requests.get(f'{base_url}/reservas/')
        if response.ok:
            reservas = response.json()
            for reserva in reservas:
                delete_response = requests.delete(f'{base_url}/reservas/{reserva["id"]}')
                if delete_response.ok:
                    print(f"✓ Reserva {reserva['id']} eliminada")
                else:
                    print(f"✗ Error al eliminar reserva {reserva['id']}")
        
        # Luego eliminar usuarios
        print("\nEliminando usuarios...")
        response = requests.get(f'{base_url}/usuarios/')
        if response.ok:
            usuarios = response.json()
            for usuario in usuarios:
                delete_response = requests.delete(f'{base_url}/usuarios/{usuario["id"]}')
                if delete_response.ok:
                    print(f"✓ Usuario {usuario['nombre']} eliminado")
                else:
                    print(f"✗ Error al eliminar usuario {usuario['id']}")
        
        print("\n✓ Base de datos limpiada exitosamente")
    except Exception as e:
        print(f"\n✗ Error al limpiar la base de datos: {str(e)}")

if __name__ == "__main__":
    print("¡ADVERTENCIA! Esto eliminará todos los datos de la base de datos.")
    print("¿Estás seguro de que deseas continuar? (s/n)")
    if input().lower() == 's':
        limpiar_base_datos()
    else:
        print("Operación cancelada")
