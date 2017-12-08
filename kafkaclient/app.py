from flask import Flask, request, Response
from pykafka import KafkaClient
app = Flask(__name__)
client = KafkaClient(zookeeper_hosts="zookeeper")
# create topics                                                                                                                                   
topics = ['deliveries', 'updates']
for item in topics:
    client.topics[item]
@app.route("/kafka", methods=['POST'])
def write_message():
    payload = request.get_json()
    req_topic = payload['topic'].encode('utf-8')
    req_message = payload['message'].encode('utf-8')
    if req_topic in client.topics:
        topic = client.topics[req_topic]
        with topic.get_sync_producer(max_queued_messages=0, linger_ms=0) as producer:
            producer.produce(req_message)
        return Response(response='{"msg": "Success"}', status=200, mimetype="application/json")
    else:
        return Response(response='{"msg": "Invalid Topic"}', status=400, mimetype="application/json")
