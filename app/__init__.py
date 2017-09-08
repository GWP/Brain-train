from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('whetlog')

# Adds a small cache reload time to all UI files
class MyFlask(Flask):
    def get_send_file_max_age(self, name):
        if name.lower().endswith('.css') or name.lower().endswith('.html') or name.lower().endswith('.js'):
            return 5
        return Flask.get_send_file_max_age(self, name)


# Define the WSGI application object
app = MyFlask(__name__.split('.')[0])

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', statuscode=404, error=error), 404

@app.errorhandler(500)
def internal_error(error):
    try:
        db.session.rollback()
    except Exception as err:
        logging.error("DB rollback failed: {}".format(err))
    return render_template('error.html', statuscode=500, error=error), 500

# Import a module / component using its blueprint handler variable
from app.math_teasers.routes import math_teasers

# Register blueprint(s)
app.register_blueprint(math_teasers)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()