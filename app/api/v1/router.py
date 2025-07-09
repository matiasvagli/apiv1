# Standard library imports
# (No standard library imports needed)

# Third-party imports
from fastapi import APIRouter, HTTPException, Body

# Local application imports
from app.schemas.user import UserCreate
from app.services.user_service import (
    create_user,
    get_user_by_email,
    verify_user,
    delete_user,
    list_users
)
from app.core.mongo import db

router = APIRouter()

# Endpoint para crear un usuario
@router.post("/usuarios", status_code=201)
async def add_user(user: UserCreate):
    user_id = await create_user(user.nombre, user.email, user.password)
    return {"id": user_id, "nombre": user.nombre, "email": user.email}

@router.get("/usuarios/{email}")
async def get_user(email: str):
    user = await get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    user.pop("password", None)
    user["id"] = str(user["_id"])
    user.pop("_id", None)
    return user

@router.post("/usuarios/login")
async def login_user(email: str=Body(...), password: str=Body(...)):
    is_valid = await verify_user(email, password)
    if not is_valid:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"message": "Login exitoso"}

@router.delete("/usuarios/{email}")
async def delete_user(email: str):
    """
    Endpoint para eliminar un usuario por su email.
    Devuelve un error 404 si el usuario no existe.
    """
    result = await delete_user(email)
    return result

@router.get("/usuarios")
async def get_users():
    """
    Endpoint para listar todos los usuarios.
    Devuelve un error 404 si no hay usuarios.
    """
    return await list_users()