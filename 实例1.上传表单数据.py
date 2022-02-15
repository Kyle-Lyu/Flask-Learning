from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 设置跨域


@app.route('/')
def student():
    return render_template('login.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
