# Utilizar una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de tu proyecto al contenedor
COPY . /app/

# Instalar las dependencias desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que correrá la aplicación (por defecto FastAPI corre en el puerto 8000)
EXPOSE 8000

# Comando para ejecutar la aplicación (Uvicorn como servidor ASGI)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
