"""
    Author: x 

using flatlib from :João Ventura   

"""
import dados
import sys
import datetime
from flatlib import aspects
from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos


#print ('Argument List:', str(sys.argv))
print()
print (dados.date, dados.pos)
print()
# Build a chart for a date and location
#chart = Chart(dados.date, dados.pos)
chart = Chart(dados.date, dados.pos, IDs=const.LIST_OBJECTS)
house1 = chart.get(const.HOUSE1)

#print(dir(sun))
for obj in chart.objects:
         print(obj)
         #print(chart.getObject(getattr(const, obj)))



print()
print(house1)
print(house1.gender())
