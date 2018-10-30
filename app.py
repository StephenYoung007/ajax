from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    make_response,
    send_from_directory,
)
import os
from mongo import find

app = Flask(__name__)


@app.route('/test')
def hello_world():
    return find()

@app.route('/', methods=['GET', 'POST'])
def demo():
    return render_template('index.html')


@app.route('/uploads/<filename>')
def uploads(filename):
    data_file_directory = r'E:\ajax\static'
    return send_from_directory(data_file_directory, filename)


@app.route('/like', methods=['GET'])
def like():
    thumb = request.args.get('soc', '')
    stat = thumb.split('/')[-1]
    print(stat)
    if stat == 'like.png':
        return r'/uploads/dislike.png'
    if stat == 'dislike.png':
        return r'/uploads/like.png'


if __name__ == '__main__':
    # config = dict(
    #     debug = True,
    #     ,
    #
    # )
    app.run(host='0.0.0.0')
