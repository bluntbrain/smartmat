 #!/usr/bin/env python
import time
import serial
import requests 
#from requests import async
#import requests_async as requests
from datetime import datetime
from dateutil.tz import *
import asyncio
import aiohttp
import json
urlToUpdateWeight = "https://datacaptureapi9380.azurewebsites.net/api/weights"
tz = 'Asia/Kolkata'
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter=0

async def main():
	while(1):
		x=ser.readline()
		x = x[2:-2]
		x_decoded = x.decode('utf-8')
		#print(x_decoded)
		if(x_decoded != None):
			try:
				x_float = float(x_decoded)
			except:
				print("An exception came")
				continue
			dateTimeObj = datetime.now()
			local = tzlocal()
			now = dateTimeObj.replace(tzinfo = local)
			timestampStr = dateTimeObj.strftime("%Y-%m-%dT%H:%M:%S")
			urlToUpdateWeightParams = {'Timestamp': timestampStr, 'Weight': x_float, 'Identifier': 'new_user'}
			data_json = json.dumps(urlToUpdateWeightParams)
			print(data_json)
			payload = {'json_payload': data_json}
			if(x_float > 60.0):
				async with aiohttp.ClientSession() as session:
					async with session.post(urlToUpdateWeight, data=data_json, headers={'Content-type': 'application/json'}) as response:
						print("Status:", response.status)
						html = await response.text()
						#print(html)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
