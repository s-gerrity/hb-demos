"""Example of SQLAlchemy Many-To-Many."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


class Book(db.Model):
    """Book."""

    __tablename__ = 'books'

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))

    genres = db.relationship("Genre",
                             secondary="books_genres",
                             backref="books")
    # !end Book attributes

    def __repr__(self):
        return "<Book title={}>".format(self.title)


class Genre(db.Model):
    """Genre of book."""

    __tablename__ = 'genres'

    genre_id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(50), unique=True)
    # !end Genre attributes

    def __repr__(self):
        return "<Genre id={} {}>".format(self.genre_id, self.genre)


class BookGenre(db.Model):
    """Genre of a specific book."""

    __tablename__ = 'books_genres'

    book_genre_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer,
                        db.ForeignKey('books.book_id'),
                        nullable=False)
    genre_id = db.Column(db.Integer,
                         db.ForeignKey('genres.genre_id'),
                         nullable=False)
    # !end BookGenre attributes

    def __repr__(self):
        return "<BookGenre book_id={} genre_id={}>".format(self.book_id, self.genre_id)


def connect_to_db(app):
    """Connect to database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///many-to-many-genre"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    import os

    os.system("dropdb many-to-many-genre")
    os.system("createdb many-to-many-genre")

    connect_to_db(app)

    # Make our tables
    db.create_all()

    # Add a book and genres
    hamlet = Book(title="Hamlet")
    fantasy = Genre(genre="Fantasy")
    tech = Genre(genre="Technology")

    # Can add using relationships
    hamlet.genres.append(fantasy)
    tech.books.append(hamlet)

    # Since the printings are part of Hamlet, we only have to add Hamlet to the
    # session to get them all
    db.session.add(hamlet)
    db.session.commit()

    # Test that this worked
    number_bookgenres = BookGenre.query.count()
    assert number_bookgenres == 2
