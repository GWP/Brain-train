from flask_sqlalchemy import SQLAlchemy
from app import db

class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

class User(Base):
    nickname = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=False)
    problems = db.relationship('Problem', backref='author', lazy='dynamic')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User {}>'.format(self.nickname)


class Problem(Base):
    question = db.Column(db.String(140))
    difficulty = db.Column(db.String(64))
    answer = db.Column(db.String(140))
    problem_type = db.Column(db.String(64))
    # timestamp = db.Column(db.DateTime)
    time_to_complete = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.question)

