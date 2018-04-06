from flask import Flask, redirect, render_template, session, request
import math
import random
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
	session['number'] = math.floor(random.random()*100+1)
	return render_template('index.html')

@app.route('/guess/<number>')
def guess(number):
	print session['number']
	if int(number) == session['number']:
		return (number + " is correct!!")
	elif int(number) > session['number']:
		return (number + " is too high!")
	else:
		return (number + " is too low!!")


app.run(debug=True)