# Dashboard de ventas en Streamlit

Práctica final de Visualización de Datos, 2º de IMAT (ICAI – Universidad Pontificia Comillas), curso 2025-26. Trabajo individual de Pilar Pérez Hernández.

*[English version](README.md)*

Dashboard interactivo construido con Streamlit y Plotly sobre un dataset de ventas de unos 350 MB (ventas diarias por tienda y familia de producto, con promociones, transacciones, estado de la tienda e información de festivos).

**Desplegado en Streamlit Community Cloud:** https://pilar-sales-dashboard.streamlit.app/ (también en `streamlit_url.txt`).


## Datos

El dataset original (ventas de tiendas tipo Favorita, unos 3 millones de filas) venía en dos CSV de 350 MB en total, `parte_1.csv` y `parte_2.csv`, alojados en Google Drive. Cargarlos enteros necesita unos 2,5 GB de RAM, más de lo que da Streamlit Community Cloud, así que la app lee ahora `data_ventas.parquet`: las mismas filas (concatenadas y sin duplicados) limitadas a las 12 columnas que usa el dashboard, con tipos categóricos y numéricos compactos. Ocupa 7 MB en disco y unos 80 MB en memoria, y se genera a partir de los dos CSV con `preparar_datos.py`. Si el Parquet no está, `app.py` descarga los CSV con `gdown` (los IDs de Drive están en el script).

Columnas que usa la app: `date`, `store_nbr`, `family` (familia de producto), `sales`, `onpromotion`, `transactions`, `state`, `holiday_type`, `year`, `month`, `week` y `day_of_week`. Al cargar se elimina la columna de índice `Unnamed: 0` si existe y las columnas numéricas se convierten con `pd.to_numeric`.


## Qué muestra el dashboard

La barra lateral solo lleva una guía breve; los selectores están dentro de cada pestaña.

**Pestaña 1 – Visión global.** KPIs (número de tiendas, familias de producto, estados y meses con datos), top 10 familias por ventas medias, histograma de ventas medias por tienda con P10 / mediana / P90, top 10 tiendas por ventas medias en promoción (`onpromotion > 0`) y gráficos de estacionalidad: ventas medias por día de la semana, por semana del año y por mes (promediando todos los años). Un desplegable muestra 50 filas de ejemplo. Se usan medias y no acumulados a propósito, para comparar el comportamiento típico.

**Pestaña 2 – Por tienda.** Un selector de `store_nbr` (por defecto, la tienda con más ventas totales) y, para esa tienda: ventas totales por año y comparación entre el número de familias vendidas y el número de familias que han estado alguna vez en promoción.

**Pestaña 3 – Por estado.** Un selector de `state` (por defecto, el estado con más ventas totales) y, para ese estado: transacciones totales por año, top 10 tiendas por ventas totales con su porcentaje sobre las ventas del estado, y top 10 familias de la tienda líder del estado, con el producto líder destacado como métrica.

**Pestaña 4 – Extra.** Un selector de año y un conjunto de vistas pensadas para dirección: ventas totales frente a ventas en promoción y porcentaje en promo, ventas mensuales con y sin promoción, peso mensual de las promociones, top 10 familias por peso de la promoción, uplift de la promoción por familia (venta media en promo / venta media sin promo − 1), venta media en festivos frente a no festivos con ranking por tipo de festivo, y un heatmap mes × día de la semana que se puede alternar entre media y total de ventas.

Las métricas van con separadores en formato español (`1.234,56`). La carga de datos y los agregados de la primera pestaña están cacheados con `st.cache_data`.


## Cómo ejecutarlo en local

```bash
pip install -r requirements.txt
streamlit run app.py
```

Python 3.10 o superior. La app arranca directamente desde `data_ventas.parquet`, sin descargas. Para regenerar el Parquet a partir de los CSV originales, coloca `parte_1.csv` y `parte_2.csv` junto al script y ejecuta `python preparar_datos.py` (los CSV están ignorados por git).


## Ficheros

```
.
├── app.py              Todo el dashboard
├── data_ventas.parquet Dataset compacto que lee la app (7 MB)
├── preparar_datos.py   Genera data_ventas.parquet a partir de los dos CSV originales
├── requirements.txt    streamlit, pandas, plotly, pyarrow, gdown
├── streamlit_url.txt   URL pública de la app desplegada
├── README.md           Versión en inglés
└── README.es.md        Este archivo
```
