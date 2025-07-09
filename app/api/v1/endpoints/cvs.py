
from fastapi import APIRouter, HTTPException, UploadFile,File
import pandas as pd
import io

router = APIRouter()

@router.post("/cvs/upload")
async def upload_cvs(file: UploadFile = File(...)):
    """
    Endpoint para subir un archivo CSV.
    El archivo debe ser un CSV con columnas 'nombre', 'email' y 'telefono'.
    Devuelve un mensaje de éxito o error.
    """
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="El archivo debe ser un CSV")
    contents = await file.read()
    size_mb = len(contents) / (1024 * 1024)  # Convertir a MB
    if size_mb > 5:  # Limitar el tamaño máximo a 5 MB
        raise HTTPException(status_code=400, detail="El archivo CSV no puede ser mayor a 5 MB")

    try:
        # Leer el archivo CSV usando pandas
        df = pd.read_csv(io.BytesIO(contents))
        
        # Validar que las columnas requeridas existen
        required_columns = ['nombre', 'email', 'telefono']
        if not all(col in df.columns for col in required_columns):
            raise HTTPException(status_code=400, detail="El CSV debe contener las columnas: nombre, email, telefono")
        
        # Procesar los datos (aquí podrías guardarlos en la base de datos)
        # Por simplicidad, solo retornamos el número de registros procesados
        return {"message": f"Archivo procesado correctamente con {len(df)} registros",
              "estadistics": {
                  "total_registros": len(df),
                  "columnas": list(df.columns),
                  "tamaño_mb": size_mb,
                  "primeros_registros": df.head().to_dict(orient='records'),
                    "ultimo_registro": df.tail(1).to_dict(orient='records')[0],
                    "columnas_nombres": df['nombre'].tolist(),
                    "columnas_emails": df['email'].tolist(),
                    "columnas_telefonos": df['telefono'].tolist()
              }
              }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {str(e)}")