import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import time

access_token = "1680459529-RIDTJRZQY9BJObNSIS2BisB7EBq8QYTKIDk79iO"
access_secret = "439aSp7DJwtWswVe0heTeOZw2LmqoTuqcca2FC057Kp9n"
consumer_key = "mwoKo3SDyUL2iWooHrVCTa87V"
consumer_secret = "B1yCBPMrQoS2kMDvUaLvad2LBKgoa16mmuGF7x6oVmL39cVkZC"

tracker = str(input("Enter term to be tracked: "))
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
write_file = tracker + '.json'


api = tweepy.API(auth)


class MyListener(StreamListener):

  def on_data(self, data):
    try:
      with open(write_file, 'a') as f:
        f.write(data)
        return True
    except BaseException as e:
      print("EXCEPTION")
    return True

  def on_error(self, status):
    print(status)
    return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=[tracker])
