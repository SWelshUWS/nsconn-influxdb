# CLI - pip install influxdb
from influxdb import InfluxDBClient
from datetime import datetime
import socket
import json

def influxFormat(obj):

  data = {}

  pythonObj = json.loads(obj)
  #access elements in the object
 # if "raweegpower" in pythonObj:
  #  rawwav = pythonObj['raweegpower']
   #
    #data = {
     # "measurement": "raweegpower",
      #"time": datetime.now(),
      #"fields": {
       #   'rawwav': rawwav
      #}
    #}

  if "attention" in pythonObj:
    data = {
      "measurement": "eSense",
      "time": datetime.now(),
      "fields": {
          'attention': pythonObj['attention']
      }
    }
  elif "meditation" in pythonObj:
    data = {
      "measurement": "eSense",
      "time": datetime.now(),
      "fields": {
          'meditation': pythonObj['meditation']
      }
    }
  elif "poorsignal" in pythonObj:
    data = {
      "measurement": 'poorsignal',
      "time": datetime.now(),
      "fields": {
          'poorsignal': pythonObj['poorsignal']
      }
    }
  elif "asiceegpower" in pythonObj:
    data = {
      "measurement": "asiceegpower",
      "time": datetime.now(),
      "fields": {
        "delta": pythonObj['asiceegpower'][0],
        "theta": pythonObj['asiceegpower'][1],
        "lowalpha": pythonObj['asiceegpower'][2],
        "highalpha": pythonObj['asiceegpower'][3],
        "lowbeta": pythonObj['asiceegpower'][4],
        "highbeta": pythonObj['asiceegpower'][5],
        "lowgamma": pythonObj['asiceegpower'][6],
        "highgamma": pythonObj['asiceegpower'][7]
        }
      }
  return data

# connect to nsconn
s = socket.socket()
self = socket.gethostname()
port = 9291
s.connect((self,port))
outString = []

# make sure database exists before parsing objects
client = InfluxDBClient('localhost', 8086, 'yourname', 'yourpass', 'nsconn')
client.switch_database('nsconn')


pCount = 0
jObj = ""
while True:
  byte = s.recv(1)
  if byte.decode("utf-8") == '{':
    pCount = pCount+1
    jObj = jObj + byte.decode("utf-8")
  elif byte.decode("utf-8") == '}':
    pCount = pCount-1
    jObj = jObj + byte.decode("utf-8")
    if pCount == 0:
      printo = influxFormat(jObj)
      print(printo)
      outString.append(printo)
      client.write_points(outString)
      jObj = ""
      continue
  else:
    jObj = jObj + byte.decode("utf-8")




