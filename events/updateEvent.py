from googleapiclient.discovery import build
from auth.auth import main

def update_event(event):
    # Obtiene las credenciales de autenticación
    creds = main()
    # Construye el servicio de la API de Google Calendar con las credenciales
    service = build('calendar', 'v3', credentials=creds)
    # Obtiene el evento existente que se va a actualizar
    event = service.events().get(calendarId='primary', eventId=event['id']).execute()

    # Solicita al usuario que ingrese los nuevos detalles del evento
    summary = input("Ingresa el nuevo resumen del evento: ")
    location = input("Ingresa la nueva ubicación del evento: ")
    description = input("Ingresa la nueva descripción del evento: ")
    start_time = input("Ingresa la nueva hora de inicio del evento (formato: YYYY-MM-DDTHH:MM:SS-05:00): ")
    end_time = input("Ingresa la nueva hora de finalización del evento (formato: YYYY-MM-DDTHH:MM:SS-05:00): ")

    # Actualiza los detalles del evento con la nueva información proporcionada por el usuario
    event['summary'] = summary
    event['location'] = location
    event['description'] = description
    event['start']['dateTime'] = start_time
    event['end']['dateTime'] = end_time

    # Llama a la función update de la API de Google Calendar para actualizar el evento
    updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
    # Devuelve el evento actualizado
    return updated_event
