from flask import Flask

app = Flask(__name__)
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Configure the database
import database
database.configure_database(app)

# Import and register route blueprints
from routes import students, classes, listings, valuations, temporary_valuations

app.register_blueprint(students.bp)
app.register_blueprint(classes.bp)
app.register_blueprint(listings.bp)
app.register_blueprint(valuations.bp)
app.register_blueprint(temporary_valuations.bp)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
