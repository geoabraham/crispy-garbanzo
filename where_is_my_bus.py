import urllib.request as req
from xml.etree.ElementTree import parse

u = req.urlopen(
    'http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
doc = parse(u)

for pt in doc.findall('.//pt'):
    print(pt.text)
