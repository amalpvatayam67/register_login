from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from itsdangerous import URLSafeTimedSerializer
import os

app = Flask(__name__)
app.secret_key = 'thisisasecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
s = URLSafeTimedSerializer(app.secret_key)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = bcrypt.generate_password_hash(
            request.form['password']).decode('utf-8')

        if User.query.filter_by(email=email).first():
            flash("Email already exists", "danger")
            return redirect(url_for('register'))

        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()

        # Simulated email verification
        token = s.dumps(email, salt='email-confirm')
        verify_url = url_for('verify_email', token=token, _external=True)
        print(f"🔗 Simulated email link (copy to browser): {verify_url}")
        os.makedirs("verification", exist_ok=True)
        path = os.path.join("verification", "verification_links.txt")
        with open(path, "a") as file:
            file.write(f"{email} → {verify_url}\n")

        flash("Registration successful! Check console for verification link.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/verify/<token>')
def verify_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
        user = User.query.filter_by(email=email).first()
        if user:
            user.is_verified = True
            db.session.commit()
            flash("Email verified successfully!", "success")
            return redirect(url_for('login'))
    except:
        flash("Verification link expired or invalid.", "danger")
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            if user.is_verified:
                session['user_id'] = user.id
                return redirect(url_for('dashboard'))
            else:
                flash("Please verify your email first.", "warning")
        else:
            flash("Invalid credentials", "danger")
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template('dashboard.html', email=user.email)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Logged out successfully.", "info")
    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
