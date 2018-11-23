"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for handling 
    aspects.

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

# Retrieve the Sun and Moon 
sun = chart.get(const.SUN)
moon = chart.get(const.MOON)

# Get the aspect
aspect = aspects.getAspect(sun, moon, const.MAJOR_ASPECTS)
print(sun)
print(moon)

print(aspect)     # <Moon Sun 90 Applicative +00:24:30>
