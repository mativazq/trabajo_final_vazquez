# Proyecto Final

### Alumno: Vazquez Matias

Este proyecto es una aplicación web de reservas creada con Django. Permite a los usuarios registrarse, crear salas y hacer reservas.

## Funcionalidades

- **Registro de Usuario**: Los usuarios pueden registrarse y gestionar sus cuentas.
- **Gestión de Salas**:
  - **Todas las Salas**: Ver todas las salas disponibles.
  - **Crear Sala**: Permite a los usuarios crear nuevas salas.
  - **Buscar Sala**: Opción para buscar salas específicas.
- **Gestión de Reservas**:
  - **Todas las Reservas**: Ver todas las reservas hechas.
  - **Crear Reserva**: Permite a los usuarios hacer nuevas reservas.
  - **Buscar Reserva**: Opción para buscar reservas específicas.

## Requisitos

- Python 3.x
- Django 3.x
- SQLite (por defecto, puede cambiarse a otro gestor de base de datos)

# Comandos

1. Crear proyecto Django
    ```bash
    django-admin startproject <nombre del proyecto que quieran ustedes>
    ```
    en este tutorial utilizaremos como ejemplo:
    ```bash
    django-admin startproject MeetingRooms
    ```

    Si el comando anterior falla, se puede utilizar:

    ```bash
    python -m django startproject nombre_del_proyecto
    # o
    python3 -m django startproject nombre_del_proyecto
    ```
2. Testear servidor
    ```bash
    python manage.py runserver
    ```
3. Crear una `application` dentro de mi proyecto:
    ```bash
    python manage.py startapp <nombre de su aplicacion>
    ```
    en el caso de este tutorial sería `bookings`:
    ```bash
    python manage.py startapp bookings
    ```
4. Creamos un archivo que se llame `urls.py` en `<nombre_del_proyecto>/<nombre_de_su_aplicacion>/urls.py`. En mi caso sería: `MeetingRooms/bookings/urls.py`



## Uso

### Gestión de Usuarios

Los usuarios pueden registrarse en la aplicación y, una vez registrados, pueden crear salas y hacer reservas. 

### Gestión de Salas

- **Todas las Salas**: Muestra una lista de todas las salas creadas.
- **Crear Sala**: Permite crear una nueva sala proporcionando los detalles necesarios.
- **Buscar Sala**: Permite buscar salas existentes mediante distintos criterios de búsqueda.

### Gestión de Reservas

- **Todas las Reservas**: Muestra una lista de todas las reservas realizadas.
- **Crear Reserva**: Permite hacer una nueva reserva proporcionando los detalles necesarios.
- **Buscar Reserva**: Permite buscar reservas existentes mediante distintos criterios de búsqueda.

