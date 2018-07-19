import tweepy
from textblob import TextBlob

stringSentiment = ''
consumer_key = "OBnmggkXwHEApPs9shSCLnRPz"
consumer_secret = "WMI7StYq84TXCGu0sn5PSpahXhwM5YBKEjL1zVmZNDNNHIL8ci"

access_token = "841695068092260353-lOD3pOxm2Md5sxVc26ZOPqd0ogzsvz7"
access_token_secret = "sNWyUHmz8kFOrKMD9G12V10ZilxDSAKwGSElNd7YFMzoL"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

query = "String to  be Searched"
public_tweet = api.search(query)
file = open("file.txt", "a")
file.write('Polarity < 0 represents negative sentiments, 0 represents neutral sentiments and polarity > 0 but less than 1 represents positive sentiments...\n\n')
for tweet in public_tweet :
	encodedTweet = tweet.text.encode('utf-8')
	file.write(encodedTweet+'\n')
	print(tweet.text)
	
	analysis = TextBlob(tweet.text)
	encodedAnalysisString = str(analysis.sentiment)
	file.write(encodedAnalysisString+'\n\n\n\n')
	print(analysis.sentiment)
	
file.close()
