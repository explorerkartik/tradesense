import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # App
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tradesense-secret-key-change-in-production'
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'

    # Database (Neon.tech PostgreSQL)
    DATABASE_URL = os.environ.get('DATABASE_URL', '')
    if DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
    }

    # Groq AI
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
    GROQ_MODEL = 'llama3-8b-8192'

    # Alpha Vantage (Stock prices)
    ALPHA_VANTAGE_API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY', '')

    # CoinGecko (Crypto - Free, no key needed)
    COINGECKO_BASE_URL = 'https://api.coingecko.com/api/v3'

    # Session
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    PERMANENT_SESSION_LIFETIME = 86400  # 1 day
