from flask import Flask,flash,redirect,url_for
from flask import render_template,request
from config import *
from user_add import *
from flask_sqlalchemy import SQLAlchemy
try:
    from forms import *
except Exception as e:
    print('no forms')

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('login',methods=['GET','POST'])
# def login():
#     # GET请求
#     user_search = search()
#     form = LoginForm()
#     if request.method == "GET":
#         return render_template('login.html', name = form.username.data, form = form)
#     # POST请求
#     if request.method == "POST":
#
#         # print(request.headers)
#         # print(request.json)
#         # print(request.data)
#         # 获取数据并转化成字典
#         user_info = request.form.to_dict()
#         user_data_db = user_search.session.query(User).filter(User.username == user_info.username).first()
#         if user_data_db is None:
#             flash('用户不存在')
#         else:
#             login_name, login_pwd = user_data_db.username, user_data_db.password
#             if user_info.get("username") == login_name and user_info.get("password") == login_pwd:
#                 flash(f'{form.username.data} logining in , remember ')
#                 return redirect(url_for('user_blog',name=login_name))
#
#             else:
#                 flash('密码错误')
#                 return render_template('login.html', name=login_name, form=form)
#     return render_template('login.html', name=form.username.data, form=form)
#     # print(request.form.to_dict())
#     # # args 获取地址栏的hash值
#     # print(request.args.to_dict())

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    user_search = search()
    if form.validate_on_submit():
        user_data = user_search.session.query(User).filter(User.username == form.username.data).first()
        #login_pwd = user_search.session.query(User).filter(User.password == form.password.data).first()

        if user_data is None:
            flash('用户不存在，请先注册')
        else:
            login_name, login_pwd = user_data.username, user_data.password
            if form.password.data == login_pwd:
                flash(f'{form.username.data} logining in , remember ')
                return redirect(url_for('user_blog',name=login_name))
            else:
                flash('密码错误')
                return render_template('login.html', name = login_name, form = form)

        #j尽量不让提交表单的最后一个ｐｏｓｔ请求作为最后一个请求，重定向会让浏览器重新发送一个ｇｅｔ请求
        #防止重复提交表单　　　
    return render_template('login.html', name = form.username.data, form = form)

@app.route('/register',methods=['POST','GET'])
def user_register():
    form = Regiestr()
    if form.validate_on_submit():
        username,password= form.username.data,form.password.data
        user_reg = register(username,password)
        user_reg.add_user()
    return render_template('regiest.html',form = form)

@app.route('/user_blog/<name>',methods=['POST','GET'])
def user_blog(name):
    form= LoginForm()
    return render_template('blog.html',name = name)

@app.route('/user_blog/personal',methods=['POST','GET'])
def personal():
    return render_template('personal.html')
if __name__ == '__main__':
    app.run()