import time
import subprocess

intervalo = 180
while True:
    print("hola")
    subprocess.run(['python3', 'mqtt.py'])
    time.sleep(intervalo)
