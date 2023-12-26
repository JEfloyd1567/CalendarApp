# Importa las funciones necesarias de los otros archivos
from auth.auth import main
from events.listEvents import list_events
from events.createEvent import create_event
from events.updateEvent import update_event
from events.deleteEvent import delete_event
from googleapiclient.discovery import build

# Función para imprimir el menú de opciones
def print_menu():
    print("1. Listar eventos")
    print("2. Crear evento")
    print("3. Actualizar evento")
    print("4. Eliminar evento")
    print("5. Salir")

# Función principal de la aplicación
def application():
    # Obtiene las credenciales de autenticación
    creds = main()
    # Construye el servicio de la API de Google Calendar con las credenciales
    service = build('calendar', 'v3', credentials=creds)
    # Bucle principal de la aplicación
    while True:
        # Imprime el menú de opciones
        print_menu()
        # Solicita al usuario que elija una opción
        choice = input("Elige una opción: ")
        # Ejecuta la opción elegida por el usuario
        if choice == "1":
            # Lista los eventos
            events = list_events()
            for i, event in enumerate(events):
                print(f"{i+1}. {event['summary']}")
                print(f"   Ubicación: {event['location']}")
                print(f"   Descripción: {event['description']}")
                print(f"   Fecha de inicio: {event['start']['dateTime']}")
                print(f"   Fecha de finalización: {event['end']['dateTime']}")
        elif choice == "2":
            # Crea un evento
            summary = input("Ingresa el resumen del evento: ")
            location = input("Ingresa la ubicación del evento: ")
            description = input("Ingresa la descripción del evento: ")
            start_time = input("Ingresa la hora de inicio del evento (formato: YYYY-MM-DDTHH:MM:SS-05:00): ")
            end_time = input("Ingresa la hora de finalización del evento (formato: YYYY-MM-DDTHH:MM:SS-05:00): ")
            event = create_event(summary, location, description, start_time, end_time)
            print('Evento creado: %s' % (event.get('htmlLink')))
        elif choice == "3":
            # Actualiza un evento
            events = list_events()
            for i, event in enumerate(events):
                print(f"{i+1}. {event['summary']}")
            event_index = int(input("Elige el número del evento que deseas actualizar: ")) - 1
            updated_event = update_event(events[event_index])
            print('Evento actualizado: %s' % (updated_event.get('htmlLink')))
        elif choice == "4":
            # Elimina un evento
            events = list_events()
            for i, event in enumerate(events):
                print(f"{i+1}. {event['summary']}")
            event_index = int(input("Elige el número del evento que deseas eliminar: ")) - 1
            delete_event(events[event_index])
            print('Evento eliminado')
        elif choice == "5":
            # Sale de la aplicación
            break
        else:
            # Informa al usuario si ha elegido una opción no válida
            print("Opción no válida. Por favor, elige una opción del menú.")

# Ejecuta la función principal si el archivo se ejecuta como un script
if __name__ == '__main__':
    application()
