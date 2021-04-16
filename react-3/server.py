from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sharkwords-final")
def sharkwords():
    return render_template("sharkwords-final.html")


@app.route("/more")
def more_demos():
    return render_template("more-demos-index.html")


@app.route("/more/sharkwords-advanced")
def sharkwords_advanced():
    return render_template("sharkwords-advanced.html")


@app.route("/more/sharkwords-hooks")
def sharkwords_hooks():
    return render_template("sharkwords-hooks.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
