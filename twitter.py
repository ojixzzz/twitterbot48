#!/usr/bin/env python

import time, sys
from twython import Twython, TwythonError
from settings import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET

twitter = Twython(
				APP_KEY, 
				APP_SECRET, 
				OAUTH_TOKEN, 
				OAUTH_TOKEN_SECRET
				)
		
statuslama = ''
while True:
	try:
		search_results = twitter.search(q='#VoteJKT48ID', count=1)
	except TwythonError as e:
		print e
		
	for tweet in search_results['statuses']:
		statusnya = 'RT @%s : %s' % (tweet['user']['screen_name'].encode('utf-8'), 
					tweet['text'].encode('utf-8'))
		if len(statusnya) < 140 and statuslama != statusnya:
			try:
				twitter.update_status(status=statusnya)
			except TwythonError as e:
				print statuslama
			statuslama = statusnya
	time.sleep(3)
