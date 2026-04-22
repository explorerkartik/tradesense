from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from services.groq_ai import get_trading_signal

signals_bp = Blueprint('signals', __name__)

@signals_bp.route('/signals')
@login_required
def index():
    return render_template('signals/index.html')

@signals_bp.route('/api/signal', methods=['POST'])
@login_required
def api_signal():
    data = request.get_json()
    symbol = data.get('symbol', '').strip().upper()
    asset_type = data.get('asset_type', 'crypto')

    if not symbol:
        return jsonify({'success': False, 'error': 'Symbol required'})

    result = get_trading_signal(symbol, asset_type)
    return jsonify({'success': True, 'result': result, 'symbol': symbol})