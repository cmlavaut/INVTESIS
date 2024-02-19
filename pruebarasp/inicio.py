import time
import subprocess

intervalo = 30
while True:
    subprocess.run(['python3', 'recibir_xbee.py'])
    time.sleep(intervalo)
