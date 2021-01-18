import requests
import pandas as pd
import csv
import itertools

response = requests.get("https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Environment_WebMercator/MapServer/45/query?where=1%3D1&outFields=*&outSR=4326&f=json")
dataDict = response.json()
with open("rawData.csv", "wb") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(dataDict.keys())
    writer.writerows(itertools.izip_longest(*dataDict.values()))
