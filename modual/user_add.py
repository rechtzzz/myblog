from build_db import *
from sqlalchemy.orm import sessionmaker


class search():
    def __init__(self):
        self.Session_class = sessionmaker(engine)
        self.session = self.Session_class()
class register():
    def __init__(self,username,password):
        self.Session_class = sessionmaker(engine)
        self.session = self.Session_class()
        self.username = username
        self.password = password
    def add_user(self):
        data = User(username=self.username,password=self.password)
        self.session.add(data)

        self.session.commit()
#data = session.query(User).filter(User.username == 'admin').all()

