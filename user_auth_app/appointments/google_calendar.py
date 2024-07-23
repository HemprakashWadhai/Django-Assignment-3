import datetime
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'django-appointment-system-1186a2e56ccb.json'

def get_calendar_service():
    """
    Create a Google Calendar API service object.
    """
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=credentials)
    return service

def create_calendar_event(doctor, patient, appointment):
    """
    Create a calendar event for an appointment.
    
    :param doctor: Doctor object with attributes `email` and `get_full_name()`.
    :param patient: Patient object with attributes `email` and `get_full_name()`.
    :param appointment: Appointment object with `date`, `start_time`, and `speciality`.
    """
    service = get_calendar_service()

    start_datetime = datetime.datetime.combine(appointment.date, appointment.start_time)
    end_datetime = start_datetime + datetime.timedelta(minutes=45)

    event = {
        'summary': f'Appointment with Dr. {doctor.get_full_name()}',
        'location': 'Virtual',
        'description': f'Appointment with Dr. {doctor.get_full_name()} for {appointment.speciality}',
        'start': {
            'dateTime': start_datetime.isoformat(),
            'timeZone': 'UTC',  # Update if needed
        },
        'end': {
            'dateTime': end_datetime.isoformat(),
            'timeZone': 'UTC',  # Update if needed
        },
        'attendees': [
            {'email': doctor.email},
            {'email': patient.email},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    try:
        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f'Event created: {event.get("htmlLink")}')
        return event
    except Exception as e:
        print(f'An error occurred: {e}')
        return None
