from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from models import db
from models.portfolio import Portfolio

portfolio_bp = Blueprint('portfolio', __name__)

@portfolio_bp.route('/portfolio')
@login_required
def index():
    return render_template('portfolio/index.html')

@portfolio_bp.route('/api/portfolio', methods=['GET'])
@login_required
def api_get():
    items = Portfolio.query.filter_by(user_id=current_user.id).all()
    return jsonify({'success': True, 'data': [i.to_dict() for i in items]})

@portfolio_bp.route('/api/portfolio', methods=['POST'])
@login_required
def api_add():
    data = request.get_json()
    symbol = data.get('symbol', '').strip().upper()
    name = data.get('name', '').strip()
    asset_type = data.get('asset_type', 'crypto')
    quantity = float(data.get('quantity', 0))
    buy_price = float(data.get('buy_price', 0))
    currency = data.get('currency', 'INR')
    notes = data.get('notes', '')

    if not symbol or not name or quantity <= 0 or buy_price <= 0:
        return jsonify({'success': False, 'error': 'Sab fields sahi se bharo!'})

    item = Portfolio(
        user_id=current_user.id,
        symbol=symbol,
        name=name,
        asset_type=asset_type,
        quantity=quantity,
        buy_price=buy_price,
        current_price=buy_price,
        currency=currency,
        notes=notes
    )
    db.session.add(item)
    db.session.commit()
    return jsonify({'success': True, 'data': item.to_dict()})

@portfolio_bp.route('/api/portfolio/<int:item_id>', methods=['DELETE'])
@login_required
def api_delete(item_id):
    item = Portfolio.query.filter_by(id=item_id, user_id=current_user.id).first()
    if not item:
        return jsonify({'success': False, 'error': 'Item nahi mila!'})
    db.session.delete(item)
    db.session.commit()
    return jsonify({'success': True})