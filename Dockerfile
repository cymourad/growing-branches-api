# get the base image
FROM ubuntu:18.04

# make the base workdir where everyhting will go
WORKDIR /

# set up the environment with python
RUN apt-get update -y && apt-get install -y
RUN apt install -y python3.8
RUN apt install -y python3-pip
RUN apt install -y python-pip
RUN apt-get install -y python-mysqldb
RUN apt-get install -y python3-dev libmysqlclient-dev

# get the required packages and install them
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# get all the code
COPY . .

# set environment variables
ENV FLASK_APP=app.py
ENV ENV="PROD"

# expose a port to listen to the requests coming in
EXPOSE 8080

# start the app by running python3 app.py
CMD [ "python3", "app.py" ]