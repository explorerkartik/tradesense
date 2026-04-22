from app import create_app
from models import db

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Sab tables ban gaye!")
    print("   - users")
    print("   - portfolios")
    print("   - watchlists")
    print("\n🚀 Database ready hai!")