#!/usr/bin/env python

import json
import urllib2
import random
import sys

keyfilename = 'meetup.key'
key = ''

try:
	with open(keyfilename, 'r') as keyfile:
		key = keyfile.read().strip()
except IOError:
	print "Error: Cannot locate Meetup API key file."
	print
	print "1) Go to http://www.meetup.com/meetup_api/key/"
	print "2) Copy your API key into your clipboard"
	print "3) Paste your API key into a file called '" + keyfilename + "' in the current directory"
	sys.exit()

if len(sys.argv) < 2:
    sys.exit('Usage: %s <event-id> [winner-count]' % sys.argv[0])

event_id = sys.argv[1]

winners = 1
if len(sys.argv) == 3:
	winners = int(sys.argv[2])

url = 'http://www.meetup.com/2/rsvps?key=' + key + '&rsvp=yes&event_id=' + event_id
data = json.load(urllib2.urlopen(url))
rsvps = data['results']

if len(rsvps) > 0:
	for x in range (1, min(winners + 1, len(rsvps))):
		rsvp = rsvps.pop(random.randint(0, len(rsvps) - 1))
		print "%2d: %s" % (x, rsvp['member']['name'])
else:
	print 'No winners'
