from multiprocessing.process import Process
import time
import redis
import socket

sock = 0
def sub(myredis, channel):
    global sock

    pubsub = myredis.pubsub()
    pubsub.subscribe([channel])
    for item in pubsub.listen():
        print '%s : %s' % (channel, item['data'])
        sock.send(str(item['data'])+'\r\n')

if __name__ == '__main__':
    sock = socket.create_connection(('localhost', 5250))
    myredis = redis.Redis()
    Process(target=sub, args=(myredis,'channel_play')).start()