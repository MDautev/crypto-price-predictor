````markdown
# 🪙 Crypto Price Predictor

A simple web app that displays historical prices for selected cryptocurrencies over the past 30 days and predicts their prices for the next 7 days using basic linear regression.

## 🔍 Features

- Fetches real-time price data from the CoinGecko API
- Visualizes 30 days of historical price data
- Predicts prices for the next 7 days using linear regression
- Supports multiple cryptocurrencies:
  - Bitcoin
  - Ethereum
  - Solana
  - Dogecoin
- Interactive chart using Chart.js
- Built with Python (Flask), JavaScript, HTML/CSS

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/crypto-price-predictor.git
cd crypto-price-predictor
```
````

### 2. Install Dependencies

Make sure you have Python 3 installed.

```bash
pip install flask scikit-learn numpy requests
```

### 3. Run the App

```bash
python app.py
```

### 4. Open in Browser

Visit:

```cpp
http://127.0.0.1:5000
```

### 🧠 How It Works

The app uses the CoinGecko API to retrieve the last 30 days of price data.
It feeds that data into a basic Linear Regression model from scikit-learn.
The model then predicts prices for the next 7 days, assuming a linear trend.
Results are visualized using Chart.js, with two datasets:
Real prices
Predicted prices (dashed line)

⚠️ This prediction model is extremely simple and does not account for market volatility or trends. It is meant for educational and demonstration purposes only.

### 📁 Project Structure

├── app.py # Flask backend
├── templates/
│ └── index.html # Frontend interface
├── static/  
└── README.md

🧑‍💻 Author
Created by MDautev
Inspired by the desire to build a simple, educational crypto prediction app.

```

```
