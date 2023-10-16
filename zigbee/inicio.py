import time
import subprocess

intervalo = 300
while True:
    print("hola")
    subprocess.run(['python3', 'xbee_mqtt.py'])
    time.sleep(intervalo)
