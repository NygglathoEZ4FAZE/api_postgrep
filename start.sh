#!/bin/sh

# Ejecutar migraciones
python3 manage.py migrate

# Iniciar el servidor con Gunicorn
exec gunicorn --bind 0.0.0.0:8000 proyecto_postgrepsql.wsgi:application
