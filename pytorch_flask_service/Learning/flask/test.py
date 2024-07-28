from flask import Flask,json,make_response

app = Flask(__name__)

@app.route('/index')
def index():
    data = {
        'name': '张三'
    }
    return make_response(json.dumps(data, ensure_ascii=False)) # 将数据传给前端,ensure_ascii编码默认为true




if __name__ == '__main__':
    app.run()