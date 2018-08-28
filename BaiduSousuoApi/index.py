from flask import Flask
from flask import render_template
from BaiduSousuoApi.baiduspider import getBdMsg
from flask import request

app = Flask(__name__)


# 装饰器 给函数新增功能的
@app.route('/')  # 路由
def index():
    return render_template('index.html')


@app.route('/hanxun')
def demo():
    return "hello hanxun - python"

@app.route('/s')
def search():
    keyword = request.args.get('wd')
    page = request.args.get('pn')
    text = getBdMsg(keyword,page)
    return text

if __name__ == '__main__':
    app.run(debug=True, port=8001)
