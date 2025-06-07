# 1) Parto de la imagen oficial de Python 3.12 (slim)
FROM python:3.12-slim

# 2) Establezco /app como directorio de trabajo
WORKDIR /app

# 3) Copio sólo requirements.txt (para usar cache en Docker)
COPY requirements.txt .

# 4) Instalo las dependencias
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 5) Copio el código fuente y los tests al contenedor
COPY src/ ./src/
COPY templates/ ./templates/
COPY tests/ ./tests/

# 5.1) Agrego PYTHONPATH para que Python encuentre el paquete "src"
ENV PYTHONPATH=/app

# 6) Variables de entorno para Flask
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# 7) Expongo el puerto 5000 para la app de Flask
EXPOSE 5000

# 8) Comando por defecto: arranco el servidor de Flask
CMD ["flask", "run"]
