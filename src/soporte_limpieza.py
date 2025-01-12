import pandas as pd
import googletrans
from googletrans import Translator
import os

# Inicializar el traductor
translator = Translator()

def traducir_columnas_y_guardar(archivo_csv, ruta_salida, separador=';', encoding='latin1'):
    """
    Traduce las columnas de un archivo CSV de portugués a español y guarda un nuevo archivo CSV.
    
    Parámetros:
    - archivo_csv: Ruta del archivo CSV de entrada.
    - ruta_salida: Ruta donde se guardará el archivo CSV traducido.
    - separador: Delimitador usado en el archivo CSV (por defecto ';').
    - encoding: Codificación del archivo CSV (por defecto 'latin1').
    """
    try:
        # Cargar la base de datos
        df = pd.read_csv(archivo_csv, sep=separador, encoding=encoding)
        
        # Traducir las columnas
        columnas_traducidas = [translator.translate(col, src='pt', dest='es').text for col in df.columns]
        df.columns = columnas_traducidas
        
        # Guardar el nuevo archivo
        os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)  # Crear directorio si no existe
        df.to_csv(ruta_salida, sep=';', index=False, encoding='utf-8-sig')
        
        print(f"Archivo traducido y guardado en: {ruta_salida}")
        return df
    
    except Exception as e:
        print(f"Error al traducir o guardar el archivo {archivo_csv}: {e}")
        return None