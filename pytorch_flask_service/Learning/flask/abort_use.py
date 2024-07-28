from flask import Flask, abort, request, make_response, render_template

app = Flask(__name__)

'''异常抛出'''

@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        print('get')
        return render_template('index.html')
    if request.method == 'POST':
        print('post')
        name = request.form.get('name')
        password = request.form.get('password')
        if name == '123' and password == '111':
            return 'login access'
        else:
            abort(404)
            return None


# 自定义错误类型处理方法
@app.errorhandler(404)
def handle_404_error(err):
    return render_template('404.html')


if __name__ == '__main__':
    app.run()
