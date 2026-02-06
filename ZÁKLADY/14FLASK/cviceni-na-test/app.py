from flask import Flask, render_template, request, json
app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/manual")
def manual():

    return render_template("manual.html")


@app.route("/contact")
def result():
    name = request.args.get("jinja_name", default="____")
    message = request.args.get("jinja_message", default="____")
    
    if name and message:

        data = {
            "email": name,
            "message": message
        }
     




        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)



    return render_template("contact.html", jinja_name=name, jinja_message=message)



if __name__ == "__main__":
    app.run(debug=True)
