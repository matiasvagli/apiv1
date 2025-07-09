# Importa la conexión a la base de datos MongoDB
from app.core.mongo import db
from fastapi import HTTPException
from starlette import status
from passlib.context import CryptContext
from app.services.utils_service import verify_password

# Crea un contexto de encriptación para los passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user_by_email(email: str):
    """
    Función asíncrona para obtener un usuario por su email.
    Busca en la colección 'usuarios' y devuelve el primer usuario encontrado.
    Si no se encuentra, devuelve None.
    """
    user = await db.usuarios.find_one({"email": email})
    return user


# Función asíncrona para crear un usuario en la base de datos
async def create_user(nombre: str, email: str, password: str):
    # Espera el resultado de la búsqueda de usuario por email
    if await get_user_by_email(email):
        # Si el usuario ya existe, lanza una excepción HTTP 400 (Bad Request)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario ya existe")
    # Hashea el password antes de guardarlo
    hashed_password = pwd_context.hash(password)
    # Si el usuario no existe, procede a crearlo
    user = {"nombre": nombre, "email": email, "password": hashed_password}
    result = await db.usuarios.insert_one(user)
    return str(result.inserted_id)


# Función para verificar las credenciales de un usuario
async def verify_user(email: str, password: str):
    user = await get_user_by_email(email)
    if not user:
        return False
    return verify_password(password, user["password"])  

#Funcion para eliminar un usuario por su email
async def delete_user(email: str):
    """
    Función asíncrona para eliminar un usuario por su email.
    Busca en la colección 'usuarios' y elimina el primer usuario encontrado.
    Si no se encuentra, lanza una excepción HTTP 404 (Not Found).
    """
    result = await db.usuarios.delete_one({"email": email})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return {"detail": "Usuario eliminado exitosamente"}

#Lista de usuarios
async def list_users():
    """
    Función asíncrona para listar todos los usuarios.
    Devuelve una lista de diccionarios con los datos de cada usuario.
    """
    users = []
    async for user in db.usuarios.find():
        
        user_data = {
            "id": str(user["_id"]),
            "nombre": user["nombre"],
            "email": user["email"]
        }
        users.append(user_data)
    if len(users) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron usuarios")
    # Si hay usuarios, devuelve la lista
    return users
