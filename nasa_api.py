#!/usr/bin/env python3

from pprint import pprint
import requests
import shutil
import os.path
import json
from cfg_nasa import *

def api_ca():
     url = "https://api.nasa.gov/planetary/apod?api_key={0}".format(api_key)
     print(url)
     r = requests.get(url)
     response = r.json()
     high_def_APOD = response#['hdurl']
     pprint(high_def_APOD)
     return high_def_APOD
    
def photo_of_the_day(data):
    response = requests.get(data) #stream=True)
    with open(os.path.join('/Users/bobkoontz/Desktop','nasa.jpg'), 'wb') as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)

def main():
    data = api_ca()
    photo_of_the_day(data)

if __name__ == "__main__":
    main()

