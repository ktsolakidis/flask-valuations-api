import pymysql
from flask_mysqldb import MySQL

db = MySQL()

def configure_database(app):
    app.config['MYSQL_HOST'] = 'database-1.cfuyzohcw40b.us-east-1.rds.amazonaws.com'
    app.config['MYSQL_USER'] = 'admin'
    app.config['MYSQL_PASSWORD'] = '3869kT00'
    app.config['MYSQL_DB'] = 'sys'
    db.init_app(app)
