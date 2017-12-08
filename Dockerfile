FROM ubuntu:xenial
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates curl software-proper
ties-common
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -
cs) stable"
RUN apt-get update
RUN apt-get install -y docker-ce
RUN curl -L https://github.com/docker/compose/releases/download/1.17.1/docker-compose-`uname -s`-
`uname -m` -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose
RUN mongod
RUN echo 'MAKING A DIRECTORY ???????????????????????????????'
RUN mkdir kafka && cd kafka




#FROM openjdk:8-jre
#ENV KAFKA_VERSION 1.0.0
#ENV KAFKA_SCALA_VERSION 2.11
#ENV KAFKA_ARCH "kafka_$KAFKA_SCALA_VERSION-$KAFKA_VERSION.tgz"
#ENV KAFKA_HOME /opt/kafka
#WORKDIR /opt
#RUN apt-get update
#RUN apt-get install -y jq
#RUN wget -O - $(wget -qO- https://www.apache.org/dyn/closer.cgi\?as_json\=1\&path\=/kafka/$KAFKA
_VERSION/$KAFKA_ARCH | jq --raw-output '.preferred')kafka/$KAFKA_VERSION/$KAFKA_ARCH | tar zxf -
#RUN mv /opt/kafka_$KAFKA_SCALA_VERSION-$KAFKA_VERSION $KAFKA_HOME
#RUN sed -i 's/zookeeper.connect=localhost:2181/zookeeper.connect=zookeeper:2181/g' /opt/kafka/co
nfig/server.properties
