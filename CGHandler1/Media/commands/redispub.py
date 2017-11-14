from multiprocessing.process import Process
import time
import redis

def pub_play(cmd):
    r = redis.Redis()
    r.publish('channel_play', cmd)

