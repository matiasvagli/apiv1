"""
Este archivo define el endpoint de autenticación (login) y la lógica para generar y validar JWT.
Se recomienda instalar 'python-jose' para el manejo de JWT:
    pip install python-jose[cryptography]
"""
from fastapi import APIRouter, HTTPException, Body
from jose import jwt
from datetime import datetime, timedelta
import os
from app.services.user_service import verify_user
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

# Configuración del JWT
# SECRET_KEY = os.getenv("JWT_SECRET", "supersecretkey")  # Cambia esto en producción
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Duración del token

router = APIRouter()

@router.post("/usuarios/login")
async def login_user(email: str = Body(...), password: str = Body(...)):
    """
    Endpoint de login. Si las credenciales son válidas, genera y devuelve un JWT.
    El token debe ser enviado luego en el header Authorization: Bearer <token> para acceder a rutas protegidas.
    """
    is_valid = await verify_user(email, password)
    if not is_valid:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    # Datos a incluir en el token (puedes agregar más info si quieres)
    to_encode = {
        "sub": email,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

# Puedes agregar aquí dependencias para proteger rutas usando el token
# Ejemplo:
# from fastapi import Depends, Request
# from jose import JWTError
# def get_current_user(request: Request):
#     ...
