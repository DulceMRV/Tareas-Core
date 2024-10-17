import numpy as np

# Función para cargar los datos del archivo CSV
def cargar_datos(ruta_archivo):
    # Cargar los datos del archivo CSV utilizando NumPy
    datos = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1, dtype=float)
    return datos

if __name__ == "__main__":
    # Ruta del archivo CSV (asegúrate de que esta ruta apunte al archivo correcto)
    ruta_archivo = 'C:/Users/dulce/Downloads/retail_sales_dataset.csv'  # Cambia el nombre del archivo
    
    # Cargar los datos
    datos = cargar_datos(ruta_archivo)
    
    # Mostrar los primeros datos cargados para verificar
    print(datos[:5])  # Muestra las primeras 5 filas
    