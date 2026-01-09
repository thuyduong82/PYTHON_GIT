from flask import Flask, render_template, redirect, url_for, request




app = Flask(__name__) #vytvoření flask aplikace

@app.route("/")#@ je dekorátor funkce která upracuje jinou funkci, / je route
def indexhtml():
    return render_template("index.html") #render tempate vrati stránku index.html 

@app.route("/form")
def form():
    #request.args.get("něco") se používá u metody GET
    #text v .get()odpovida atributu name="" v html
    name = request.args.get("name")
    input_class = request.args.get("class")
    age = request.args.get("age")
    message = request.args.get("message")
    print(name, input_class, age)

    if name and input_class and message:
        return redirect(url_for("results", jinja_name=name, jinja_class=input_class, jinja_message=message))# jinja je prvni
    return render_template("form.html")

@app.route("/results")
def results():
    name = request.args.get("name", default="____")
    input_class = request.args.get("input_class", default="____")
    message = request.args.get("message", default="____")

    return render_template("results.html", jinja_name=name, jinja_class=input_class, jinja_message=message)

if __name__== "__main__":
    app.run(debug = True)