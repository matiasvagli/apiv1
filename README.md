# API Usuarios FastAPI + MongoDB

Esta API es un ejemplo profesional y didáctico para la gestión de usuarios y procesamiento de archivos CSV, ideal para casos de estudio, proyectos de aprendizaje o como base para sistemas más complejos.

## Características principales
- **Registro y login de usuarios** con validación y hash de contraseñas usando Passlib.
- **Roles de usuario** (`user` y `admin`) y protección de rutas según permisos con dependencias personalizadas.
- **Autenticación JWT** segura y centralizada con python-jose.
- **Endpoints REST** para:
  - Crear usuario (solo admin)
  - Login y obtención de token
  - Consultar, listar y eliminar usuarios
  - Subir y procesar archivos CSV (con pandas)
- **Procesamiento de archivos CSV**: la API permite subir archivos CSV y los depura/acondiciona usando pandas, devolviendo estadísticas y datos limpios para análisis o carga en base de datos.
- **Validaciones robustas** (campos requeridos, tamaño de archivos, formato CSV, etc).
- **Estructura profesional**: routers, servicios, esquemas y configuración separados.
- **Preparada para escalar**: fácil de agregar nuevas funcionalidades, endpoints o integraciones.

## Tecnologías y librerías utilizadas
- **FastAPI**: framework principal para la API.
- **MongoDB + Motor**: base de datos NoSQL y driver asíncrono.
- **Pandas**: procesamiento y análisis de archivos CSV.
- **Passlib**: hash seguro de contraseñas.
- **python-jose**: generación y validación de tokens JWT.
- **Pydantic**: validación de datos y esquemas.
- **Uvicorn**: servidor ASGI para desarrollo y producción.

## Ejemplo de usuario para pruebas
- **Email:** admin@gmail.com
- **Password:** admin
- **Rol:** admin

Puedes usar este usuario para loguearte y probar los endpoints protegidos por rol admin.

## Ejemplo de login (request)
```json
POST /api/v1/usuarios/login
{
  "email": "admin@gmail.com",
  "password": "admin"
}
```

## Ejemplo para crear usuario (solo admin)
```json
POST /api/v1/usuarios
{
  "nombre": "Juan",
  "email": "juan@email.com",
  "password": "1234",
  "role": "user"
}
```

## Ejemplo para subir un CSV
Usá la ruta `/api/v1/cvs/upload` y subí un archivo con las columnas `nombre`, `email`, `telefono`.

## Rutas principales para explorar
- `POST /api/v1/usuarios` (crear usuario, solo admin)
- `POST /api/v1/usuarios/login` (login y obtención de token)
- `GET /api/v1/usuarios/{email}` (consultar usuario)
- `GET /api/v1/usuarios` (listar usuarios)
- `DELETE /api/v1/usuarios/{email}` (eliminar usuario, solo admin)
- `POST /api/v1/cvs/upload` (subir y procesar CSV)

## Ideas para seguir aprendiendo
- Agregar paginación y filtros en el listado de usuarios
- Guardar los datos del CSV en la base de datos
- Implementar logs y auditoría
- Agregar tests automáticos (pytest)
- Mejorar la documentación OpenAPI
- Desplegar en la nube (Render, Railway, etc)

---

> Esta API es ideal como ejemplo de buenas prácticas en FastAPI, MongoDB y autenticación moderna. ¡Usala como base para tus propios proyectos o para practicar!

# Si tenes alguna duda no dudes en contactarme valgimatias@gmail.com


