from googleapiclient.discovery import build
from auth.auth import main

def update_event(event):
    creds = main()
    service = build('calendar', 'v3', credentials=creds)
    event = service.events().get(calendarId='primary', eventId=event['id']).execute()

    summary = input("Ingresa el nuevo resumen del evento: ")
    location = input("Ingresa la nueva ubicación del evento: ")
    description = input("Ingresa la nueva descripción del evento: ")
    start_time = input("Ingresa la nueva hora de inicio del evento (formato: YYYY-MM-DDTHH:MM:SS-05:00): ")
    end_time = input("Ingresa la nueva hora de finalización del evento (formato: YYYY-MM-DDTHH:MM:SS-05:00): ")

    event['summary'] = summary
    event['location'] = location
    event['description'] = description
    event['start']['dateTime'] = start_time
    event['end']['dateTime'] = end_time

    updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
    return updated_event
