import requests
import json

data = {}

url = 'http://172.17.0.2:5000/results'

r = requests.post(url, json={'SepalLength': 0, 'SepalWidth': 0,
                             'PetalLength':  0, 'PetalWidth': 0})

mr = r.json()

with open('responsedata.json') as res:
    res_data = json.load(res)
    print(res_data['FlowerIrisResponseData'][mr])
