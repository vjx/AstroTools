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
lista = ['SUN', 'MOON', 'MERCURY', 'VENUS', 'MARS', 'JUPITER','SATURN','URANUS','NEPTUNE']
#print(dir(sun))
for obj in lista:
         #print(obj)
         print(chart.getObject(getattr(const, obj)))
print()
for obj in lista:
         for plan in lista:
            p1 = chart.get(getattr(const, obj))
            p2 = chart.get(getattr(const, plan))
            aspect = aspects.getAspect(p1, p2, const.MAJOR_ASPECTS)
            print (aspect)

print()
print(house1)
print(house1.gender())
