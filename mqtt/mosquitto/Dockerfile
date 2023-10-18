FROM python:3.8

WORKDIR /home
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY ./inicio.py /home
COPY ./credenciales.json /home
COPY ./mqtt.py /home
RUN mkdir /home/database

CMD [ "python3", "inicio.py" ]


