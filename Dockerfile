FROM apachepulsar/pulsar:2.6.0

COPY ./pulsar_consumer.py /root/pulsar_consumer.py
COPY ./pulsar_producer.py /root/pulsar_producer.py
