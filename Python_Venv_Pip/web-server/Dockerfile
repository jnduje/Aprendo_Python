# Desde que version de Python va a correr este contenedor que estoy creando
FROM python:3.8 

# Creo una carpeta (espacio de trabajo) dentro del contenedor
WORKDIR /app

# Copio los requerimientos de módulos desde el archivo requirements.txt LOCAL al requirements.txt del CONTENEDOR
COPY requirements.txt /app/requirements.txt

# Corro pip (detecta solo la versión de python3) para instalar las dependencias que nombra el archivo requirements.txt
# ubicad dentro de la carpeta app del contenedor. 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copio todos los archivos de mi aplicación al contenedor
COPY . app/

# Lanzo el servidor de uivcorn 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]

# Crear el contenedor -> docker-compose build
# Lanzar el contenedor -> docker-compose up -d
# Para ver el estado del contenedor -> docker-compose ps
# Para entrar en el contenedor -> docker-compose exec <nombre_del_servicio> bash 
#  

# Luego correr el archivo de interes de la misma manera que siempre: python3 main.py

# Para bajar cerrar el contenedor -> docker-compose down
# Para salir del contenedor -> exit