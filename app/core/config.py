# app/core/config.py

# Este archivo centraliza la configuración global de la aplicación,
# especialmente variables sensibles y parámetros que pueden cambiar
# según el entorno (desarrollo, testing, producción).

import os

# Clave secreta para firmar y verificar los JWT.
# Es recomendable definir la variable de entorno JWT_SECRET en producción.
SECRET_KEY = os.getenv("JWT_SECRET", "supersecretkey")  # ¡Cambia esto en producción!

# Algoritmo utilizado para firmar los JWT.
ALGORITHM = "HS256"

# Tiempo de expiración del token de acceso (en minutos).
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1 hora