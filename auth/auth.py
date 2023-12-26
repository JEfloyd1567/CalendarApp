import os.path
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Define el alcance de los permisos que tu aplicación solicitará al usuario
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    # Inicializa las credenciales en None
    creds = None
    # Verifica si ya existe un token guardado
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            # Carga las credenciales del token
            creds = pickle.load(token)
    # Si no hay credenciales cargadas o si las credenciales cargadas no son válidas, entonces necesitas obtener nuevas credenciales
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Si las credenciales han expirado pero tienen un token de actualización, puedes usar ese token para obtener nuevas credenciales sin necesidad de que el usuario vuelva a autenticarse
            creds.refresh(Request())
        else:
            # Si no hay credenciales cargadas o si las credenciales cargadas no tienen un token de actualización, entonces necesitas autenticarte de nuevo
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'credentials.json'), SCOPES)
            creds = flow.run_local_server(port=0)
        # Guarda las credenciales para uso futuro
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    # Devuelve las credenciales
    return creds
