# Aplicación de Google Calendar

Esta aplicación esta escrita en Python 3.11.0.

Esta es una aplicación de consola en Python que utiliza la API de Google Calendar para listar, crear, actualizar y eliminar eventos.

# Configuración
Paso 1: Obtén las credenciales de Google Cloud
Ve a la Consola de Google Cloud.
Crea un nuevo proyecto.
Habilita la API de Google Calendar para tu proyecto.
Ve a la página de credenciales y crea unas nuevas.
Cuando te lo solicite, descarga el archivo JSON de las credenciales.
Paso 2: Configura el archivo credentials.json
Guarda el archivo JSON de las credenciales como credentials.json en el directorio principal de tu proyecto (veevartTest2/).
Asegúrate de que el archivo credentials.json contiene las siguientes claves: client_id, project_id, auth_uri, token_uri, auth_provider_x509_cert_url, client_secret, redirect_uris.

# Uso
Para usar la aplicación, ejecuta el archivo aplication.py en la consola:

`python application.py`

Se te presentará un menú con las siguientes opciones:

Listar eventos
Crear evento
Actualizar evento
Eliminar evento
Salir
Elige una opción ingresando el número correspondiente.

# Listar eventos
Al elegir esta opción, se mostrarán todos los eventos actuales en tu calendario de Google.

# Crear evento
Al elegir esta opción, se te pedirá que ingreses los detalles del evento, incluyendo el resumen, la ubicación, la descripción, la hora de inicio y la hora de finalización.

# Actualizar evento
Al elegir esta opción, primero se mostrarán todos los eventos actuales. Luego, se te pedirá que elijas el evento que deseas actualizar por su índice en la lista. Después, se te pedirá que ingreses los nuevos detalles del evento.

# Eliminar evento
Al elegir esta opción, primero se mostrarán todos los eventos actuales. Luego, se te pedirá que elijas el evento que deseas eliminar por su índice en la lista.
