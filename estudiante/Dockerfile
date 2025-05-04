# Dockerfile del microservicio estudiante
FROM python:3.9-slim

# Instalar las dependencias necesarias (utilizando MariaDB en lugar de MySQL)
RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos
COPY . .

# Comando para iniciar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
