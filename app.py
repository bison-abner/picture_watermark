from flask import Flask, render_template, request, redirect, url_for

import os

from werkzeug.utils import secure_filename

from imageEmbeddedWatermark import embed_watermark
from imageExtractionWatermark import extract_watermark
from flask import send_from_directory
app = Flask(__name__)


UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp3','wav'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return '文件未提供'
    file = request.files['file']
    if file.filename == '':
        return '没有选择文件'
    if file and allowed_file(file.filename):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        # 文件上传成功，重定向到输入水印文本的页面
        return redirect(url_for('enter_watermark', filename=file.filename))
    return '不支持的文件类型'

@app.route('/enter_watermark/<filename>', methods=['GET'])
def enter_watermark(filename):
    # 显示水印文本输入表单的页面
    return render_template('enter_watermark.html', filename=filename)

@app.route('/apply_watermark', methods=['POST'])
def apply_watermark():
    filename = request.form['filename']
    watermark_text = request.form['watermark']

    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    output_filename = "wm_" + filename
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)

    # 嵌入水印
    embed_watermark(input_path, output_path, watermark_text)
    original_image_url = url_for('static', filename='uploads/' + filename)
    watermarked_image_url = url_for('static', filename='output/' + output_filename)

    return render_template('watermark_success.html',
                           original_image_url=original_image_url,
                           watermarked_image_url=watermarked_image_url,
                           filename=output_filename)

@app.route('/watermark_extraction', methods=['POST'])
def watermark_extraction():
    filename = request.form['filename']
    input_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    # 水印长度文件的路径
    len_wm_path = os.path.join(app.config['OUTPUT_FOLDER'], 'watermark_length.txt')

    # 调用 extract_watermark 函数进行水印提取
    watermark = extract_watermark(input_path, len_wm_path)

    # 返回提取的水印文本
    return render_template('watermark_extraction_result.html', watermark=watermark, filename=filename)

    # 从表单中获取文件名
    # filename = request.form['filename']
    # output_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    #
    # # 读取水印长度
    # config_path = os.path.join(app.config['OUTPUT_FOLDER'], 'watermark_length.txt')
    # with open(config_path, 'r') as f:
    #     len_wm = int(f.read())
    # # 这里添加提取水印的代码
    # # 注意：您需要知道水印的长度或其他相关参数
    # watermark = '这里是提取的水印文本'  # 这里应该是提取水印的结果
    #
    # # 返回提取的水印文本
    # return render_template('watermark_extraction_result.html', watermark=watermark, filename=filename)
    #

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
