from flask import Flask, request, render_template
from flask import session, flash, make_response, redirect

app = Flask(__name__)

# Flask uses a secret key to encrypt cookies used to connect
# the browser to the session--so if you want to use sessions,
# you have to have a secret key. If the public learns this
# value, they can forge session information--so for sites with
# security concerns, make sure this isn't checked into a
# public place like GitHub
app.secret_key = '4534gdghjk5d#$RGR^HDG'


@app.route('/')
def index():
    """Homepage."""

    return render_template('index.html')


################################################################
# Routes for the cookies demo

@app.route('/form-cookie')
def show_cookies_form():
    """Show form that prompts for favorite color."""

    return render_template('form-cookie.html')


@app.route('/handle-form-cookie')
def set_cookie():
    """Return form response; include cookie for browser."""

    fav_color = request.args['fav_color']

    html = render_template('response-cookie.html')
    resp = make_response(html)

    resp.set_cookie('fav_color', fav_color)

    return resp


@app.route('/later-cookie')
def get_cookie():
    """An example page that can use that cookie."""

    fav_color = request.cookies['fav_color']

    return render_template('later-cookie.html',
                           fav_color=fav_color)


################################################################
# Routes that demonstrate sessions


@app.route('/form-session')
def show_session_form():
    """Show form that prompts for nickname and lucky number."""

    return render_template('form-session.html')


@app.route('/session-basics/set')
def set_session():
    """Set value for session['fav_number']."""

    session['fav_number'] = 64

    return render_template('basic-set-session.html')


@app.route('/session-basics/get')
def get_session():
    """Get values out of the session."""

    fav_num = session['fav_number']

    return render_template('basic-get-session.html',
                           fav_num=fav_num)


@app.route('/handle-form-session')
def handle_session_form():
    """Return agreeable response and save to session."""

    session['nickname'] = request.args['nickname']
    session['fav_number'] = request.args['fav_number']

    return render_template('response-session.html')


################################################################
# Routes that demonstrate flashing


@app.route('/flash-demo')
def show_flash_messages():
    """An example for setting and retrieving flashed messages."""

    flash('I am a flash message.')
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
