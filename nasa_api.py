#!/usr/bin/env python3

from pprint import pprint
import requests
import shutil
import os.path
import json
from cfg_nasa import *

def api_call_jsons():
     url = "https://api.nasa.gov/planetary/apod?api_key={0}".format(api_key)
     r = requests.get(url)
     response = r.json()
     high_def_APOD = response.get('hdurl')
     title_APOD = response.get('title')
     return {'pic': high_def_APOD, 'titles': title_APOD}
    
def get_photo_of_the_day(data):
    titles_value = data.get('titles')
    pic_value = data.get('pic')
    response = requests.get((pic_value), stream=True)
    with open(os.path.join('/Users/bobkoontz/Pictures/nasa/','{0}.jpg').format(titles_value), 'wb') as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)

def main():
    data = api_call_jsons()
    get_photo_of_the_day(data)

if __name__ == "__main__":
    main()