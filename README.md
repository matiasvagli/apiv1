# En estapa final  de construccion

# API Usuarios FastAPI + MongoDB

Esta API es un ejemplo profesional y didáctico para la gestión de usuarios y procesamiento de archivos CSV, ideal para casos de estudio, proyectos de aprendizaje o como base para sistemas más complejos.

## Características principales
- **Registro y login de usuarios** con validación y hash de contraseñas.
- **Roles de usuario** (`user` y `admin`) y protección de rutas según permisos.
- **Autenticación JWT** segura y centralizada.
- **Endpoints REST** para:
  - Crear usuario (solo admin)
  - Login y obtención de token
  - Consultar, listar y eliminar usuarios
  - Subir y procesar archivos CSV (con pandas)
- **Validaciones robustas** (campos requeridos, tamaño de archivos, formato CSV, etc).
- **Estructura profesional**: routers, servicios, esquemas y configuración separados.
- **Preparada para escalar**: fácil de agregar nuevas funcionalidades, endpoints o integraciones.

## Ideas para seguir aprendiendo
- Agregar paginación y filtros en el listado de usuarios
- Guardar los datos del CSV en la base de datos
- Implementar logs y auditoría
- Agregar tests automáticos (pytest)
- Mejorar la documentación OpenAPI
- Desplegar en la nube (Render, Railway, etc)

---

> Esta API es ideal como ejemplo de buenas prácticas en FastAPI, MongoDB y autenticación moderna. ¡Usala como base para tus propios proyectos o para practicas técnicas!
