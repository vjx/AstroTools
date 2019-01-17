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
    date = Datetime('1981/05/22', 
'08:00', '+01:00')
    pos = GeoPos('38n72', '9w00')

elif sys.argv[1] == "sof":
    date = Datetime('2015/04/21', '16:56', '+00:00')
    pos = GeoPos('38n72', '9w00')

elif sys.argv[1] == "leo":
    date = Datetime('2012/10/13', '19:26', '+00:00')
    pos = GeoPos('38n72', '9w00')

elif sys.argv[1] == "ram":
    date = Datetime('1984/07/14', '06:00', '+00:00')
    pos = GeoPos('41n16', '8w63')

elif sys.argv[1] == "hitler":
    date = Datetime('1889/04/20', '18:30', '+00:00')
    pos = GeoPos('40n15', '13e03')

    
else:
    print('Erro: Nome nao encontrado')
    date = Datetime('0/01/1', '00:00', '+00:00')
    pos = GeoPos('38n32', '8w54')




