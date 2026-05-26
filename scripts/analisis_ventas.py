# Importación de la librería Pandas para análisis de datos
import pandas as pd

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
