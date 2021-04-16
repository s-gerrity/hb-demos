from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension
from flask import _request_ctx_stack


app = Flask(__name__)

# In order to use the debug toolbar, we need to have a secret key -- this
# is the same secret key we need for Flask session, anyway.
app.secret_key = 'something-random-here'


@app.route('/')
def index():
    """Show order form."""

    return render_template('order_form.html')


@app.route('/process-order', methods=['POST'])
def process_order():
    """Process order.

    Calculate the price and, if applicable, announce that they get
    free shipping.
    """

    melon_type = request.form.melon_type
    qty = request.form['quantity']

    total = qty * 2

    if qty > 5:
        free_shipping = True
    else:
        free_shipping = False
        shipping_cost = qty * 0.75
        total += shipping_cost

    return render_template('order_confirm.html',
                           melon_type=melon_type,
                           qty=qty,
                           price=total,
                           free_shipping=free_shipping)


if __name__ == '__main__':

    # We need to set up app.debug to True before we use the toolbar
    app.debug = True

    # DebugToolbarExtension(app)

    # Flask's debugger only works when threaded=False. It's a config
    # value that *should* default to False but on some environments, it
    # defaults to True.
    app.run(host='0.0.0.0', threaded=False)
