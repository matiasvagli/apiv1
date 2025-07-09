from passlib.context import CryptContext

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