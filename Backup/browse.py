import requests
from time import sleep
import random

safe = ["google.com","yahoo.com","corp.com","ctcyber.io"]


while True:
    try:
        x = requests.get("http://" + random.choice(safe))
        print(x.text)
        sleep(3)
    except:
        pass