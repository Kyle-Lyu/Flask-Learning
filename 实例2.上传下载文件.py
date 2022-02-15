from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename

import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000  # 上传文件大小限制为16M，如果超过会抛出异常
CORS(app, supports_credentials=True)  # 设置跨域


@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        print(request.files)
        # secure_filename检查客户端上传的文件名，确保安全，注意文件名称不要全中文！！！
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return render_template('upload.html')
    else:
        return render_template('index.html')


@app.route('/download/<filename>', methods=['GET', 'POST'])
def download(filename):
    # as_attachment=True 表示文件作为附件下载
    return send_from_directory('./upload', filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
