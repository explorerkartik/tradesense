from flask import Blueprint, render_template, jsonify
from flask_login import login_required
from services.price_feed import get_crypto_prices, get_forex_rates, get_indian_stocks

market_bp = Blueprint('market', __name__)

@market_bp.route('/markets')
@login_required
def index():
    return render_template('markets/index.html')

@market_bp.route('/api/prices/crypto')
@login_required
def api_crypto():
    data = get_crypto_prices()
    return jsonify({'success': True, 'data': data})

@market_bp.route('/api/prices/stocks')
@login_required
def api_stocks():
    data = get_indian_stocks()
    return jsonify({'success': True, 'data': data})

@market_bp.route('/api/prices/forex')
@login_required
def api_forex():
    data = get_forex_rates()
    return jsonify({'success': True, 'data': data})

@market_bp.route('/api/prices/all')
@login_required
def api_all():
    crypto = get_crypto_prices()[:4]
    stocks = get_indian_stocks()[:4]
    forex = get_forex_rates()[:3]
    return jsonify({
        'success': True,
        'crypto': crypto,
        'stocks': stocks,
        'forex': forex
    })