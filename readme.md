# Twitter Bot Special for JKT48

1. Requirements
- Python 2.7.6 or later
- Twython
``` pip install twython ```

2. Configure
- Goto https://apps.twitter.com and create your app
- More detail goto http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/
- Edit settings.py
	```
	APP_KEY = Consumer Key (API Key)
	APP_SECRET = Consumer Secret (API Secret)
	OAUTH_TOKEN = Access Token
	OAUTH_TOKEN_SECRET = Access Token Secret
	```
3. Run
	```nohup python twitter.py > out 2>&1 &```

