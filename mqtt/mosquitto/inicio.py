import time
import subprocess

intervalo = 300
while True:
    print("hola")
    subprocess.run(['python3', 'mqtt.py'])
    time.sleep(intervalo)
