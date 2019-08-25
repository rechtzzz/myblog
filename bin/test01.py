import pymysql
import sqlalchemy
from user_add import *

sear = search()

#data = sear.session.query(User).filter(User.username == 'admin').first()
data1 = sear.session.query(User).filter(User.username == 'admin1').first()
user_data = sear.session.query(User).filter(User.username == 'admin1').first()
#login_pwd = user_search.session.query(User).filter(User.password == form.password.data).first()

if user_data is None:
    print('用户不存在，请先注册')
else:
    login_name, login_pwd = user_data.username, user_data.password
    if 'admin1' == login_pwd:
        print(f'{login_name} logining in , remember ')
        #return redirect(url_for('user_blog'))
    else:
        print('密码错误')
        #return render_template('login.html', name = form.username.data, form = form)




