ARCHIVO = 'informacion.txt'

def procesar_linea(linea):
    datos = linea.strip().split(';')
    if len(datos) == 4:
        nombre, apellido, direccion, correo = datos
        print(f"Nombre    : {nombre}")
        print(f"Apellido  : {apellido}")
        print(f"Dirección : {direccion}")
        print(f"Correo    : {correo}")
        print("-" * 40)
    else:
        print("Línea con formato inválido:", linea.strip())

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            next(archivo)  # Saltar cabecera
            for linea in archivo:
                procesar_linea(linea)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

if __name__ == '__main__':
    leer_archivo(ARCHIVO)