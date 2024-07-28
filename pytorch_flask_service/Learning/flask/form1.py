from flask import Flask,render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        print("get")
        return render_template('index.html')
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        print(name,password)
        return 'this is post'

@app.route('/redirect')
def ret():
    #return redirect(url_for('index'))
    return redirect('https://www.baidu.com')


if __name__ == "__main__":
    app.run()