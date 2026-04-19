# Glenmark Stock Forecast using ARIMA

## Objective

Analyze and forecast stock prices of Glenmark using ARIMA.

## Dataset

* Source: Yahoo Finance (GLENMARK.NS)
* Duration: Last 1 year
* Feature used: Closing Price

## Methodology

1. Data preprocessing (handled missing values, selected closing price)
2. Visualization of stock trend and moving average
3. Stationarity check using ADF test
4. ACF & PACF plots for parameter selection
5. ARIMA(1,1,1) model applied
6. Forecasted next 30 days

## Results

* Model successfully generated future price predictions
* Forecast indicates a (upward/downward/stable) trend based on observed graph

## Conclusion

ARIMA is effective for short-term time series forecasting but has limitations in capturing sudden market changes.

## AI Ethics & Responsible Usage

* This project is for academic purposes only
* Predictions are not financial advice
* Model results may not reflect real-world market behavior
