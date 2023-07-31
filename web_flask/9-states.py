#!/usr/bin/python3
<<<<<<< HEAD
""" Starts a Flash Web Application """
from flask import Flask, render_template
from models import *
from models import storage
=======
""" Script that runs an app with Flask framework """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


>>>>>>> 7f61b772f728a880b09b506a47b10166c1943b1c
app = Flask(__name__)


@app.teardown_appcontext
<<<<<<< HEAD
def teardown_db(exception):
    """ After each request remove the current SQLAlchemy """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def get_states(state_id=None):
    """ display a HTML page"""
    states = storage.all("State")

    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html',
                           states=states, state_id=state_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
def teardown_session(exception):
    """ Teardown """
    storage.close()


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_html(id=None):
    """ Function called with /states route """
    states = storage.all(State)

    if not id:
        dict_to_html = {value.id: value.name for value in states.values()}
        return render_template('7-states_list.html',
                               Table="States",
                               items=dict_to_html)

    k = "State.{}".format(id)
    if k in states:
        return render_template('9-states.html',
                               Table="State: {}".format(states[k].name),
                               items=states[k])

    return render_template('9-states.html',
                           items=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 7f61b772f728a880b09b506a47b10166c1943b1c
