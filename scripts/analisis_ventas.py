# Importación de la librería Pandas para análisis de datos
import pandas as pd

# Diccionario con información de ventas simuladas
sales_data = {
    "product": ["Notebook", "Mouse", "Teclado"],
    "sales": [15, 40, 25]
}

# Creación del DataFrame
dataframe = pd.DataFrame(sales_data)

# Mostrar resumen de ventas
print("Resumen de ventas")
print(dataframe)

# Calcular total de ventas
total_sales = dataframe["sales"].sum()

print(f"\nTotal de ventas: {total_sales}")
