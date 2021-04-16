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

    comments = db.relationship("Comment")
    # !end Book attributes

    @classmethod
    def get_by_title(cls, title):

        # Book.get_by_title("Hamlet")
        return cls.query.filter_by(title=title).one()

    def __repr__(self):
        return "<Book title={}>".format(self.title)


class User(db.Model):
    """User of site."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))

    comments = db.relationship("Comment")
    # !end User attributes
    
    # books = db.relationship("Book",
    #                          secondary="comments",
    #                          backref="users")

    def __repr__(self):
        return "<User id={} email={}>".format(self.user_id, self.email)


class Comment(db.Model):
    """Comment on a book by a user."""

    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer,
                        db.ForeignKey('books.book_id'),
                        nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    body = db.Column(db.Text, nullable=False)

    book = db.relationship("Book")
    user = db.relationship("User")
    # !end Comment attributes

    def __repr__(self):
        return "<Comment id={} body={}...>".format(self.comment_id,
                                                   self.body[:10])


def connect_to_db(app):
    """Connect to database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///many-to-many"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    import os

    os.system("dropdb many-to-many")
    os.system("createdb many-to-many")

    connect_to_db(app)

    # Make our tables
    db.create_all()

    # Add a book and a user
    hamlet = Book(title="Hamlet")
    jane = User(email="jane@jhacks.com")

    # Can add things separately using objects
    comment1 = Comment(book=hamlet, user=jane, body="I loved it!")
    db.session.add(comment1)

    # Can add using relationships
    hamlet.comments.append(Comment(user=jane, body="I hated it!"))
    jane.comments.append(Comment(book=hamlet, body="It was meh!"))

    # Since the printings are part of Hamlet, we only have to add Hamlet to the
    # session to get them all
    db.session.add(hamlet)
    db.session.commit()

    # Test that this worked
    comments = Book.get_by_title("Hamlet").comments
    print(comments)
    assert len(comments) == 3
