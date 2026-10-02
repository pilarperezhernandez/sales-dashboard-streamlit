# Sales dashboard in Streamlit

Final assignment for Data Visualisation, 2nd year of IMAT (ICAI – Universidad Pontificia Comillas), 2025-26. Individual project by Pilar Pérez Hernández.

*[Versión en español](README.es.md)*

Interactive dashboard built with Streamlit and Plotly on a retail sales dataset of about 350 MB (daily sales per store and product family, with promotions, transactions, store state and holiday information). The interface and the chart labels are in Spanish.

**Deployed on Streamlit Community Cloud:** https://practicafinalvisualizaciondatospilarperezhernadez-84tumpmskg3a.streamlit.app/ (also in `streamlit_url.txt`). The first load may take a while because the app has to download the data.


## Data

The dataset is split into two CSV files, `parte_1.csv` and `parte_2.csv`, hosted on Google Drive. They are not in the repository because of their size; `app.py` downloads them with `gdown` the first time it runs (the Drive file IDs are hardcoded in the script) and keeps them next to `app.py`, so later runs read the local copies. The two parts are concatenated and de-duplicated into a single DataFrame.

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

Python 3.10 or newer. The first start downloads the two CSVs from Google Drive (a few hundred MB), so it needs an internet connection and some patience; after that, as long as the files stay in the folder, the app starts straight from disk. The CSVs are ignored by git (`*.csv` in `.gitignore`).


## Files

```
.
├── app.py              The whole dashboard
├── requirements.txt    streamlit, pandas, plotly, pyarrow, gdown
├── streamlit_url.txt   Public URL of the deployed app
├── README.md           This file
└── README.es.md        Spanish version
```
