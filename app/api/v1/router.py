# Standard library imports
# (No standard library imports needed)

# Third-party imports
from fastapi import APIRouter, HTTPException, Body, Depends

# Local application imports
from app.schemas.user import UserCreate
from app.services.user_service import (
    create_user,
    get_user_by_email,
    verify_user,
    delete_user,
    list_users
)
from app.services.utils_service import get_current_user
from app.core.mongo import db
from app.api.v1.endpoints.cvs import router as cvs_router
from app.api.v1.endpoints.auth import router as auth_router

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



@router.delete("/usuarios/{email}")
async def delete_user_endpoint(email: str, usuario_actual: str = Depends(get_current_user)):
    """
    Endpoint protegido para eliminar un usuario por su email.
    Requiere autenticación JWT válida en el header Authorization.
    Devuelve un error 404 si el usuario no existe.
    El parámetro usuario_actual contiene el email extraído del token.
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

router.include_router(auth_router)
router.include_router(cvs_router)