from flask import Flask, redirect


app = Flask(__name__)

new_url = 'http://maps.t-mobile.com/TMo_TechLTE_Map'


def urlChange(inURL):
    slashes = inURL.count('/')
    z = int(inURL.split('/')[slashes - 2].split('/')[0])
    x = int(inURL.split('/')[slashes - 1].split('/')[0])
    y = int(inURL.split('/')[slashes].split('.png')[0])
    z = z + 1
    x = x + 1
    y = y + 1
    newURL = str(z)+'/'+str(x)+':'+str(y)+'/tile.png'
    return newURL


@app.route('/')
def root():
    return redirect(urlChange(new_url), code=302)


@app.route('/<path:page>')
def anypage(page):
    return redirect('{new_url}/{page}'.format(page=urlChange(page), new_url=new_url),
                    code=302)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
