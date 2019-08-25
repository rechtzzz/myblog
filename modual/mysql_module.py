
from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    sex = db.Column(db.String(5),default='F',nullable=False)
    #password_hash = db.Column(db.String(128))
    password = db.Column(db.String(20))


if __name__ == '__mian__':
    #自助添加用户
    user1 = User(username='name',password='pwd')
    db.session.add(user1)
    db.session.commit()