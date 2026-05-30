# Análisis de Ventas de una Pequeña Empresa

## Descripción del proyecto

Este proyecto corresponde al trabajo práctico desarrollado bajo la modalidad de célula ágil de tres integrantes.

El escenario elegido es el Escenario B: Análisis de Ventas de una Pequeña Empresa.

El objetivo del proyecto es analizar un conjunto de datos simulados de ventas comerciales para obtener indicadores básicos que permitan interpretar el desempeño de la empresa.

## Integrantes y roles

- Hugo: Líder y Organizador. Responsable de crear el repositorio, definir la estructura inicial y redactar la documentación general.
- Paco: Desarrollador Técnico. Responsable de desarrollar el script de análisis estadístico.
- Luis: Revisor y QA. Responsable de revisar el código, mejorar la documentación, controlar la seguridad y gestionar el Pull Request final.

## Estructura del repositorio

analisis-ventas-pequena-empresa/

├── datos/
│   └── ventas.csv

├── scripts/
│   └── analisis_ventas.py

├── resultados/
│   ├── resumen_ventas.csv
│   ├── ventas_por_mes.csv
│   └── grafico_ventas_mensuales.png

├── README.md

└── .gitignore

## Dataset utilizado

El dataset utilizado es un archivo CSV simulado llamado ventas.csv, ubicado en la carpeta datos.

Contiene las siguientes columnas:

- id
- fecha_venta
- producto
- cantidad
- precio_unitario

## Indicadores calculados

El script permite calcular:

- Ventas totales.
- Producto más vendido.
- Cantidad vendida del producto más vendido.
- Ventas agrupadas por mes.
- Gráfico de evolución mensual de ventas.

## Instrucciones de ejecución

1. Clonar el repositorio:

git clone https://github.com/TU_USUARIO/analisis-ventas-pequena-empresa.git

2. Ingresar a la carpeta del proyecto:

cd analisis-ventas-pequena-empresa

3. Ejecutar el script:

python scripts/analisis_ventas.py

## Resultados

Los resultados se guardan automáticamente en la carpeta resultados.

Archivos generados:

- resumen_ventas.csv
- ventas_por_mes.csv
- grafico_ventas_mensuales.png

## Seguridad

El proyecto incluye un archivo .gitignore para evitar subir archivos temporales o innecesarios.

El Personal Access Token de GitHub no debe escribirse dentro del código ni subirse al repositorio.

## Trazabilidad con Jira

Cada commit realizado en el repositorio debe comenzar con el ID del Issue de Jira correspondiente.

Ejemplos:

PROY-1: Crear estructura inicial del repositorio  
PROY-2: Desarrollar script de análisis de ventas  
PROY-3: Actualizar documentación y revisión final
