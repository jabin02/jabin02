# Use a base image with Python
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY stock_forecasting_app.py /app/

# Install dependencies
RUN pip install --no-cache-dir streamlit yfinance pandas matplotlib statsmodels

# Expose the Streamlit default port
EXPOSE 8501


# Run the Streamlit app
CMD ["streamlit", "run", "stock-investment.py", "--server.port=8501", "--server.enableCORS=false"]

