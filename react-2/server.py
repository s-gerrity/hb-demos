from flask import Flask, render_template, jsonify
import time


app = Flask(__name__)


@app.route('/')
def index():
    """Display homepage."""

    return render_template('index.html')


@app.route('/clicker')
def demo_clicker():
    """Display click event demo."""

    return render_template('click.html')


@app.route('/dice')
def demo_dice():
    """Display dice demo."""

    return render_template('dice.html')


@app.route('/weather')
def demo_weather():
    """Display weather demo."""

    return render_template('weather.html')


@app.route('/state-with-ajax')
def demo_state_with_ajax():
    """Display demo of initializing state with AJAX."""

    return render_template('state-ajax.html')


@app.route('/api/weather')
def get_weather():
    """Return weather forecast."""

    return jsonify({'forecast': 'sunny'})


@app.route('/api/fruits')
def get_fruits():
    """Return a list of all melons."""

    time.sleep(2)  # Simulate a slow internet connection

    return jsonify([{'fruit_id': 1,
                     'name': 'apple'},
                    {'fruit_id': 2,
                     'name': 'berry'},
                    {'fruit_id': 3,
                     'name': 'cherry'}])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
