from multiprocessing import connection
from re import M
from statistics import median_grouped
import sys
import pika
import json

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

iterCnt = 1
argumentList = sys.argv[1:]
# if argument and it is numeric set the iteration
if(n > 1):
    cnt = argumentList[0]
    if (cnt.isnumeric()):
        iterCnt =  int(cnt)

#create a jason like data array
data = {"Proportional": 1.7, "Integral": 2.5, "Derivative": 0.8, "TimeOut": 15}

#put it in json format
json_data = json.dumps(data)

#create a connecton.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# connect to the hello queue
channel.queue_declare(queue='hello')

# clear out the queue
channel.queue_purge(queue='hello')

for x in range(0, iterCnt):
        channel.basic_publish(exchange='',routing_key='hello', body=json_data)

connection.close()

