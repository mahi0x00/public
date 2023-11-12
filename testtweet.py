#Important note
#Before running this for the first time run "pip3 install tweepy"

import tweepy
consumer_key = "Put your consumer key here"
consumer_secret = "Put your consumer secret here"
access_token = "Put your access token key here"
access_token_secret = "Put your access token secret here"
text = "Write tweet text here"


def main():
    client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret)
    print(client)

    client.create_tweet(text=text)
    
if __name__ == "__main__":
    main()
