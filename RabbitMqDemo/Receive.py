import pika, sys, os

#define the mail iteration loop waiting for queue data
def main():
    #create a connecton.
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # connect to the hello queue
    channel.queue_declare(queue='hello')
    channel.queue_purge(queue='hello')
    
    #define a call back metod to handle data on the quueue
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
 
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)