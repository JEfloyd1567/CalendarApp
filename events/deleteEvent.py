from googleapiclient.discovery import build
from auth.auth import main

def delete_event(event):
    creds = main()
    service = build('calendar', 'v3', credentials=creds)
    service.events().delete(calendarId='primary', eventId=event['id']).execute()
