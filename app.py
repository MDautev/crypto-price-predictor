from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# Основен рут
@app.route('/')
def index():
    return render_template('index.html')


# Рут за получаване на данни за криптовалути
from flask import request

@app.route('/api/get_crypto_data')
def get_crypto_data():
    coin = request.args.get('coin', 'bitcoin')  # по подразбиране е bitcoin
    url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart'
    params = {'vs_currency': 'usd', 'days': '30'}
    response = requests.get(url, params=params)
    data = response.json()
    return jsonify(data)



from sklearn.linear_model import LinearRegression
import numpy as np

@app.route('/api/predict')
def predict_price():
    coin = request.args.get('coin', 'bitcoin')
    url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart'
    params = {'vs_currency': 'usd', 'days': '30'}
    response = requests.get(url, params=params)
    data = response.json()

    prices = data['prices']
    X = np.arange(len(prices)).reshape(-1, 1)
    y = np.array([price[1] for price in prices])

    model = LinearRegression()
    model.fit(X, y)

    future_days = 7
    X_future = np.arange(len(prices), len(prices) + future_days).reshape(-1, 1)
    predicted_prices = model.predict(X_future)

    return jsonify({
        "predicted_prices": predicted_prices.tolist()
    })





if __name__ == '__main__':
    app.run(debug=True)