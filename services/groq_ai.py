import os
import requests

GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def analyze_news(text):
    if not GROQ_API_KEY:
        return mock_analysis(text)
    
    prompt = f"""You are a financial news analyzer. Analyze the following news and determine:
1. Is it REAL, FAKE, or MANIPULATED?
2. Sentiment: BULLISH, BEARISH, or NEUTRAL
3. Credibility score: 0-100
4. Brief explanation (2-3 lines)
5. Impact on market: HIGH, MEDIUM, or LOW

News: {text}

Respond in this exact JSON format:
{{
    "verdict": "REAL/FAKE/MANIPULATED",
    "sentiment": "BULLISH/BEARISH/NEUTRAL", 
    "credibility": 85,
    "explanation": "Your explanation here",
    "impact": "HIGH/MEDIUM/LOW",
    "key_points": ["point1", "point2", "point3"]
}}"""

    try:
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3,
            "max_tokens": 500
        }
        response = requests.post(GROQ_API_URL, json=payload, headers=headers, timeout=30)
        if response.status_code == 200:
            data = response.json()
            content = data['choices'][0]['message']['content']
            import json
            start = content.find('{')
            end = content.rfind('}') + 1
            if start != -1 and end != 0:
                return json.loads(content[start:end])
    except Exception as e:
        print(f"Groq error: {e}")
    
    return mock_analysis(text)

def mock_analysis(text):
    return {
        "verdict": "REAL",
        "sentiment": "NEUTRAL",
        "credibility": 70,
        "explanation": "API key set karo .env mein for real AI analysis.",
        "impact": "MEDIUM",
        "key_points": ["News analyzed", "Set GROQ_API_KEY for better results", "Mock data shown"]
    }

def get_trading_signal(symbol, asset_type="crypto"):
    if not GROQ_API_KEY:
        return mock_signal(symbol)
    
    prompt = f"""You are an expert trading analyst. Give a trading signal for {symbol} ({asset_type}).
Based on general market knowledge, provide:

Respond in this exact JSON format only:
{{
    "signal": "BUY/SELL/HOLD",
    "confidence": 75,
    "reason": "Brief reason in 2 lines",
    "target_price_change": "+5.2%",
    "risk_level": "LOW/MEDIUM/HIGH",
    "timeframe": "Short-term/Medium-term/Long-term"
}}"""

    try:
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.4,
            "max_tokens": 300
        }
        response = requests.post(GROQ_API_URL, json=payload, headers=headers, timeout=30)
        if response.status_code == 200:
            data = response.json()
            content = data['choices'][0]['message']['content']
            import json
            start = content.find('{')
            end = content.rfind('}') + 1
            if start != -1 and end != 0:
                return json.loads(content[start:end])
    except Exception as e:
        print(f"Groq signal error: {e}")
    
    return mock_signal(symbol)

def mock_signal(symbol):
    return {
        "signal": "HOLD",
        "confidence": 60,
        "reason": "Set GROQ_API_KEY for real AI signals.",
        "target_price_change": "0%",
        "risk_level": "MEDIUM",
        "timeframe": "Short-term"
    }