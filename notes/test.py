
inURL = 'http://maps.t-mobile.com/TMo_TechLTE_Map/0/0:0/tile.png'

inURL = 'http://maps.t-mobile.com/TMo_TechLTE_Map/6/5:11/tile.png'

inURL = 'http://tmobilespectrummaptile.cartodb.io/5/4/10.png'
inURL = 'localhost:5000/5/4/10.png'


def urlChange(inURL):
    slashes = inURL.count('/')
    z = int(inURL.split('/')[slashes - 2].split('/')[0])
    x = int(inURL.split('/')[slashes - 1].split('/')[0])
    y = int(inURL.split('/')[slashes].split('.png')[0])
    z = z + 1
    x = x + 1
    y = y + 1
    newURL = 'http://maps.t-mobile.com/TMo_TechLTE_Map/'+str(z)+'/'+str(x)+':'+str(y)+'/tile.png'
    return newURL

urlChange(inURL)
