"""
    Author: x 

using flatlib from :João Ventura
    
    
    

"""
import datetime
from flatlib import aspects
from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos


# Build a chart for a date and location
data = datetime.datetime.utcnow()
d = data.strftime('%Y/%m/%d')
h = data.strftime('%H:%M:%S')
date = Datetime(d,h)

pos = GeoPos('38n72', '9w13')
chart = Chart(date, pos)

for obj in chart.objects:
     print(obj)

