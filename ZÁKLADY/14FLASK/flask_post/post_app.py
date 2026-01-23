from flask import Flask, render_template, redirect, url_for, request, g
import random
import sqlite3

# Vytvoření flaskové aplikace
app = Flask(__name__)

# uloží cestu k databázi pod proměnnou (konstantu) DATABASE
DATABASE = "instance/database.db"

def get_db():
    # g je flaskový objekt global, do kterého ukládáme spojení s datbází
    db = getattr(g, "_database", None)

    # pokud neexistuje spojení s databází, vytvoř jej, pokud existuje, vrať jej
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# spuštění databáze (nebo její vytvoření, pokud neexistuje)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource("schema.sql", mode="r") as file:
            db.cursor().executescript(file.read())
        db.commit()

# funkce která automaticky spustí a ukončí připojení k databázi, když je potřeba
@app.teardown_appcontext
def close_connection(exception):
    db = get_db()
    if db is not None:
        db.close()


# @ je dekorátor, který upravuje funkce
# v případě flasku řeší routování - připojování se na specifickou cestu/stránku
@app.route("/")
def hello_world():
    return render_template("index.html") # render_template vrátí stránku index.html ze složky templates

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # .args je pro GET, .form je pro POST
        name = request.form.get("name")
        input_class = request.form.get("class")
        age = request.form.get("age")
        message = request.form.get("message")
        print(name, input_class, age)

        cursor = get_db().cursor()
        cursor.execute(
            f"INSERT INTO students (student_name, class, age, student_message) VALUES (?, ?, ?, ?)",
            (name, input_class, age, message)
        )
        get_db().commit()

    return render_template("form_post.html")

@app.route("/result")
def result():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    return render_template("result.html", rows=rows)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)