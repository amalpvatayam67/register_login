
# 🔐 Flask Login, Registration, and Email Verification System

A secure user authentication project built using **Flask**, **SQLite**, and **Bootstrap 5**.  
This project supports:

- ✅ User Registration with Email Verification (simulated via console + file)
- 🔐 Secure Login with Password Hashing (Flask-Bcrypt)
- 🚪 Logout functionality
- 📥 SQLite Database (auto-created)
- ✉️ Verification links saved to `verification/verification_links.txt`
- 🎨 Styled UI using Bootstrap

---

## 📁 Project Structure

```
register_login/
├── app.py
├── instance/
│   └── database.db            # Auto-generated SQLite DB
├── myenv/                     # Virtual environment (optional)
├── templates/
│   ├── layout.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── verify.html
├── verification/
│   └── verification_links.txt # Stores simulated verification links
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd register_login
```

### 2. (Optional) Create and Activate Virtual Environment

```bash
python3 -m venv myenv
source myenv/bin/activate     # Windows: myenv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install flask flask-sqlalchemy flask-bcrypt itsdangerous
```

---

## 🚀 Running the App

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 💡 Features

- Passwords hashed using **bcrypt**
- Email verification using secure token (`itsdangerous`)
- Flash messages with categories (`success`, `danger`, etc.)
- Auto-generates `database.db` if deleted
- Clean Bootstrap-styled UI
- Verification links saved locally for dev/testing

---

## 📧 Example Verification Link Output

```
🔗 Simulated email link (copy to browser): http://127.0.0.1:5000/verify/<token>
```

Also saved in:

```
verification/verification_links.txt
```

---

## 📃 License

This project is free to use for learning and educational purposes.
