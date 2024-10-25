FROM python:3.11

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Copia el script de inicio
COPY start.sh /app/start.sh

# Hace que el script sea ejecutable
RUN chmod +x /app/start.sh

# Expone el puerto 8000
EXPOSE 8000

# Ejecuta el script de inicio
CMD ["/app/start.sh"]