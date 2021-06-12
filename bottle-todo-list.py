'''
Simple Bottle todo list CRUD web application
'''
import os
import sqlite3
from bottle import route, run, debug, template, request,TEMPLATE_PATH,redirect,request

"""
Connection Config
"""
host = "localhost"
port = 8080
autoreload = True
#hoststr = f'{host}{f":{port}" if port and port not in (80,443) else ""}'

fp = __file__.split('/')
print('/'.join(fp[0:-1]))
TEMPLATE_PATH.insert(0, f"{'/'.join(fp[0:-1])}/static") #sets the template path to the "static" folder local script dir

def init():
    conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
    conn.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
    conn.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
    conn.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
    conn.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
    conn.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
    conn.commit()

def exec_query(query):
    with sqlite3.connect('todo.db') as conn:
        c = conn.cursor()
        c.execute(query)
        return c.fetchall()

@route('/makeactive/<rowid>')
def make_active(rowid=None):
    if rowid:
        exec_query( f'UPDATE todo SET status=1 WHERE id={rowid};' )
    redirect('/todo')

@route('/makedone/<rowid>')
def make_done(rowid=None):
    if rowid:
        exec_query( f'UPDATE todo SET status=0 WHERE id={rowid};' )
    redirect('/todo')

@route('/todo')
def todolist():
    if not os.path.exists(f"{'/'.join(fp[0:-1])}/todo.db"):
        print("Initializing the database")
        redirect ('/init')
    res  = exec_query( "SELECT id, task from todo where status=1" )
    res2 = exec_query( "SELECT id, task from todo where status=0" )
    rowids = exec_query( "SELECT id from todo")
    return template('make_table', activerows=res, donerows=res2, rowids=rowids)

@route('/init')
def initialize():
    init()
    redirect('/todo')

@route('/addnew',method='POST')
def brandnew_item():
    if request.forms.get('newitem') not in (None, ''):
        print( request.forms.get('newitem') )
        exec_query( f'INSERT INTO todo (task,status) VALUES("{request.forms.get("newitem")}",{request.forms.get("status")})' )
    redirect('/todo')

@route('/updateitem',method='POST')
def update_item():
    if request.forms.get('updatedtask') not in (None, ''):
        exec_query( f"UPDATE todo SET task='{request.forms.get('updatedtask')}' WHERE id='{request.forms.get('rowid')}'" )
    redirect('/todo')

@route('/delete/<rowid>')
def delete_row(rowid):
    try:
        if int(rowid) and None != rowid:
            exec_query(f"delete from todo where id={rowid}")
    except ValueError:
        pass
    finally:
        redirect("/todo")

run(host=host,port=port, reloader=autoreload)