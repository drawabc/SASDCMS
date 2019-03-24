import tweepy

class TwitterAPI:
    def __init__(self):
        self.ACCESS_TOKEN="1104719780274044928-ByXaoz9Xg8K4QG4gP3myQFsMaAmnO0"
        self.ACCESS_TOKEN_SECRET="DpOvbtp18gzOrOe0fmQIXdDoRPDOVd2sUVLIhL6De9IfU"
        self.CONSUMER_SECRET="HyTiL120kBPz2f3QT4NKJB39Gv2ADrafTwNl80jgVKIekPCcQY"
        self.CONSUMER_KEY="nNfgA6tyseTN3FL9Gf2ovyHB9"
    def sendTweet(self,message):
        try:
            consumer_secret=self.CONSUMER_SECRET
            consumer_key=self.CONSUMER_KEY
            access_token = self.ACCESS_TOKEN
            access_token_secret = self.ACCESS_TOKEN_SECRET

            auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
            auth.set_access_token(access_token,access_token_secret)

            api=tweepy.API(auth)
            api.update_status(message)
            return "Tweet successfully sent"
        except:
            return "Tweet failed to send"
        
if __name__ == '__main__':
    print(TwitterAPI().sendTweet("This is a test Message"))
