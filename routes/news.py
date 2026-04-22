from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from services.groq_ai import analyze_news
from models import db
import json
from datetime import datetime

news_bp = Blueprint('news', __name__)

@news_bp.route('/news-analyzer')
@login_required
def index():
    return render_template('news/index.html')

@news_bp.route('/api/analyze-news', methods=['POST'])
@login_required
def api_analyze():
    data = request.get_json()
    text = data.get('text', '').strip()
    
    if not text:
        return jsonify({'success': False, 'error': 'News text required'})
    
    if len(text) < 20:
        return jsonify({'success': False, 'error': 'News too short — kam se kam 20 characters likho'})
    
    result = analyze_news(text)
    return jsonify({'success': True, 'result': result, 'text': text[:200]})