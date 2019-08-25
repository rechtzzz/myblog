import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://zhangxt:qwerqwer@localhost:3306/testdb?charset=utf8'
    #如果你不打算使用mysql，使用这个连接sqlite也可以
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
