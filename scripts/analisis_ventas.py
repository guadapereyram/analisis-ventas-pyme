# Importación de la librería Pandas para análisis de datos
import pandas as pd
import matplotlib.pyplot as plt

# Carga del archivo CSV con información de ventas
dataframe = pd.read_csv("../datos/ventas.csv")

# Mostrar resumen de ventas
print("Resumen de ventas")
print(dataframe)

# Calcular total de ventas
total_sales = dataframe["ventas"].sum()

print(f"\nTotal de ventas: {total_sales}")

# Calcular promedio de ventas
average_sales = dataframe["ventas"].mean()

print(f"Promedio de ventas: {average_sales}")

# Identificar el producto con mayor cantidad de ventas
top_product = dataframe.loc[dataframe["ventas"].idxmax(), "producto"]
top_sales = dataframe["ventas"].max()

print(f"Producto más vendido: {top_product} ({top_sales} ventas)")

# Calcular ventas por categoría
sales_by_category = dataframe.groupby("categoria")["ventas"].sum()

print("\nVentas por categoría:")
print(sales_by_category)

print("\nVentas por categoría:")
print(sales_by_category)

# Generar gráfico de ventas por producto
plt.figure(figsize=(8, 5))
plt.bar(dataframe["producto"], dataframe["ventas"])
plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad de ventas")
plt.tight_layout()

# Guardar gráfico en la carpeta resultados
plt.savefig("../resultados/ventas_por_producto.png")

print("\nGráfico generado en: resultados/ventas_por_producto.png")
