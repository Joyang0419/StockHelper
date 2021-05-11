from app import db
# login manager
from flask_login import UserMixin
from app import login_manager


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    @classmethod
    def create(cls, **kwargs):
        """新增"""
        obj = cls(**kwargs)
        db.session.add(obj)
        db.session.commit()
        return obj

    @login_manager.user_loader
    def user_loader(user_id):
        return Users.query.get(int(user_id))
