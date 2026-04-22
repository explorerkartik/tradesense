from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.user import User
from models.portfolio import Portfolio
from models.watchlist import Watchlist
