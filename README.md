# Sales dashboard in Streamlit

Final assignment for Data Visualisation, 2nd year of IMAT (ICAI – Universidad Pontificia Comillas), 2025-26. Individual project by Pilar Pérez Hernández.

*[Versión en español](README.es.md)*

Interactive dashboard built with Streamlit and Plotly on a retail sales dataset of about 350 MB (daily sales per store and product family, with promotions, transactions, store state and holiday information). The interface and the chart labels are in Spanish.

**Deployed on Streamlit Community Cloud:** https://pilar-sales-dashboard.streamlit.app/ (also in `streamlit_url.txt`).


## Data

The original dataset (Favorita-style store sales, about 3 million rows) came as two CSV files of 350 MB in total, `parte_1.csv` and `parte_2.csv`, hosted on Google Drive. Loading them whole needs about 2.5 GB of RAM, more than Streamlit Community Cloud provides, so the app now reads `data_ventas.parquet`: the same rows (concatenated and de-duplicated) restricted to the 12 columns the dashboard uses, with categorical and downcast numeric types. It weighs 7 MB on disk and about 80 MB in memory, and it is generated from the two CSVs by `preparar_datos.py`. If the Parquet file is missing, `app.py` falls back to downloading the CSVs with `gdown` (the Drive file IDs are in the script).

Columns the app relies on: `date`, `store_nbr`, `family` (product family), `sales`, `onpromotion`, `transactions`, `state`, `holiday_type`, `year`, `month`, `week` and `day_of_week`. A leftover `Unnamed: 0` index column is dropped on load and the numeric columns are coerced with `pd.to_numeric`.


## What the dashboard shows

The sidebar only holds a short guide; all the selectors live inside each tab.

**Tab 1 – Global view.** KPIs (number of stores, product families, states and months with data), top 10 product families by mean sales, histogram of mean sales per store with P10 / median / P90, top 10 stores by mean sales on promotion (`onpromotion > 0`), and seasonality charts: mean sales by day of week, by week of year and by month (averaged over all years). An expander shows a 50-row sample of the data. Means rather than totals are used on purpose, to compare typical behaviour.

**Tab 2 – Per store.** A `store_nbr` selector (defaulting to the store with the highest total sales) and, for that store: total sales per year and a comparison of the number of product families sold vs the number that were ever on promotion.

**Tab 3 – Per state.** A `state` selector (defaulting to the state with the highest total sales) and, for that state: total transactions per year, top 10 stores by total sales with their share of the state's sales, and the top 10 product families of the leading store in that state, with the leading product highlighted as a metric.

**Tab 4 – Extra.** A year selector and a set of management-oriented views for that year: total sales vs sales on promotion and the promotion share, monthly sales with and without promotion, monthly promotion share, top 10 families by promotion weight, promotion uplift per family (mean sales on promotion / mean sales off promotion − 1), mean sales on holidays vs non-holidays with a ranking by holiday type, and a month × day-of-week heatmap switchable between mean and total sales.

Metrics are formatted with Spanish separators (`1.234,56`). Aggregations for the first tab and the data loading are cached with `st.cache_data`.


## Running it locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Python 3.10 or newer. The app starts straight from `data_ventas.parquet`, so no download is needed. To rebuild the Parquet from the original CSVs, put `parte_1.csv` and `parte_2.csv` next to the script and run `python preparar_datos.py` (the CSVs are ignored by git).


## Files

```
.
├── app.py              The whole dashboard
├── data_ventas.parquet Compact dataset read by the app (7 MB)
├── preparar_datos.py   Builds data_ventas.parquet from the two original CSVs
├── requirements.txt    streamlit, pandas, plotly, pyarrow, gdown
├── streamlit_url.txt   Public URL of the deployed app
├── README.md           This file
└── README.es.md        Spanish version
```
