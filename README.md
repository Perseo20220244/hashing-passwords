# Proyecto Django - Hashing de Contraseñas

Este es un proyecto simple de Django que utiliza el hashing de contraseñas para proteger las credenciales de inicio de sesión de los usuarios. Este proyecto incluye una página de login donde se puede comprobar que las contraseñas están almacenadas de forma segura.

## Requisitos

- Python 3.x
- Django 4.x (o versión compatible)
- SQLite (base de datos predeterminada de Django)

## Pasos para ejecutar el proyecto

1. **Clonar el repositorio**: Primero, clona el repositorio a tu máquina local. Abre una terminal y ejecuta:

git clone https://github.com/Perseo20220244/hashing-passwords.git
cd hashing_pswd

2. **Crear un entorno virtual e instalar las dependencias**: Dentro del directorio de tu proyecto, crea un entorno virtual y activa el entorno para instalar las dependencias necesarias:

- Crear un entorno virtual:
  ```
  python -m venv venv
  ```
- Activar el entorno virtual:
  - En Linux/macOS:
    ```
    source venv/bin/activate
    ```
  - En Windows:
    ```
    venv\Scripts\activate
    ```
- Con el entorno virtual activado, instala las dependencias con:
  ```
  pip install -r requirements.txt
  ```

3. **Migrar la base de datos**: Django necesita configurar las tablas de la base de datos. Para ello, ejecuta el siguiente comando:

   ```
   python manage.py migrate
   ```

4. **Crear un usuario de prueba (opcional)**: Puedes crear un usuario de prueba desde el shell de Django para poder autenticarte en el login.

- Accede al shell de Django:
  ```
  python manage.py shell
  ```
- Dentro del shell de Django, ejecuta el siguiente código para crear un usuario:
  ```python
  from accounts.models import User
  user = User(username="tuusuario")
  user.set_password("tucontraseña")  # Hashea la contraseña
  user.save()  # Guarda el usuario en la base de datos
  ```

5. **Iniciar el servidor de desarrollo**: Una vez que tengas todo listo, puedes iniciar el servidor de desarrollo de Django:
   ```
   python manage.py runserver
   ```

Accede a la aplicación en tu navegador en la siguiente URL:
http://127.0.0.1:8000/accounts/login

6. **Verificar el hasheo de la contraseña**: Para asegurarte de que la contraseña se está almacenando correctamente en forma de hash, sigue estos pasos:

- Vuelve a ingresar al shell de Django con:
  ```
  python manage.py shell
  ```
- Obtén el usuario que creaste:
  ```python
  user = User.objects.get(username="tuusuario")
  print(user.password)  # Muestra el hash de la contraseña
  ```
  El resultado será algo similar a esto:
  ```
  pbkdf2_sha256$260000$xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx$xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  ```
  Este es el hash de la contraseña. El algoritmo que se usa por defecto es **PBKDF2 con SHA-256**, que es un método seguro para almacenar contraseñas.

---

## Notas

- **PBKDF2 con SHA-256** es el algoritmo de hashing utilizado por Django para las contraseñas. Este algoritmo es seguro y recomendado para almacenar contraseñas de manera eficiente.
- Si deseas cambiar la configuración de seguridad o el algoritmo de hashing, puedes hacerlo editando el archivo `settings.py` de Django, donde se especifican las configuraciones de seguridad para las contraseñas.
- Este proyecto usa **SQLite** como base de datos por defecto, pero puedes cambiar a otra base de datos como MySQL o PostgreSQL si lo prefieres, modificando la configuración en `settings.py`.

---

ESTRUSCURA DEL PROYECTO

hashing passwords/
│
├── hashing_pswd/ # Carpeta del proyecto Django
│ ├── accounts/ # Aplicación Django de cuentas
│ │ ├── migrations/ # Migraciones de Django (no debes modificar)
│ │ ├── templates/ # Plantillas HTML
│ │ ├── **init**.py # Inicialización de la app
│ │ ├── admin.py # Configuración de administrador
│ │ ├── apps.py # Configuración de la app
│ │ ├── models.py # Modelos de la app
│ │ ├── tests.py # Pruebas unitarias
│ │ ├── urls.py # Rutas de la app
│ │ └── views.py # Vistas de la app
│ ├── db.sqlite3 # Base de datos SQLite (puedes omitir esto si no lo quieres subir)
│ ├── hashing_pswd/ # Carpeta principal del proyecto Django
│ │ ├── settings.py # Configuración de Django
│ │ ├── urls.py # Rutas del proyecto Django
│ │ ├── wsgi.py # Interfaz WSGI para producción
│ │ ├── asgi.py # Interfaz ASGI para la comunicación en tiempo real
│ │ └── manage.py # Script de administración de Django
├── venv/ # Entorno virtual (sería mejor que no lo subas, ya que es específico de tu máquina)
├── .gitignore # Archivos y carpetas que no serán subidos a GitHub
├── requirements.txt # Requerimientos para instalar dependencias
└── README.md # Instrucciones sobre cómo ejecutar el proyecto
