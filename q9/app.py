from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'published_date': self.published_date
        }

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    if book is None:
        abort(404)
    return jsonify(book.to_dict())

@app.route('/books', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    
    # Validate required fields
    title = request.json.get('title')
    if not title:
        abort(400, description="Title is required")

    new_book = Book(
        title=title,
        author=request.json.get('author', ''),
        published_date=request.json.get('published_date', '')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if book is None:
        abort(404)
    if not request.json:
        abort(400)
    
    # Update book fields
    book.title = request.json.get('title', book.title)
    book.author = request.json.get('author', book.author)
    book.published_date = request.json.get('published_date', book.published_date)
    
    db.session.commit()
    return jsonify(book.to_dict())

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        abort(404)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
