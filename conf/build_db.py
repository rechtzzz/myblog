from sqlalchemy import String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
engine = create_engine('mysql+pymysql://zhangxt:qwerqwer@localhost:3306/testdb',echo = False)
class User(Base):
    __tablename__ = 'myblog'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    sex = Column(String(5),default='F',nullable=False)
    #password_hash = db.Column(db.String(128))
    password = Column(String(128))
    def __str__(self):
        return f'user_id:{self.user_id}    username:{self.username}    '
if __name__ == '__main__':
    Base.metadata.create_all(engine)

