import pandas as pd
import matplotlib.pyplot as plt
import os

# Definimos rutas relativas para que el proyecto pueda ejecutarse en Google Colab
# sin depender de rutas absolutas de una computadora específica.
ruta_datos = "datos/ventas.csv"
ruta_resultados = "resultados"

# Creamos la carpeta de resultados si todavía no existe.
os.makedirs(ruta_resultados, exist_ok=True)

# Cargamos el archivo CSV con los datos de ventas.
ventas = pd.read_csv(ruta_datos)

# Convertimos la columna de fecha a formato datetime.
# Esto permite agrupar correctamente las ventas por mes.
ventas["fecha_venta"] = pd.to_datetime(ventas["fecha_venta"])

# Calculamos el total de cada venta multiplicando cantidad por precio unitario.
ventas["total_venta"] = ventas["cantidad"] * ventas["precio_unitario"]

# Calculamos las ventas totales del período analizado.
ventas_totales = ventas["total_venta"].sum()

# Identificamos el producto más vendido según la cantidad total de unidades.
ventas_por_producto = ventas.groupby("producto")["cantidad"].sum()
producto_mas_vendido = ventas_por_producto.idxmax()
cantidad_producto_mas_vendido = ventas_por_producto.max()

# Agrupamos las ventas por mes para analizar la evolución temporal.
ventas["mes"] = ventas["fecha_venta"].dt.to_period("M")
ventas_por_mes = ventas.groupby("mes")["total_venta"].sum().reset_index()
ventas_por_mes["mes"] = ventas_por_mes["mes"].astype(str)

# Guardamos un resumen de indicadores en la carpeta resultados.
resumen = pd.DataFrame({
    "indicador": [
        "Ventas totales",
        "Producto más vendido",
        "Cantidad vendida del producto más vendido"
    ],
    "resultado": [
        ventas_totales,
        producto_mas_vendido,
        cantidad_producto_mas_vendido
    ]
})

resumen.to_csv(f"{ruta_resultados}/resumen_ventas.csv", index=False)

# Guardamos también las ventas mensuales en un CSV para facilitar la revisión.
ventas_por_mes.to_csv(f"{ruta_resultados}/ventas_por_mes.csv", index=False)

# Generamos un gráfico simple de evolución de ventas mensuales.
plt.figure(figsize=(8, 5))
plt.plot(ventas_por_mes["mes"], ventas_por_mes["total_venta"], marker="o")
plt.title("Evolución de ventas mensuales")
plt.xlabel("Mes")
plt.ylabel("Total de ventas")
plt.xticks(rotation=45)
plt.tight_layout()

# Guardamos el gráfico en la carpeta resultados.
plt.savefig(f"{ruta_resultados}/grafico_ventas_mensuales.png")

# Mostramos los resultados principales en pantalla.
print("ANÁLISIS DE VENTAS")
print("------------------")
print(f"Ventas totales: ${ventas_totales}")
print(f"Producto más vendido: {producto_mas_vendido}")
print(f"Cantidad vendida del producto más vendido: {cantidad_producto_mas_vendido}")
print("\nVentas por mes:")
print(ventas_por_mes)
