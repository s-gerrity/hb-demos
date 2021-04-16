"""Example of SQLAlchemy One-To-Many."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


class Book(db.Model):
    """Book."""

    __tablename__ = 'books'

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))

    # !end Book attributes (this comment is for generating lecture handouts)

    def add_printing(self, print_date):
        """Add a printing."""

        self.printings.append(Printing(print_date=print_date))

    def __repr__(self):
        return "<Book title={}>".format(self.title)


class Printing(db.Model):
    """Printing of a book."""

    __tablename__ = 'printings'

    printing_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer,
                        db.ForeignKey('books.book_id'),
                        nullable=False)
    print_date = db.Column(db.DateTime)

    book = db.relationship('Book', backref='printings')
    
    # !end Printing attributes (this comment is for generating lecture handouts)

    def __repr__(self):
        return "<Printing book={} date={}>".format(self.book_id, self.print_date)


def connect_to_db(app):
    """Connect to database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///one-to-many"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from datetime import datetime
    import os

    os.system("dropdb one-to-many")
    os.system("createdb one-to-many")

    connect_to_db(app)

    # Make our tables
    db.create_all()

    # Can add things separately using ID
    hamlet = Book(title="Hamlet")

    # Can add things separately using object
    hamlet_p2 = Printing(book=hamlet, print_date=datetime(2015, 1, 1))

    # Can add using printing property on book
    hamlet.printings.append(Printing(print_date=datetime(2015, 2, 1)))

    # Or with an instance method
    hamlet.add_printing(datetime(2017, 3, 16))

    # Since the printings are part of Hamlet, we only have to add Hamlet to the
    # session to get them all
    db.session.add(hamlet)
    db.session.commit()

    # Test that this worked
    printings = Book.query.filter_by(title='Hamlet').one().printings
    assert len(printings) == 3
    print(printings)
