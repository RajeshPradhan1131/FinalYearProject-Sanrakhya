from app import app
from flask import render_template
from flask import request, jsonify

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hospital")
def hospital():
    return render_template("hospital.html")

@app.route("/bloodbank")
def bloodbank():
    return render_template("bloodbank.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/chatbot")
def chatbot_page():
    return render_template("chatbot.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_message = request.json.get("message", "").lower()

    if "hospital" in user_message:
        reply = "Nearest hospitals are being fetched 🏥..."
    elif "blood" in user_message:
        reply = "Checking blood bank availability 🩸..."
    elif "bed" in user_message:
        reply = "Looking for available beds and ICU..."
    else:
        reply = "Sorry, I didn’t understand. Try asking about hospitals, blood, or beds."

    return jsonify({"reply": reply})

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")