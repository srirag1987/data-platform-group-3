FROM tabulario/spark-iceberg:latest

# Install ncat and other dependencies
USER root
RUN apt-get update && apt-get install -y ncat

# Install Kafka
# You can replace the URL with the desired Kafka version
RUN wget -qO- https://downloads.apache.org/kafka/3.0.0/kafka_2.13-3.0.0.tgz | tar xvz -C /opt && \
    ln -s /opt/kafka_2.13-3.0.0 /opt/kafka

USER iceberg