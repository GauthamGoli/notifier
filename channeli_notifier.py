from pync import Notifier
from datetime import datetime
import requests
import time

def get_notice_time(time_str):
	return datetime.strptime(time_str,'%Y-%m-%dT%H:%M:%S')

while True:
	r = requests.get('https://channeli.in/notices/list_notices/new/All/All/0/0/0/')

	try:
		fp = open('last.txt','r+')
		fr = fp.readlines()
	except:
		fp = open('last.txt', 'w')
		fr = []
	last_notice_time = get_notice_time(fr[0]) if fr else None
	latest_notice_response = r.json()[0]
	latest_notice_time = get_notice_time(latest_notice_response["datetime_modified"])
	if last_notice_time is None or last_notice_time<latest_notice_time:
		Notifier.notify(latest_notice_response["subject"],title=latest_notice_response["main_category"])
		fp.write(latest_notice_response["datetime_modified"])
	time.sleep(30)


