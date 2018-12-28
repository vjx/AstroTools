import sys
import datetime
from flatlib import aspects
from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos

if len(sys.argv) <= 1:
    data = datetime.datetime.utcnow()
    d = data.strftime('%Y/%m/%d')
    h = data.strftime('%H:%M:%S')
    date = Datetime(d,h)
    pos = GeoPos('38n72', '9w13')

elif sys.argv[1] == "x":
    date = Datetime('1981/05/22', '08:00', '+00:00')
    pos = GeoPos('38n72', '9w00')

    
else:
    date = Datetime('2015/03/13', '17:00', '+00:00')
    pos = GeoPos('38n32', '8w54')




