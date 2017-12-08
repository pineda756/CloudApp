FROM python:2.7-alpine3.6
COPY . /opt/chatserver/
WORKDIR /opt/chatserver
RUN apk add --no-cache g++ \
    && pip install -r requirements.txt
ENV FLASK_APP app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]