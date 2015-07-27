#!/usr/bin/python
'''
Query runlevel information for system services (like chkconfig on CentOS/Redhat)
'''

import os
import re


def getServiceStatus(service,rcDir):
        pat = re.compile('S[0-9]{2}'+service)
        serviceList = ','.join(os.listdir(rcDir))
        if service in serviceList:
                if re.search(pat,serviceList):
                        return 'on'
                else:
                        return 'off'
        else:
                return 'off'


initDir = '/etc/init.d/'
services = {}
for service in os.listdir(initDir):
	for runlevel in range(7):
		service = service.strip()
		rcDir = '/etc/rc'+str(runlevel)+'.d'
		status = getServiceStatus(service,rcDir)
		if services.has_key(service):
			services[service][runlevel] = status
		else:
			services[service] = {runlevel:status}


#Output the result
for (service,status) in services.items():
	print	'%-*s %s' % (20,service,status)

 
