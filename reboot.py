#! /usr/bin/env python3

__author__ = 'JZ'
__homepage__ = 'https://github.com/Justsoos/reboot-tplink'

import requests

def reboot(host, user, password):
	try:
		url = 'http://{}/userRpm/SysRebootRpm.htm?Reboot='.format(host)
		headers = {'Referer': url}
		r = requests.get(url, headers=headers, auth=(user, password))
	except:
		raise

if __name__ == '__main__':

	host = '192.168.1.1'
	user = 'admin'
	password = '12345678'

	reboot(host, user, password)
