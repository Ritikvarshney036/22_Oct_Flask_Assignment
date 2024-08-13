import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Database setup
DATABASE = 'items.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as db:
        db.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
    print("Initialized the database.")

@app.route('/')
def home():
    db = get_db()
    items = db.execute('SELECT * FROM items').fetchall()
    return render_template('home.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        db = get_db()
        db.execute('INSERT INTO items (name) VALUES (?)', (name,))
        db.commit()
        return redirect(url_for('home'))
    return render_template('add_item.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    db = get_db()
    item = db.execute('SELECT * FROM items WHERE id = ?', (id,)).fetchone()
    
    if request.method == 'POST':
        name = request.form['name']
        db.execute('UPDATE items SET name = ? WHERE id = ?', (name, id))
        db.commit()
        return redirect(url_for('home'))
    
    return render_template('edit_item.html', item=item)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_item(id):
    db = get_db()
    db.execute('DELETE FROM items WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
