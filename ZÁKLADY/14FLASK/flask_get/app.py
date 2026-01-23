from flask import Flask, render_template, redirect, url_for, request
import random

# Vytvoření flaskové aplikace
app = Flask(__name__)

# @ je dekorátor, který upravuje funkce
# v případě flasku řeší routování - připojování se na specifickou cestu/stránku
@app.route("/")
def hello_world():
    return render_template("index.html") # render_template vrátí stránku index.html ze složky templates



@app.route("/form")
def form():
    # requests.args.get("něco") se používá pro metodu GET
    # text v .get() odpovídá attributu name="" (jménu) v html
    name = request.args.get("name")
    input_class = request.args.get("class")
    age = request.args.get("age")
    message = request.args.get("message")
    print(name, input_class, age)


    if name and input_class and message:
        return redirect(url_for("result", jinja_name=name, jinja_class=input_class, jinja_message=message))

    return render_template("form.html")

@app.route("/result")
def result():
    name = request.args.get("jinja_name", default="____")
    input_class = request.args.get("jinja_class", default="____")
    message = request.args.get("jinja_message", default="____")
    random_number = random.randint(0, 10)

    return render_template("result.html", jinja_name=name, jinja_class=input_class, jinja_message=message, number=random_number)

if __name__ == "__main__":
    app.run(debug=True)