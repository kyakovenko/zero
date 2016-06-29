# -*- coding: utf-8 -*-
__author__ = 'Kirill Yakovenko'
__email__ = 'kirill.yakovenko@gmail.com'

from db.session import session
from db.models import RoomMetrics

import dht
import time
dht.wiringPiSetup()

current_time = int(time.time())
while (True):
	data_lst = []
	start_time = (current_time / 60) * 60
	while current_time - start_time < 60:
		try:
			data_lst.append( dht.read_dht11() )
		except RuntimeError as exc:
			pass #print exc
		finally:
			time.sleep(5)
			current_time = int(time.time())
	# save data
	if data_lst:
		humidity, temperature = zip(*data_lst)
		metric = RoomMetrics(
			temperature=sum(map(float, temperature)) / len(temperature) + 0.5, 
			humidity=sum(map(float, humidity)) / len(humidity) + 0.5)
		session.add(metric)
		session.commit()
