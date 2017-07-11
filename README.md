# T-Mobile Spectrum Map Tile Redirect Service

This is a flask app that redirect T-Mobiile Map services which is essentially off by 1 in the XYZ system. 

So a normal `maps.com/0/0/0.png` for Spectrum is  `http://maps.t-mobile.com/TMo_TechLTE_Map/1/1:1/tile.png`

[Spectrum Spatial Developer Guide](http://support.pb.com/help/spectrum/9.0/pdf/en/Spectrum_9.0_SpatialDeveloperGuide.pdf)




`http://maps.t-mobile.com/TMo_TechLTE_Map/6/5:11/tile.png`
![http://maps.t-mobile.com/TMo_TechLTE_Map/6/5:11/tile.png](http://maps.t-mobile.com/TMo_TechLTE_Map/6/5:11/tile.png)

Served from this redirect Flask app:

`http://maps.t-mobile.com/TMo_TechLTE_Map/5/4:10/tile.png`
![https://tmobilespectrummaptile.cartodb.io/5/4/10.png](https://tmobilespectrummaptile.cartodb.io/5/4/10.png)


