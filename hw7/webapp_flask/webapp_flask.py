from flask import Flask
import sqlite3 as sql

DATABASE = "test.db"

app = Flask(__name__)


@app.route('/persons')
def get_names():
    con = sql.connect(DATABASE)
    cur = con.cursor()
    cur.execute('select name from persons;')
    rows = ['%s' % row for row in cur.fetchall()]
    cur.close()
    con.close()
    return '; '.join(rows)


@app.route('/persons/<name>')
def get_data(name):
    con = sql.connect(DATABASE)
    cur = con.cursor()
    cur.execute('select age, profession from persons where name =?', (name,))
    rows = cur.fetchall()
    cur.close()
    con.close()
    return '%s' % rows


@app.route('/persons/<name>/age')
def get_age(name):
    con = sql.connect(DATABASE)
    cur = con.cursor()
    cur.execute('select age from persons where name =?', (name,))
    rows = ['%s' % row for row in cur.fetchall()]
    cur.close()
    con.close()
    return '%s' % rows


@app.route('/persons/<name>/profession')
def get_profession(name):
    con = sql.connect(DATABASE)
    cur = con.cursor()
    cur.execute('select profession from persons where name =?', (name,))
    rows = ['%s' % row for row in cur.fetchall()]
    cur.close()
    con.close()
    return '%s' % rows


if __name__ == "__main__":
    app.run(debug=True, port=8888)
