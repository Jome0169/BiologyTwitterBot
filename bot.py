#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
import argv
import json  


def getAPI():
    CONSUMER_KEY = 'Wz7Enqk9Xw6tQI3D6MJrWE4cH'#keep the quotes, replace this with your consumer
    CONSUMER_SECRET = 'MGlyAlHDHsLgETZ6DR5XaHyahPaJ7kPpm0KP1O9pMuF1lbXSat'#keep the quotes, replace this with your
    ACCESS_KEY = '708117539478351873-DRfBWY0nZtENf3YHQDHbhqYaswSdwIA'#keep the quotes, replace this with your access token
    ACCESS_SECRET = 'tRN0gaIKsJOTE0MThL5UFO6NoMhwM6eySWETBg8JXG647'#keep the quotes, replace this with your access
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api




