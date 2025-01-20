import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

def fetch_data(ticker, period='10y'):
    """Fetch historical stock data."""
    if ticker:
        try:
            data = yf.download(ticker, period=period)
            if data.empty:
                st.error("No data found. Please check the ticker symbol and try again.")
                return None
            return data
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return None
    return None

def sarima_forecast(close_prices):
    """Fit SARIMA model and forecast future values."""
    if close_prices is not None:
        order = (1, 1, 1)
        seasonal_order = (1, 1, 1, 12)
        sarima_model = SARIMAX(close_prices, order=order, seasonal_order=seasonal_order, enforce_stationarity=False, enforce_invertibility=False)
        sarima_results = sarima_model.fit(disp=False)
        forecast_steps = 365
        forecast = sarima_results.get_forecast(steps=forecast_steps)
        forecasted_prices = forecast.predicted_mean
        forecast_ci = forecast.conf_int()
        last_price = close_prices.iloc[-1]
        price_diff = forecasted_prices - last_price
        percentage_change = (price_diff / last_price) * 100
        return forecasted_prices, forecast_ci, price_diff, percentage_change
    return None, None, None, None

def plot_forecast(forecasted_prices, forecast_ci, last_date):
    """Plot the forecasted prices with confidence intervals."""
    if forecasted_prices is not None:
        future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=len(forecasted_prices), freq='D')
        plt.figure(figsize=(10, 5))
        plt.plot(future_dates, forecasted_prices, label='Forecasted Prices', color='blue')
        plt.fill_between(future_dates, forecast_ci.iloc[:, 0], forecast_ci.iloc[:, 1], color='gray', alpha=0.3, label='Confidence Interval')
        plt.title('Forecasted Prices and Confidence Intervals')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        st.pyplot(plt)

st.title('Stock Forecasting App')

ticker_symbol = st.text_input("Enter a stock ticker symbol (e.g., 'AAPL', 'GOOGL'):")

if ticker_symbol:
    data = fetch_data(ticker_symbol)
    if data is not None:
        last_date = data.index[-1]
        close_prices = data['Close']
        forecasted_prices, forecast_ci, price_diff, percentage_change = sarima_forecast(close_prices)
        if forecasted_prices is not None:
            plot_forecast(forecasted_prices, forecast_ci, last_date)

            forecast_data = pd.DataFrame({
                'Date': pd.date_range(start=last_date + pd.Timedelta(days=1), periods=len(forecasted_prices)),
                'Forecasted Prices': forecasted_prices,
                'Price Difference': price_diff.round(2),
                'Percentage Change': percentage_change.round(2)
            }).set_index('Date')

            st.write("Forecasted Prices (Next 365 Days):")
            st.dataframe(forecast_data)

            investment_price = st.number_input("Enter your planned investment amount in USD:", min_value=0.0, step=100.0)
            if investment_price > 0:
                current_price = close_prices.iloc[-1]
                forecasted_price_next_year = forecasted_prices.iloc[-1]
                investment_value_next_year = (forecasted_price_next_year / current_price) * investment_price

                st.write(f"Current stock price: ${current_price:.2f}")
                st.write(f"Forecasted stock price after one year: ${forecasted_price_next_year:.2f}")
                st.write(f"Your investment value after one year: ${investment_value_next_year:.2f}")
