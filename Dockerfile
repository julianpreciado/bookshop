# Imagen base de Python
FROM python:3.11.0b1-bullseye

# Directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos
COPY ./requirements.txt ./

ENV PYTHONUNBUFFERED=1

# Instalar los requerimientos
RUN pip install -r requirements.txt

# Copiar el código fuente del proyecto
COPY ./ ./

# Puerto expuesto por Django
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
