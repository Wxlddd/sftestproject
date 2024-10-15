import pandas as pd
from pathlib import Path

# I dati sono stati ottenuti da Binance, maggior exchange di Crypto (?)

data_folder = Path("rawdata")
filepath = data_folder / "Binance_BTCEUR_d.csv"
df = pd.read_csv("rawdata/Binance_BTCEUR_d.csv")
print(df.head())
