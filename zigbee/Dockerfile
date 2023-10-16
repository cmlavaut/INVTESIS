FROM python:3.8

WORKDIR /home/app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY ./inicio.py /home/app
COPY ./xbee_mqtt.py /home/app 
RUN mkdir /home/database

CMD [ "python3", "inicio.py" ]

