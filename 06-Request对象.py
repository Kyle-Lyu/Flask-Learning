from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("Request.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    print('url: ', request.url)
    print('base_url: ', request.base_url)
    print('host: ', request.host)
    print('host_url: ', request.host_url)
    print('path: ', request.path)
    print('full_path: ', request.full_path)

    print('request.method:\n', request.method)
    print('request.data:\n', request.data)
    print('request.request.args:\n', request.args)
    print("request.request.args.get('b'):\n", request.args.get('c'))
    print('request.form:\n', request.form)
    print("request.request.form.get('password'):\n", request.form.get('password'))
    print('request.values:\n', request.values)
    print('request.json:\n', request.json)
    print('request.cookies:\n', request.cookies)
    print('request.headers:\n', request.headers)
    return json.dumps(request.form)


if __name__ == '__main__':
    app.run(debug=True)
