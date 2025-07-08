# Importaciones necesarias
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Para manejar CORS (Cross-Origin Resource Sharing)

# Crear la aplicación FastAPI principal
app = FastAPI(
    title="FastAPI CVs",  # Título que aparece en la documentación automática (/docs)
    description="API para procesamiento y gestión de CVs",  # Descripción en la documentación
    version="1.0.0"  # Versión de la API
)

# Configurar CORS - permite que navegadores web accedan a la API desde otros dominios
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen. En producción usar dominios específicos: ["https://miapp.com"]
    allow_credentials=True,  # Permite enviar cookies y headers de autenticación
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los headers HTTP
)

# Ruta principal de la API - endpoint de bienvenida
@app.get("/")
def read_root():
    """
    Endpoint principal que devuelve información básica de la API
    Accesible en: http://localhost:8000/
    """
    return {
        "message": "API de CVs funcionando correctamente",
        "version": "1.0.0",
        "docs": "/docs"  # Indica dónde encontrar la documentación
    }

# Ruta de salud del sistema - útil para monitoreo
@app.get("/health")
def health_check():
    """
    Endpoint para verificar que la API está funcionando
    Útil para sistemas de monitoreo y balanceadores de carga
    Accesible en: http://localhost:8000/health
    """
    return {"status": "healthy", "service": "fastapi-cvs"}

# Configuración para ejecutar la aplicación directamente
if __name__ == "__main__":
    import uvicorn
    # Ejecutar el servidor uvicorn con configuración de desarrollo
    uvicorn.run(
        app,  # La aplicación FastAPI
        host="0.0.0.0",  # Acepta conexiones desde cualquier IP
        port=8000,  # Puerto donde corre la API
        reload=True  # Reinicia automáticamente cuando se cambia el código
    )
