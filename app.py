from flask import Flask, render_template, request, redirect, session, flash, jsonify
import smtplib
import sqlite3

app=Flask(__name__)


#route() decorators
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def back_to_index():
    return render_template('index.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True)