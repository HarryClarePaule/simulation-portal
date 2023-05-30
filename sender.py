import requests
from datetime import datetime
import socket
import os
import psutil

login = os.getlogin()
hostname = socket.gethostname()
#hostname = "NA-DT-07"
comsol_running = "comsol.exe" in (i.name() for i in psutil.process_iter())

now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M")

BASE = 'http://127.0.0.1:5000/'

response = requests.post(BASE + hostname, json={"availability": "AVAILABLE", "user_online": "Harry", "comsol_online": comsol_running, "time": dt_string})
print(response.json())
print(login, hostname, comsol_running, dt_string)