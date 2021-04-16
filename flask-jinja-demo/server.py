from flask import Flask, request, render_template
from random import choice, sample


COMPLIMENTS = ["smart", "clever", "tenacious", "awesome", "Pythonic"]

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""

    return render_template("index.html")


@app.route('/hello')
def say_hello():
    """Simple greet for user."""

    return render_template("hello.html")


# @app.route('/greet')
# def offer_greeting():
#     """Give player compliments."""

#     player = request.args.get("person")
#     nice_thing = choice(COMPLIMENTS)
#     return render_template("compliment.html", name=player, compliment=nice_thing)


@app.route('/greet')
def greet_person():
    """Give player compliments."""

    player = request.args.get("person")
    wants_compliments = request.args.get("wants_compliments")

    # COMPLIMENTS = ["smart", "clever", "tenacious", "awesome", "Pythonic"]

    if wants_compliments:
        nice_things = sample(COMPLIMENTS, 3)
    else:
        nice_things = []
    return render_template("compliments.html",
                           compliments=nice_things, name=player)


@app.route('/base')
def base():
    """Show base template."""

    # NOTE: you do NOT normally need to make a route to show the base template ---
    # this is here just so in lecture we can show you how the base template renders
    # by itself!

    return render_template("base.html")


@app.route('/inherit')
def inheritance():
    """Show example of page that uses base template."""

    return render_template("mypage.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
