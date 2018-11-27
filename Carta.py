"""
    Author: x 

using flatlib from :João Ventura   

"""
import sys
import datetime
from flatlib import aspects
from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

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
print("Sol em",sun.sign,sun.signlon)
print("Lua em",moon.sign,moon.signlon)
#print(sun)
#print(dir(sun))


