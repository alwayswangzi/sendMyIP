#!/usr/bin/python
# coding=utf-8

import pycurl, json, os, sys, time
from StringIO import StringIO

#setup InstaPush variables

# set this to Application ID from Instapush
appID = "5826bf64a4c48ad384b54902"

# set this to the Application Secret from Instapush
appSecret = "ad55eaf6f79ccea20aa10e331a5ec343"

# leave this set to DoorAlert unless you named your event something different in Instapush
pushEvent = "sendIP"

#=====================loop begin============================

count = 10

time.sleep(30)

while True:
	
	p = os.popen("ping -c 1 www.baidu.com | awk \'/packet loss/{print $6}\'",'r')
	POCKET_LOSS = p.read()

#	print "count: ", count, ", pocket loss: ", POCKET_LOSS
	count = count - 1
	if count == 0:
#		print "Error! Can't connect Internet, program exit\n"
		sys.exit(0)

	if POCKET_LOSS == "0%\n":	
		p = os.popen("ifconfig eth0 | sed -n \"2,2p\" | awk \'{print substr($2,1)}\'",'r')
		ETH0_IP_ADDR = p.read()
		pushMessage = "Raspberry Pi, eth0 IP " + ETH0_IP_ADDR
		break
		
	time.sleep(10)

#=============================================================

# use StringIO to capture the response from our push API call
buffer = StringIO()

# use Curl to post to the Instapush API
c = pycurl.Curl()

# set Instapush API URL
c.setopt(c.URL, 'https://api.instapush.im/v1/post')

# setup custom headers for authentication variables and content type
c.setopt(c.HTTPHEADER, ['x-instapush-appid: ' + appID, 'x-instapush-appsecret: ' + appSecret, 'Content-Type: application/json'])

# create a dictionary structure for the JSON data to post to Instapush
json_fields = {}

# setup JSON values
json_fields['event']=pushEvent
json_fields['trackers'] = {}
json_fields['trackers']['message']=pushMessage

postfields = json.dumps(json_fields)

# make sure to send the JSON with post
c.setopt(c.POSTFIELDS, postfields)

# set this so we can capture the resposne in our buffer
c.setopt(c.WRITEFUNCTION, buffer.write)

# uncomment to see the post that is sent
#c.setopt(c.VERBOSE, True)

c.perform()

# capture the response from the server
body= buffer.getvalue()

# print the response
#print(body)

# reset the buffer
buffer.truncate(0)
buffer.seek(0)

# cleanup
c.close()
