from flask import Flask, redirect


app = Flask(__name__)
new_url = 'http://maps.t-mobile.com/TMo_TechLTE_Map/6/5:11/tile.png'
# http://amir.rachum.com/blog/2016/08/27/flask-redirect/
# http://maps.t-mobile.com/TMo_TechLTE_Map/{z}/{x}:{y}/tile.png


@app.route('/')
def root():
    return redirect(new_url, code=302)


@app.route('/<path:page>')
def anypage(page):
    return redirect('{new_url}/{page}'.format(page=page, new_url=new_url),
                    code=302)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# 1. use regexes to parse your url, find the z, x, and y, and add +1s
# 2. come up with a new url structure that maybe has the z, x, and y as query string parameters or path parameters and have flask interpret those to add +1s and ask tmobile for the tile
