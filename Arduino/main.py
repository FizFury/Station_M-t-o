import urequests as requests
from machine import I2C, Pin
from lcdi2c import LCDI2C
from Lib import get_measures
from time import sleep
import time
import ujson

sonde_id = 1

#res = requests.get(url='http://192.168.8.248:5000/print_data')
#print(res.text)
i = 0
res = 0
i2c = I2C(Pin(0), Pin(2))
lcd = LCDI2C( i2c, cols=16, rows=2 )
lcd.backlight()
while True:
    print("début de boucle")
    i += 1
    data = get_measures()
    if res == 200:
        lcd.clear()
        lcd.set_cursor((0,0))
        lcd.print("connexion")
        lcd.set_cursor((0,1))
        lcd.print("reussie")
        time.sleep(5)
        lcd.clear()
        temperature = str(data['temperature'])
        humidite = str(data['humidite'])
        lcd.set_cursor((0,0))
        lcd.print("Temperature:"+temperature+"C")
        lcd.set_cursor((0,1))
        lcd.print("Humidite:"+humidite+"%")
    else:
        lcd.clear()
        lcd.set_cursor((0,0))
        lcd.print("probleme")
        lcd.set_cursor((0,1))
        lcd.print("connexion")
    
    print("essaie"+str(i))
    
    data.update({'sonde_id': str(sonde_id)})
    data = ujson.dumps(data)
    print(data)

    request_url = 'http://192.168.8.248:5000/insert_data'
    try:
        res = requests.post(request_url, headers = {'content-type': 'application/json'}, data = data).json()
        print(res)
    except:
        print("API KO")
    print("fin de boucle")
    time.sleep(2)#284