from googleapiclient.discovery import build
from auth.auth import main
import datetime

def list_events():
    # Obtiene las credenciales de autenticación
    creds = main()
    # Construye el servicio de la API de Google Calendar con las credenciales
    service = build('calendar', 'v3', credentials=creds)
    # Obtiene la hora actual en formato UTC y la convierte a una cadena en formato ISO 8601
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    # Llama a la función list de la API de Google Calendar para obtener una lista de eventos
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    # Extrae la lista de eventos de los resultados
    events = events_result.get('items', [])
    # Devuelve la lista de eventos
    return events
