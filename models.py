from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager

login = LoginManager()
db = SQLAlchemy()

class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'

    super = db.Column(db.Boolean, default=False)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String())

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

@login.user_loader
def load_user(id):
    return UserModel.query.get(int(id))


class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    ordinal = db.Column(db.Integer)
    fulfilled = db.Column(db.Boolean, default=False)

    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    url = db.Column(db.String(200))
    img_url = db.Column(db.String(200))
    description = db.Column(db.String(500))
