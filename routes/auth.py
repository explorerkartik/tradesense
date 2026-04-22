from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from models import db
from models.user import User, bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        if not username or not email or not password:
            flash('Sab fields fill karo!', 'danger')
            return render_template('auth/register.html')
        if len(username) < 3:
            flash('Username kam se kam 3 characters ka hona chahiye!', 'danger')
            return render_template('auth/register.html')
        if len(password) < 6:
            flash('Password kam se kam 6 characters ka hona chahiye!', 'danger')
            return render_template('auth/register.html')
        if password != confirm_password:
            flash('Passwords match nahi kar rahe!', 'danger')
            return render_template('auth/register.html')
        if User.query.filter_by(username=username).first():
            flash('Yeh username pehle se liya hua hai!', 'danger')
            return render_template('auth/register.html')
        if User.query.filter_by(email=email).first():
            flash('Yeh email pehle se registered hai!', 'danger')
            return render_template('auth/register.html')
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Account ban gaya! Ab login karo.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        remember = request.form.get('remember', False)
        if not email or not password:
            flash('Email aur password dono chahiye!', 'danger')
            return render_template('auth/login.html')
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            flash('Email ya password galat hai!', 'danger')
            return render_template('auth/login.html')
        login_user(user, remember=bool(remember))
        flash(f'Welcome back, {user.username}!', 'success')
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('dashboard.index'))
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logout ho gaye!', 'info')
    return redirect(url_for('auth.login'))