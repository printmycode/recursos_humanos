# recursos_humanos
App para ver y filtrar una base de datos de empleados

## Instalación

1. Clona este repositorio en tu máquina local usando la siguiente URL de GitHub:
   git clone https://github.com/printmycode/recursos_humanos.git

2. Accede a la carpeta del proyecto:
   cd recursos_humanos

3. Instala las dependencias necesarias:
   pip install -r requirements.txt

4. Ejecuta las migraciones de la base de datos:
   python manage.py migrate

5. Crea un superusuario para acceder al panel de administración:
   python manage.py createsuperuser

6. Inicia el servidor de desarrollo:
   python manage.py runserver

7. Abre tu navegador web y accede a la siguiente URL:
   http://127.0.0.1:8000/

## Uso

Una vez que hayas seguido los pasos de instalación, puedes acceder al proyecto y utilizar las siguientes funcionalidades:

- Registro de empleados: Permite agregar información sobre los empleados, incluyendo su nombre, cargo y género.
- Filtro de empleados: Puedes filtrar los empleados por su ID, cargo y género.
- Inicio de sesión: Si tienes un usuario creado, puedes iniciar sesión para acceder a las funcionalidades de administración.
- Cierre de sesión: Si deseas cerrar sesión, puedes hacerlo haciendo clic en el botón "Logout".

## Contribuciones

Las contribuciones a este proyecto son bienvenidas. Si encuentras algún error, tienes sugerencias de mejora o deseas agregar nuevas funcionalidades, puedes abrir un "issue" o enviar un "pull request" en [GitHub](https://github.com/printmycode/recursos_humanos).

## Licencia

Este proyecto está bajo la licencia MIT. Puedes ver más detalles en el archivo [LICENSE](https://github.com/printmycode/recursos_humanos/blob/main/LICENSE).

---
¡Gracias por visitar este proyecto! Si tienes alguna pregunta o necesitas ayuda adicional, no dudes en contactarme. ¡Espero que este proyecto te sea útil y te ayude en tus desarrollos!
