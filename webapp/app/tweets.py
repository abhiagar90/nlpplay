import tweepy

access_token = "3186412080-xPpfnGngI0wX1B54tztpC0FL15AHOwSRY7OOQ3x"
access_token_secret = "Ad42R8zxaHq1grJcP8L8afUSve3TGOAbi7O2gdQ82oTHf"
consumer_key = "9ff2ZYHKZhtAojUc6lBH5Nlsd"
consumer_secret = "ElXQ20E9sjlW1X2rWVQqSto1qUikhZX6gmAt0uZF0fNHSfo2z6"


def thisIsSparta(sparta_tag) :
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    dates = []
    texts = []


    tweets = tweepy.Cursor(api.search, q=sparta_tag).items(20)

    for tweet in tweets:
        #print tweet.created_at, tweet.text, "\n"
        dates.append(str(tweet.created_at))
        texts.append(tweet.text)

    print dates
    print texts

    return dates, texts

