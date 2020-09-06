from app import app
from flask import render_template, request, g
import sqlite3

#database path
DATABASE = '/home/shivani/Learning/python/photo_app/photo_app'

#establish database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

#close database connetion
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#execute queries
def query_db(query, args=(), one=False):
	cur = get_db().execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv

#initialising schema
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()



#routes
@app.route('/')
@app.route('/index')
def index():
	return render_template('login.html', title='Login')

@app.route('/login', methods=['POST'])
def login():
	#fetch user input
	username = request.form['username']
	password = request.form['password']

	#query to fetch user record if exists
	user = query_db('select * from users where username = ?',
                [username], one=True)

	if user and password == user['password']:
		return render_template("my_photos.html", username=username)
	else:
		print("login failed")
		return render_template("login.html", message='Incorrect username/password. Try again!')
