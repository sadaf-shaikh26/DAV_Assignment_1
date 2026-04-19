import matplotlib
matplotlib.use('TkAgg')

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

print("Downloading data...")

# 1. Download data
data = yf.download("GLENMARK.NS", period="1y")
data = data[['Close']].dropna()

print("Download complete")

# -------------------------------
# 📊 GRAPH 1: Closing Price
# -------------------------------
plt.figure(figsize=(10,5))
plt.plot(data['Close'], label="Closing Price")
plt.title("Glenmark Closing Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.show()

# -------------------------------
# 📊 GRAPH 2: Moving Average
# -------------------------------
data['MA20'] = data['Close'].rolling(window=20).mean()

plt.figure(figsize=(10,5))
plt.plot(data['Close'], label="Close")
plt.plot(data['MA20'], label="20-Day Moving Avg")
plt.title("Moving Average (Trend View)")
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.show()

# -------------------------------
# 📊 ADF TEST
# -------------------------------
result = adfuller(data['Close'])

print("\nADF Test Result:")
print("ADF Statistic:", result[0])
print("p-value:", result[1])

# -------------------------------
# 📊 GRAPH 3: ACF
# -------------------------------
plot_acf(data['Close'])
plt.title("ACF Plot")
plt.show()

# -------------------------------
# 📊 GRAPH 4: PACF
# -------------------------------
plot_pacf(data['Close'])
plt.title("PACF Plot")
plt.show()

# -------------------------------
# 📊 ARIMA MODEL
# -------------------------------
model = ARIMA(data['Close'], order=(1,1,1))
model_fit = model.fit()

print(model_fit.summary())

# -------------------------------
# 📊 FORECAST
# -------------------------------
forecast = model_fit.forecast(steps=30)

# Fix dates
future_dates = pd.date_range(start=data.index[-1], periods=31, freq='B')[1:]
forecast.index = future_dates

# -------------------------------
# 📊 GRAPH 5: FINAL FORECAST
# -------------------------------
plt.figure(figsize=(10,5))
plt.plot(data['Close'], label="Past")
plt.plot(forecast, label="Forecast")

plt.title("Glenmark Stock Forecast (Next 30 Days)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.xticks(rotation=45)

plt.show()