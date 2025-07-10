from passlib.context import CryptContext
from fastapi import Depends,Request, HTTPException
from jose import jwt
from jose import JWTError
from app.core.config import SECRET_KEY, ALGORITHM


# Contexto para el hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si la contraseña en texto plano coincide con la contraseña hasheada.
    
    :param plain_password: Contraseña en texto plano proporcionada por el usuario.
    :param hashed_password: Contraseña hasheada almacenada en la base de datos.
    :return: True si las contraseñas coinciden, False en caso contrario.
    """
    return pwd_context.verify(plain_password, hashed_password)  


def get_current_user(request: Request):
    """
    Extrae y valida el usuario actual a partir del token JWT en el header Authorization.
    Mejoras:
    - Soporta el formato estándar 'Bearer <token>'
    - Devuelve error si el header no está presente o tiene formato incorrecto
    - Devuelve error si el token es inválido o expirado
    - Puede usarse como dependencia en rutas protegidas
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Token no proporcionado o formato incorrecto"
        )
    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload # Devuelve el payload completo, puedes acceder a payload["sub"] para el email
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido o expirado"
        )
    
#Definimios los permisos de acceso
def Admin_access(payload: dict = Depends(get_current_user)):
    """
    Verifica si el usuario tiene permisos de administrador.
    Si no es admin, lanza una excepción HTTP 403 (Forbidden).
    """
    if payload.get("role") != "admin":
        raise HTTPException(
            status_code=403,
            detail="Acceso denegado. Se requieren permisos de administrador."
        )
    return payload

def User_access(payload: dict = Depends(get_current_user)):
    """
    Verifica si el usuario tiene permisos de usuario.
    Si no es usuario, lanza una excepción HTTP 403 (Forbidden).
    """
    if payload.get("role") not in ["user", "admin"]:  # Permite tanto usuarios normales como administradores
        raise HTTPException(
            status_code=403,
            detail="Acceso denegado. Se requieren permisos de usuario."
        )
    return payload