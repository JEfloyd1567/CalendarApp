from auth.auth import main
from events.listEvents import list_events
from events.createEvent import create_event
from events.updateEvent import update_event
from events.deleteEvent import delete_event
from googleapiclient.discovery import build

def print_menu():
    print("1. Listar eventos")
    print("2. Crear evento")
    print("3. Actualizar evento")
    print("4. Eliminar evento")
    print("5. Salir")

def application():
    creds = main()
    service = build('calendar', 'v3', credentials=creds)
    while True:
        print_menu()
        choice = input("Elige una opción: ")
        if choice == "1":
            events = list_events()
            for i, event in enumerate(events):
                print(f"{i+1}. {event['summary']}")
                print(f"   Ubicación: {event['location']}")
                print(f"   Descripción: {event['description']}")
                print(f"   Fecha de inicio: {event['start']['dateTime']}")
                print(f"   Fecha de finalización: {event['end']['dateTime']}")
        elif choice == "2":
            summary = input("Ingresa el resumen del evento: ")
            location = input("Ingresa la ubicación del evento: ")
            description = input("Ingresa la descripción del evento: ")
            start_time = input("Ingresa la hora de inicio del evento (formato: YYYY-MM-DDTHH:MM:SS-05:00): ")
            end_time = input("Ingresa la hora de finalización del evento (formato: YYYY-MM-DDTHH:MM:SS-05:00): ")
            event = create_event(summary, location, description, start_time, end_time)
            print('Evento creado: %s' % (event.get('htmlLink')))
        elif choice == "3":
            events = list_events()
            for i, event in enumerate(events):
                print(f"{i+1}. {event['summary']}")
            event_index = int(input("Elige el número del evento que deseas actualizar: ")) - 1
            updated_event = update_event(events[event_index])
            print('Evento actualizado: %s' % (updated_event.get('htmlLink')))
        elif choice == "4":
            events = list_events()
            for i, event in enumerate(events):
                print(f"{i+1}. {event['summary']}")
            event_index = int(input("Elige el número del evento que deseas eliminar: ")) - 1
            delete_event(events[event_index])
            print('Evento eliminado')
        elif choice == "5":
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == '__main__':
    application()
