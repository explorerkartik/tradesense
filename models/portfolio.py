from models import db
from datetime import datetime

class Portfolio(db.Model):
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    symbol = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    asset_type = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Float, nullable=False, default=0)
    buy_price = db.Column(db.Float, nullable=False, default=0)
    current_price = db.Column(db.Float, default=0)
    currency = db.Column(db.String(10), default='INR')
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @property
    def total_invested(self):
        return self.quantity * self.buy_price

    @property
    def current_value(self):
        return self.quantity * self.current_price

    @property
    def profit_loss(self):
        return self.current_value - self.total_invested

    @property
    def profit_loss_percent(self):
        if self.total_invested == 0:
            return 0
        return ((self.current_value - self.total_invested) / self.total_invested) * 100

    def to_dict(self):
        return {
            'id': self.id,
            'symbol': self.symbol,
            'name': self.name,
            'asset_type': self.asset_type,
            'quantity': self.quantity,
            'buy_price': self.buy_price,
            'current_price': self.current_price,
            'currency': self.currency,
            'total_invested': self.total_invested,
            'current_value': self.current_value,
            'profit_loss': self.profit_loss,
            'profit_loss_percent': self.profit_loss_percent,
            'created_at': self.created_at.strftime('%Y-%m-%d')
        }