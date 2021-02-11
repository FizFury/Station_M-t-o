import urequests as requests
from Lib import get_measures
import time
import ujson

sonde_id = 1

#res = requests.get(url='http://192.168.8.248:5000/print_data')
#print(res.text)
i = 0
while True:
    i += 1
    print("essaie"+str(i))
    time.sleep(5)#284
    data = get_measures()
    data.update({'sonde_id': str(sonde_id)})
    data = ujson.dumps(data)
    print(data)

    request_url = 'http://192.168.8.248:5000/insert_data'
    res = requests.post(request_url, headers = {'content-type': 'application/json'}, data = data).json()




   





