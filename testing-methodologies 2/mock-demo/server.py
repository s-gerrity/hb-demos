import requests
from flask import Flask, render_template, request, jsonify
from model import connect_to_db, Employee

app = Flask(__name__)


def state_to_code(state_name):
    """Convert state name to a code. Uses "external" API."""

    r = requests.get("http://127.0.0.1:5001/name-to-code.json",
                     data={"state": state_name})
    return r.json()['code']


@app.route("/emps-by-state")
def emps_by_state():
    """See employees for a state."""

    state_name = request.args.get("state")
    code = state_to_code(state_name)
    emps = Employee.query.filter(Employee.state == code).all()

    return render_template("emps_by_state.html",
                           employees=emps,
                           state_name=state_name,
                           code=code)


@app.route("/emps-by-state.json")
def emps_by_state_json():
    """See employees for a state."""

    state_name = request.args.get("state_name")
    code = state_to_code(state_name)
    emps = Employee.query.filter(Employee.state == code).all()

    info = {code: []}
    for emp in emps:
        info[code].append({'id': emp.id,
                           'name': emp.name,
                           'state': emp.state,
                           'dept_code': emp.dept_code})

    return jsonify(info)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("homepage.html")


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    app.run(host='0.0.0.0')
