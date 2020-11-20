from flask import render_template, request, redirect
from app import app



@app.route('/<var1>/<var2>')
def index(var1,var2):
    print (var1)
    print (var2)
    return render_template('index.html', title = 'Home')

