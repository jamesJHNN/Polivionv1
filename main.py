#!/usr/bin/env python
# -*- coding: utf-8 -*-u

"""
Purpose : Listening to stream api and compute some sentiment measure.
"""

import tweepy
import json
from pymongo import MongoClient
from helpers import authentify, write_to_json_line


class MyStreamListener(tweepy.StreamListener):
    """
    tweepy.StreamListener is a class provided by tweepy used to access
    the Twitter Streaming API. It allows us to retrieve tweets in real time.
    """

    def __init__(self, save_to_mongo=False, save_to_json=True, json_file_path='polivion.json'):
        self.save_to_mongo = save_to_mongo
        self.save_to_json = save_to_json
        self.json_file_path = json_file_path
        if self.save_to_mongo :
            self.client = MongoClient('localhost', 27017)
            # Use cooldb database
            self.db = self.client.tweetstream
            self.collection_name = "polivion"



    def on_connect(self):
        """Called when the connection is made"""
        print("You're connected to the streaming server.")

    def on_error(self, status_code):
        """This is called when an error occurs"""
        print('Error: ' + repr(status_code))
        return False

    def on_data(self, data):
        """This will be called each time we receive stream data"""
        # Decode JSON
        datajson = json.loads(data)

        # print
        #print(datajson['text'])
        if 'text' in datajson.keys():
            if "polivion" in datajson['text'].lower():
                rating=[int(s) for s in datajson['text'].split() if s.isdigit()][0]
                print("this user {} rated {}".format(datajson['user']['screen_name'],rating))
                #save to database
#                if self.save_to_mongo:            
#                    self.db[self.collection_name].insert(datajson)
                #save to jspon
                if self.save_to_json:
                    write_to_json_line(data, self.json_file_path)





if __name__ == "__main__":
#    ci, cs = get_consumer_tokens()
#    aci, acs = get_access_tokens()
    auth = authentify(ci, cs, aci, acs)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    my_stream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())
    my_stream.filter(track=["polivion"], languages=['en'])
    
    
    
    
    
    
        
