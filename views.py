"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from CS_ISU import app 

@app.route('/')
@app.route('/login/', methods=['POST', 'GET'])
def login():
    '''renders the login or first page'''
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'adminpassword':
            error = 'Invalid Login'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    '''Renders the home page.'''
    return render_template( 
        'index.html',
        title='Home',
        year=datetime.now().year,
        )
'''All the code below is about the pages that take inputs from the user (username, password, url) and saves them to be stored for later access'''    
@app.route('/inputs')
def inputs():
    '''renders inputs page'''
    return render_template('inputs.html')

'''If the user searches for the data and no data exists, returns empty page. if they input data or if data already exists then it will either update data and then display it all, or just display it all'''
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    '''renders data page, stores data from inputs page'''
    if request.method == 'GET':
        return f"Error, no data"
    if request.method == "POST":
        inputs_data = request.form
        return render_template('data.html', inputs_data = inputs_data)

@app.route('/contact')
def contact():
    """Renders contact page."""
    return render_template(
        'contact.html',
        title='Contact and Information',
        year=datetime.now().year,
        message='Connect with us at : '
    )

@app.route('/about')
def about():
    """Renders info page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

app.run(host='localhost', port=5000)
