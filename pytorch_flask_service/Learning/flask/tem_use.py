from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    data = {
        'name': 'zhangsan',
        'age': 18,
        'mylist': [1, 2, 3, 4, 5]
    }
    return render_template('index2.html', data=data)


# 自定义过滤器
def list_step(li):
    return li[::2]
# li = [1, 2, 3, 4, 5]

# 注册过滤器  第一个值写自定义函数的名字 第二个值写你要用时候的名字
app.add_template_filter(list_step, 'li2')

if __name__ == '__main__':
    app.run()
