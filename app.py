from flask import Flask
from flask_login import LoginManager
from config import Config
from models import db
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.market import market_bp
from routes.signals import signals_bp
from routes.news import news_bp
from routes.portfolio import portfolio_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please login to access this page.'
    login_manager.login_message_category = 'info'

    from models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(market_bp)
    app.register_blueprint(signals_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(portfolio_bp)

    # Create all tables
    with app.app_context():
        db.create_all()
        print("✅ Database tables created successfully!")

    return app

app = create_app()

@app.route('/ping')
def ping():
    return 'pong', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
