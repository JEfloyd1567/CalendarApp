from googleapiclient.discovery import build
from auth.auth import main

def delete_event(event):
    # Obtiene las credenciales de autenticación
    creds = main()
    # Construye el servicio de la API de Google Calendar con las credenciales
    service = build('calendar', 'v3', credentials=creds)
    # Llama a la función delete de la API de Google Calendar para eliminar el evento
    service.events().delete(calendarId='primary', eventId=event['id']).execute()
