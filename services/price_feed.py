import requests
import os

ALPHA_VANTAGE_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY', '')

def get_crypto_prices():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            'vs_currency': 'usd',
            'ids': 'bitcoin,ethereum,binancecoin,ripple,cardano,solana,dogecoin,polkadot',
            'order': 'market_cap_desc',
            'per_page': 8,
            'page': 1,
            'sparkline': False,
            'price_change_percentage': '24h'
        }
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            result = []
            for coin in data:
                result.append({
                    'symbol': coin['symbol'].upper(),
                    'name': coin['name'],
                    'price': coin['current_price'],
                    'change_24h': round(coin.get('price_change_percentage_24h', 0) or 0, 2),
                    'market_cap': coin['market_cap'],
                    'volume': coin['total_volume'],
                    'image': coin['image'],
                    'type': 'crypto'
                })
            return result
    except Exception as e:
        print(f"CoinGecko error: {e}")
    return get_mock_crypto()

def get_mock_crypto():
    return [
        {'symbol': 'BTC', 'name': 'Bitcoin', 'price': 67000, 'change_24h': 2.5, 'market_cap': 1300000000000, 'volume': 28000000000, 'image': '', 'type': 'crypto'},
        {'symbol': 'ETH', 'name': 'Ethereum', 'price': 3500, 'change_24h': 1.8, 'market_cap': 420000000000, 'volume': 15000000000, 'image': '', 'type': 'crypto'},
        {'symbol': 'BNB', 'name': 'BNB', 'price': 580, 'change_24h': -0.5, 'market_cap': 85000000000, 'volume': 1800000000, 'image': '', 'type': 'crypto'},
        {'symbol': 'SOL', 'name': 'Solana', 'price': 180, 'change_24h': 3.2, 'market_cap': 78000000000, 'volume': 3200000000, 'image': '', 'type': 'crypto'},
    ]

def get_forex_rates():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            rates = data.get('rates', {})
            return [
                {'symbol': 'USD/INR', 'name': 'US Dollar', 'price': round(rates.get('INR', 83.5), 2), 'change_24h': 0.1, 'type': 'forex'},
                {'symbol': 'EUR/INR', 'name': 'Euro', 'price': round(rates.get('INR', 83.5) / rates.get('EUR', 0.92), 2), 'change_24h': -0.2, 'type': 'forex'},
                {'symbol': 'GBP/INR', 'name': 'British Pound', 'price': round(rates.get('INR', 83.5) / rates.get('GBP', 0.79), 2), 'change_24h': 0.3, 'type': 'forex'},
                {'symbol': 'JPY/INR', 'name': 'Japanese Yen', 'price': round(rates.get('INR', 83.5) / rates.get('JPY', 149.5), 4), 'change_24h': -0.1, 'type': 'forex'},
            ]
    except Exception as e:
        print(f"Forex error: {e}")
    return [
        {'symbol': 'USD/INR', 'name': 'US Dollar', 'price': 83.45, 'change_24h': 0.1, 'type': 'forex'},
        {'symbol': 'EUR/INR', 'name': 'Euro', 'price': 90.23, 'change_24h': -0.2, 'type': 'forex'},
        {'symbol': 'GBP/INR', 'name': 'British Pound', 'price': 105.67, 'change_24h': 0.3, 'type': 'forex'},
    ]

def get_indian_stocks():
    return [
        {'symbol': 'RELIANCE', 'name': 'Reliance Industries', 'price': 2945.50, 'change_24h': 1.2, 'type': 'stock', 'exchange': 'NSE'},
        {'symbol': 'TCS', 'name': 'Tata Consultancy Services', 'price': 3812.30, 'change_24h': 0.8, 'type': 'stock', 'exchange': 'NSE'},
        {'symbol': 'HDFCBANK', 'name': 'HDFC Bank', 'price': 1678.90, 'change_24h': -0.4, 'type': 'stock', 'exchange': 'NSE'},
        {'symbol': 'INFY', 'name': 'Infosys', 'price': 1845.20, 'change_24h': 2.1, 'type': 'stock', 'exchange': 'NSE'},
        {'symbol': 'WIPRO', 'name': 'Wipro', 'price': 478.65, 'change_24h': -1.3, 'type': 'stock', 'exchange': 'NSE'},
        {'symbol': 'TATAMOTORS', 'name': 'Tata Motors', 'price': 924.40, 'change_24h': 3.5, 'type': 'stock', 'exchange': 'NSE'},
        {'symbol': 'BAJFINANCE', 'name': 'Bajaj Finance', 'price': 7234.80, 'change_24h': 0.6, 'type': 'stock', 'exchange': 'NSE'},
        {'symbol': 'ADANIENT', 'name': 'Adani Enterprises', 'price': 2456.30, 'change_24h': -2.1, 'type': 'stock', 'exchange': 'NSE'},
    ]