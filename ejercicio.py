import os
import argparse
import re

STOP_WORDS = {
    # Pronombres personales
    'yo', 'tú', 'él', 'ella', 'ello', 'nosotros', 'vosotros', 'ellos', 'ellas', 'usted', 'ustedes',
    'me', 'te', 'se', 'nos', 'os', 'le', 'les', 'lo', 'la', 'los', 'las',
    
    # Artículos
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas',
    
    # Preposiciones
    'a', 'ante', 'bajo', 'con', 'contra', 'de', 'desde', 'en', 'entre', 'hacia', 'hasta', 
    'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras',
    
    # Conjunciones
    'y', 'o', 'u', 'pero', 'mas', 'aunque', 'sino', 'porque', 'si', 'como', 'que',
    
    # Adverbios comunes
    'no', 'sí', 'también', 'ya', 'así', 'bien', 'aquí', 'ahí', 'allí', 'cómo', 'cuándo', 
    'dónde', 'muy', 'poco', 'mucho', 'tan', 'casi', 'solo', 'solamente',
    
    # Contracciones
    'al', 'del'
}

def quitar_caracteresEspeciales(texto):
     return re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑ@\s]', ' ', texto)

def procesar_archivos_en_directorio(directorio):
    # lsitar todos los archivos en el directorio para recorrerlos uno a uno
    for nombre_archivo in os.listdir(directorio):
        # Construyo la ruta completa al archivo (relativa)
        ruta_archivo = os.path.join(directorio, nombre_archivo)
        
        # Verificar si es un archivo (y no subcarpeta)
        if os.path.isfile(ruta_archivo):
            print(f"\nProcesando archivo: {nombre_archivo}")
            
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                    # Leer línea por línea
                    for num_linea, linea in enumerate(archivo, 1):
                       # linea = linea.strip()  # Eliminar espacios y saltos de línea
                        linea_limpia = quitar_caracteresEspeciales(linea.strip()) #quito caracteres especiales y los reemplazo con espacios 
                        linea_normalizada = linea_limpia.lower() #paso a minusculas todas las palabras
                        palabras = [palabra for palabra in linea_normalizada.split() 
                                  if palabra not in STOP_WORDS]  # Filtra stop words
                        print("Palabras limpias:", palabras)
            except UnicodeDecodeError:
                print(f"Error, no se pudo leer {nombre_archivo} como texto.")
            except Exception as e:
                print(f"Error inesperado al procesar {nombre_archivo}: {e}")



# bloque ejecutado al correr directamente este script
# se pide el directorio donde esten los archivos y ese path se parsea 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directorio", help="Ruta del directorio con los archivos txt a procesar")
    args = parser.parse_args()
    procesar_archivos_en_directorio(args.directorio)