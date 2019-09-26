# A super-simple qr-code server that exposes port 8080
#
FROM jfloff/alpine-python:latest-slim
MAINTAINER Justin Wood <Justin.Wood@rackspace.com>

# install pip and hello-world server requirements
RUN mkdir /app
COPY tes-engagement/app.py /app/app.py
COPY tes-engagement/requirements.txt /app/requirements.txt
COPY tes-engagement/dist /app/dist
RUN pip install -r /app/requirements.txt

# in case you'd prefer to use links, expose the port
EXPOSE 8080
ENTRYPOINT ["python", "/app/app.py"]
