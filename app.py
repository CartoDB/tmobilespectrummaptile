from flask import Flask, redirect


app = Flask(__name__)
new_url = 'http://maps.t-mobile.com/TMo_TechLTE_Map/6/5:11/tile.png'
new_url = 'http://maps.t-mobile.com/TMo_TechLTE_Map/'
# http://amir.rachum.com/blog/2016/08/27/flask-redirect/
# http://maps.t-mobile.com/TMo_TechLTE_Map/{z}/{x}:{y}/tile.png
# localhost:5000
# localhost:5000/{z}/{x}/{y}.png
# http://tmobilespectrummaptile.cartodb.io/{z}/{x}/{y}.png
# http://tmobilespectrummaptile.cartodb.io/0/0/0.png
# https://
# https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png


def urlChange(inURL):
    z = 6
    x = 5
    y = 11
    # z = int(inURL.split('Map/')[1].split('/')[0])
    # x = int(inURL.split('/')[5].split(':')[0])
    # y = int(inURL.split(':')[2].split('/')[0])
    # z = z + 1
    # x = x + 1
    # y = y + 1
    newURL = 'http://maps.t-mobile.com/TMo_TechLTE_Map/'+str(z)+'/'+str(x)+':'+str(y)+'/tile.png'
    return newURL


@app.route('/')
def root():
    print redirect(urlChange(new_url), code=302)
    return redirect(urlChange(new_url), code=302)


@app.route('/<path:page>')
def anypage(page):
    print redirect('{new_url}/{page}'.format(page=page, new_url=urlChange(new_url)),
                    code=302)
    return redirect('{new_url}/{page}'.format(page=page, new_url=urlChange(new_url)),
                    code=302)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# 1. use regexes to parse your url, find the z, x, and y, and add +1s
# 2. come up with a new url structure that maybe has the z, x, and y as query string parameters or path parameters and have flask interpret those to add +1s and ask tmobile for the tile
