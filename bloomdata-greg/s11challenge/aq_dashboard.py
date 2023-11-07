"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import openaq

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(app)

api = openaq.OpenAQ()


class Record(DB.Model):
    # id (integer, primary key)
    id = DB.Column(DB.Integer, primary_key=True)
    # datetime (string)
    datetime = DB.Column(DB.String, nullable=False)
    # value (float, cannot be null)
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f'({self.datetime}, {self.value})'


@app.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    # Get data from OpenAQ, make Record objects with it, and add to db
    results = get_results()
    for result in results:
        DB.session.add(Record(datetime=result[0], value=result[1]))
    DB.session.commit()
    return 'Data refreshed!'


def get_results():
    status, body = api.measurements(city='Los Angeles', parameter='pm25')
    if status == 200:
        return [(x['date']['utc'], x['value']) for x in body['results']]
    else:
        return []


@app.route('/')
def root():
    """Base view."""
    results = Record.query.filter(Record.value >= 18).all()
    # return str([(result.datetime, result.value) for result in results])
    s = '['
    for result in results:
        s = s + '(' + result.datetime + ', ' + str(result.value) + '), '
    return s[:-2] + ']'
