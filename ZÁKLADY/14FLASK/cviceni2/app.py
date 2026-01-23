from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
tophesla = ["123456","	admin", "12345678","password"]

# Připojení do SQLite databáze
def get_db():
    conn = sqlite3.connect("users.db")
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("konec")
def konec():
    return render_template("konec.html")


# přihlášení
@app.route("/login", methods=["GET"])
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    for i from tophesla:
        if i == tphesla

    if len(password) > 10:
        return redirect("/success")
    else:
        return redirect("/busted")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/busted")
def busted():
    return render_template("busted.html")

if __name__ == "__main__":
    app.run(debug=True)
