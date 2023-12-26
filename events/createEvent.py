from googleapiclient.discovery import build
from auth.auth import main



def create_event(summary, location, description, start_time, end_time):
    creds = main()
    service = build('calendar', 'v3', credentials=creds)
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
    event = service.events().insert(calendarId='primary', body=event).execute()
    return event
