from flask import Flask, render_template, session, g

app = Flask(__name__)

JS_TESTING_MODE = False

@app.before_request
def add_tests():
    g.jasmine_tests = JS_TESTING_MODE


@app.route('/')
def index():
    return render_template('calc.html')


if __name__ == "__main__":
    import sys
    if sys.argv[-1] == "jstest":
        JS_TESTING_MODE = True
        
    app.run(host='0.0.0.0')
