from flask import Flask, render_template, redirect, url_for, request
import random
print("hello!")
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("hello?")
    return render_template("index.html")

@app.route("/konec")
def konec():
    return render_template("konec.html")

@app.route("/form")
def form():
    print("cau")
   
    name = request.args.get("name", "").strip()
    input_class = request.args.get("class", "").strip()
    age = request.args.get("age", "").strip()
    message = request.args.get("message", "").strip()

    print(name.lower())
    if name.lower() == "thuy":
        return redirect(url_for("konec"))


    if name and input_class and message:
        return redirect(url_for(
            "result",
            jinja_name=name,
            jinja_class=input_class,
            jinja_message=message
        ))

 
    return render_template("form.html")

@app.route("/result")
def result():
    name = request.args.get("jinja_name", default="____")
    input_class = request.args.get("jinja_class", default="____")
    message = request.args.get("jinja_message", default="____")
    random_number = random.randint(0, 10)

    return render_template(
        "result.html",
        jinja_name=name,
        jinja_class=input_class,
        jinja_message=message,
        number=random_number
    )

if __name__ == "__main__":
    app.run(debug=True)

