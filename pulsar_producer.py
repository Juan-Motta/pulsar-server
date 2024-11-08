import pulsar
import time
import sys

client = pulsar.Client('pulsar://host.docker.internal:46650')
producer = client.create_producer('my-topic')

i = 0
while True:
    time.sleep(5)
    print("Message #{} sent".format(i))
    sys.stdout.flush()
    producer.send(('hello-pulsar-%d' % i).encode('utf-8'))
    i = i + 1

client.close()
