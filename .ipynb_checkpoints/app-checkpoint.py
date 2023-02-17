from flask import Flask, g, render_template, request

import sklearn as sk
import matplotlib.pyplot as plt
import numpy as np
import pickle

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import io
import base64
import sqlite3

### stuff from last class
app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')


#######
@app.route('/submit/', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        message, handle = insert_message(request)
        return render_template('submit.html', thanks = True, handle = handle, message = message)


# matplotlib: https://matplotlib.org/3.5.0/gallery/user_interfaces/web_application_server_sgskip.html
# plotly: https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946
@app.route('/view/')
def view():
    messages = random_messages(3)
    return render_template('view.html', messages = messages)
    

        
def get_message_db():
    # use the try except command to test if there is a database called message_db in the g attribute of the app
    # if there is, we just return the database; if there is not, go to the except
    try:
        return g.message_db
    
    #if there is no such database in g, we just connect one in the attribute g
    except:
        g.message_db = sqlite3.connect("messages_db.sqlite")
        
        # use the SQL command to check if there is a table called messages in the database
        # if there is no such table, we create one in the database
        # with three columns id, handle, and message
        cmd = """CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY,
                handle TEXT,
                message TEXT)"""
        cursor = g.message_db.cursor()
        cursor.execute(cmd)
        return g.message_db
    
    
def insert_message(request):
    # extract message and handle from request
    message = request.form['message']
    handle = request.form['handle']
    
    # call the function get_message_db() to connect to the database
    db = get_message_db()
    
    # get a cursor object
    cursor = db.cursor()
    
    # get current number of row of the table 
    cursor.execute("SELECT COUNT(*) FROM messages")
    id_num = cursor.fetchone()[0] + 1
    
    # insert id, message, and handle into the table
    cursor.execute("INSERT INTO messages (id, handle, message) VALUES (?, ?, ?)", (id_num, handle, message))
    db.commit()
    
    # close the connection
    db.close()
    
    return message, handle


def random_messages(n):
    # call the function get_message_db() to connect to the database
    db = get_message_db()
    
    # get a cursor object
    cursor = db.cursor()
    
    # get n random messages from the table
    cursor.execute("SELECT * FROM messages ORDER BY RANDOM() LIMIT ?",(n,))
    
    # get all the messages 
    messages = cursor.fetchall()
    db.close()
    
    return messages
    