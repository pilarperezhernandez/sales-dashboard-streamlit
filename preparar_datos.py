# preparar_datos.py
# Genera data_ventas.parquet a partir de los dos CSV originales (parte_1.csv y parte_2.csv).
# Solo conserva las columnas que usa app.py y usa tipos compactos para que el dashboard
# quepa en la memoria de Streamlit Community Cloud (de ~2 GB a ~80 MB en memoria).

import pandas as pd

COLUMNAS = [
    "date", "store_nbr", "family", "sales", "onpromotion", "holiday_type",
    "state", "transactions", "year", "month", "week", "day_of_week",
]

partes = [pd.read_csv(f, low_memory=False) for f in ("parte_1.csv", "parte_2.csv")]
df = pd.concat(partes, ignore_index=True).drop_duplicates()
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

df = df[COLUMNAS].copy()
df["date"] = pd.to_datetime(df["date"], errors="coerce")
for col in ["family", "holiday_type", "state", "day_of_week"]:
    df[col] = df[col].astype("category")
for col in ["store_nbr", "onpromotion", "year", "month", "week"]:
    df[col] = pd.to_numeric(df[col], errors="coerce", downcast="integer")
df["sales"] = pd.to_numeric(df["sales"], errors="coerce").astype("float32")
df["transactions"] = pd.to_numeric(df["transactions"], errors="coerce").astype("float32")

df.to_parquet("data_ventas.parquet", index=False, compression="zstd")
print(f"{len(df)} filas guardadas en data_ventas.parquet")
