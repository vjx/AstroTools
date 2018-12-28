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
print (dados.date, dados.pos)
print()
# Build a chart for a date and location
chart = Chart(dados.date, dados.pos)


#print(dir(sun))
for obj in chart.objects:
         print(obj)

