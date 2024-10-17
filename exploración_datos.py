import pandas as pd

# Cargar los datos del archivo CSV
ruta_archivo = 'C:/Users/dulce/Downloads/retail_sales_dataset.csv'  # Asegúrate de que esta ruta sea correcta
datos = pd.read_csv(ruta_archivo)

# Mostrar los primeros datos para verificar la carga correcta
print(datos.head())

# Total de ventas por categoría de producto
ventas_por_categoria = datos.groupby('Product Category')['Total Amount'].sum()
print("Total de ventas por categoría de producto:")
print(ventas_por_categoria)

# Promedio de ventas diarias por categoría de producto
promedio_ventas_diarias = datos.groupby('Product Category')['Total Amount'].mean()
print("\nPromedio de ventas diarias por categoría de producto:")
print(promedio_ventas_diarias)

# Identificar la categoría con mayores y menores ventas
categoria_mayor_ventas = ventas_por_categoria.idxmax()
categoria_menor_ventas = ventas_por_categoria.idxmin()

print(f"\nCategoría con mayores ventas: {categoria_mayor_ventas}")
print(f"Categoría con menores ventas: {categoria_menor_ventas}")
# Filtrar datos para mostrar solo las ventas de una categoría específica
categoria_especifica = 'Electronics'  # Cambia esto a la categoría que deseas filtrar
datos_filtrados = datos[datos['Product Category'] == categoria_especifica]

# Mostrar los datos filtrados
print(f"\nDatos filtrados para la categoría '{categoria_especifica}':")
print(datos_filtrados)

# Suma de total de ventas
suma_total_ventas = datos_filtrados['Total Amount'].sum()
print(f"\nSuma total de ventas en la categoría '{categoria_especifica}': {suma_total_ventas}")

# Resta: Diferencia entre la venta máxima y mínima
diferencia_ventas = datos_filtrados['Total Amount'].max() - datos_filtrados['Total Amount'].min()
print(f"Diferencia entre la venta máxima y mínima en '{categoria_especifica}': {diferencia_ventas}")

# Multiplicación: Total de ventas con un aumento del 10%
total_con_aumento = suma_total_ventas * 1.1
print(f"Total de ventas con un aumento del 10%: {total_con_aumento}")

# División: Ventas promedio por producto
cantidad_ventas = datos_filtrados['Quantity'].sum()  # Total de unidades vendidas
ventas_por_producto = suma_total_ventas / cantidad_ventas if cantidad_ventas > 0 else 0
print(f"Ventas promedio por producto en '{categoria_especifica}': {ventas_por_producto}")