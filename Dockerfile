FROM ubuntu:18.04

RUN apt-get update && apt-get install -y build-essential python3 python3-dev python3-pip libmysqlclient-dev libsm6 libxext6 libxrender-dev locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

WORKDIR /home/

COPY . .

RUN  pip3 install -r /home/requirements.txt

#RUN python3 run.py create_db

ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]