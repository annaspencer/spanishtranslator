##models
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
db = SQLAlchemy()



def connect_db(app):
    """connect to db"""
    db.app = app
    db.init_app(app)

class User(db.Model):

    __tablename__ = "users"

   
    username = db.Column(db.Text, nullable=False, unique=True, primary_key=True)
    password = db.Column(db.Text, nullable=False)

    

   
    
    @classmethod 
    def register(cls, username, password):
        """register user, set password"""
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        user = cls(
            username=username,
            password=hashed_utf8,
             )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, pwd):
        """validates usrname and password"""
        u =User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):

            return u 
        else:
            return False
    

class Vocab(db.Model):

    __tablename__ = "vocab"

   
    title = db.Column(db.Text, nullable=False, unique=True, primary_key=True)
    username =db.Column(db.Text, db.ForeignKey('users.username'))

    user = db.relationship('User', backref="lists")


class Word(db.Model):

    __tablename__ = "words"

   
    word = db.Column(db.Text, nullable=False, unique=True, primary_key=True)
    translation = db.Column(db.Text, nullable=False)
    list_title = db.Column(db.Text, db.ForeignKey('vocab.title'))
    
    v_list = db.relationship('Vocab', backref="words")

