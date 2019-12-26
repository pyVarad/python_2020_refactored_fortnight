import pika as pk


class Transport:
    def __init__ (self, host, port):
        self.host = host
        self.port = port

    def producer(self, exchange, queue):
        params = pk.URLParameters('amqp://guest:guest@transport:5672/')
        params.socket_timeout = 5
        connection = pk.BlockingConnection(params)
        channel = connection.channel()
        channel.basic_publish(exchange='userAdmin', routing_key='userAdminRequest', body='User information')


    def consumer(self):
        print("Consumer")