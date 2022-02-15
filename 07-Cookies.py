from flask import Flask, request, Response, render_template, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('set_cookie'))  # 重定向

# 获取cookie
@app.route('/get_cookie')
def get_cookie():
    cookie = request.cookies.get('user')  # 获取关键字为user对应cookie的值
    print(cookie)
    return render_template('get_cookie.html', cookie=cookie)


# 设置cookie
@app.route('/set_cookie')
def set_cookie():
    html = render_template('show_cookie_by_JQuery.html')
    response = make_response(html)  # 设置响应体
    # response = Response(html)
    response.set_cookie('user', 'Kint')
    return response


# 删除cookie
@app.route('/del_cookie')
def del_cookie():
    html = render_template('show_cookie_by_JQuery.html')
    response = Response(html)
    response.delete_cookie('user')
    return response


if __name__ == '__main__':
    app.run(debug=True)
