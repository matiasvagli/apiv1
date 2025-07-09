# Importa el cliente asíncrono de MongoDB (Motor)
from motor.motor_asyncio import AsyncIOMotorClient
# Para leer variables de entorno del sistema
import os

# URI de conexión a MongoDB, configurable por variable de entorno
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
# Nombre de la base de datos, configurable por variable de entorno
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "fastapi")

# Crea el cliente de MongoDB usando la URI
client = AsyncIOMotorClient(MONGODB_URI)
# Obtiene la base de datos a usar
db = client[MONGO_DB_NAME]
