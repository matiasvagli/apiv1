# Importa BaseModel y EmailStr de Pydantic para validación de datos
from pydantic import BaseModel, EmailStr, field_validator
from typing import Annotated , Literal
from pydantic import StringConstraints

# Esquema para la creación de usuarios, usado para validar los datos de entrada en la API
class UserCreate(BaseModel):
    nombre: str  # El nombre del usuario, debe ser string
    email: EmailStr  # El email del usuario, validado como email
    password: Annotated[str, StringConstraints(min_length=4, max_length=6)]  # Password entre 4 y 6 caracteres
    role: Literal["user", "admin"] = "user"  # Rol del usuario, por defecto es "user"
    @field_validator("nombre")
    def validate_nombre(cls, value):
        """
        Valida que el nombre no esté vacío.
        Si está vacío, lanza un ValueError con un mensaje descriptivo.
        """
        if not value or not value.strip():
            raise ValueError("El nombre no puede estar vacío")
        
        return value

    @field_validator("password")
    def validate_password(cls, value):
        """
        Valida que el password no esté vacío.
        Si está vacío, lanza un ValueError con un mensaje descriptivo.
        """
        if not value or not value.strip():
            raise ValueError("El password no puede estar vacío")
        
        return value