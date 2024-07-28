from flask import Flask


app = Flask(__name__)

# 路由 请求方式 端点
@app.route("/hello",methods=['POST','GET'],endpoint='hello')
def hello():
    return "<p>Hello, World!</p>"

@app.route("/hi",methods=['POST','GET'],endpoint='hi')
def hi():
    return "<p>Hi!</p>"

# 直接传数字而不需要转换
# @app.route("/user/<int:id>",methods=['POST','GET'])
@app.route("/user/<id>",methods=['POST','GET'])
def user(id):
    if id == '1':
        return "<p>python</p>"
    if id == str(2):
        return "<p>django</p>"
    if int(id) == 3:
        return "<p>flask</p>"
    return "<p>Hello World</p>"

# 导包
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):
    '''自定义转换器类'''
    def __init__(self, url_map, regex):
        # 调用父类方法
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        # 父类的方法，已经实现好的
        print("to_python方法被调用")
        return value

# 将自定义转换器添加到flask应用中
app.url_map.converters['re'] = RegexConverter

@app.route('/index/<re("123"):value>')
def index(value):
    print("value")
    return "hello"

if __name__ == '__main__':
    app.run()