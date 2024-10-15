import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

cryptolist = ["ETH,SOL,XRP"]

crypto1 = "BTC"
crypto2 = "SOL"

raw1 = pd.read_csv(f"{crypto1}EUR.csv", parse_dates=True).convert_dtypes()
raw2 = pd.read_csv(f"{crypto2}EUR.csv", parse_dates=True).convert_dtypes()

if len(raw1) < len(raw2):
    raw2 = raw2.drop(range(0,len(raw2)-len(raw1)))
else:
    if len(raw1) > len(raw2):
        raw1 = raw1.drop(range(0, len(raw1) - len(raw2)))

close1 = raw1.loc[:, "Close"]
close2 = raw2.loc[:, "Close"]

plt.plot(close1, close2, "o")

x = close1.to_numpy().reshape((-1, 1))
y = close2.to_numpy()