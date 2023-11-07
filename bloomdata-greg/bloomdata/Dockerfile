# Dockerfile

FROM debian

### So logging/io works reliably w/Docker
ENV PYTHONUNBUFFERED=1
### UTF Python issue for Click package (pipenv dependency)
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
### Need to explicitly set this so `pipenv shell` works
ENV SHELL=/bin/bash

### Basic Python dev dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3-pip curl -y

### Install via pip or pipenv:
RUN pip3 install pandas numpy