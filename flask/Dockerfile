FROM python:3.8

WORKDIR /home/app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5010
EXPOSE 1883
EXPOSE 9001
COPY . .

CMD [ "python", "main.py" ]

