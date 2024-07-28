# flask 数据库
# pip install flask_sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Config:
    '''配置参数'''
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/db01'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)

# SQLAlchemy 和 app 绑定
db = SQLAlchemy(app)

# 创建数据库模版类
class Role(db.Model):
    # 角色表
    __tablename__ = 'role'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)

class User(db.Model):
    # 用户表
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),unique=True)
    password = db.Column(db.String(128))
    # 表关系 外键ForeignKey 用来关联到另一张表
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))

if __name__ == '__main__':
    # 清楚所有的表
    db.drop_all()
    # 创建所有的表
    db.create_all()

    # 创建对象 插入数据】
    role1 = Role(name='admin')
    # session 记录到对象任务中
    db.session.add(role1)
    # 提交任务
    db.session.commit()