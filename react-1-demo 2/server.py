from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_index():
    return """
        <div>
            <h3>React demo</h3>
            <div>
                <a href='/hello'>Hello component</a>
            </div>
            <div>
                <a href='/hello2'>Hello component w/ props</a>
            </div>
        </div>
    """

@app.route('/hello')
def show_hello():
    return render_template('hello.html')

@app.route('/hello2')
def show_hello2():
    return render_template('hello2.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
