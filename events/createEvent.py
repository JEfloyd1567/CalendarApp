from googleapiclient.discovery import build
from auth.auth import main

def create_event(summary, location, description, start_time, end_time):
    # Obtiene las credenciales de autenticación
    creds = main()
    # Construye el servicio de la API de Google Calendar con las credenciales
    service = build('calendar', 'v3', credentials=creds)
    # Crea un diccionario que contiene los detalles del evento que se va a crear
    event = {
      'summary': summary,
      'location': location,
      'description': description,
      'start': {
        'dateTime': start_time,
        'timeZone': 'America/Bogota',
      },
      'end': {
        'dateTime': end_time,
        'timeZone': 'America/Bogota',
      },
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }
    # Llama a la función insert de la API de Google Calendar para crear el nuevo evento
    event = service.events().insert(calendarId='primary', body=event).execute()
    # Devuelve el evento creado
    return event
