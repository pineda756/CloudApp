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