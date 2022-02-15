from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    int_ = 1024
    str_ = 'Hello World!'
    list_ = [1, 2, 3, 4, 5]
    dict_ = {'name': 'Kint', 'age': 23}
    # render_template方法:渲染模板
    # 参数1: 模板名称  参数n: 传到模板里的数据
    return render_template('render_template.html', my_int=int_, my_str=str_, my_list=list_, my_dict=dict_)


if __name__ == '__main__':
    app.run(debug=True)
