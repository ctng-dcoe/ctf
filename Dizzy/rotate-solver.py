import requests
import time
#from bs4 import BeautifulSoup

flag = ''
def solve():
    rq = requests.get("http://localhost:8081")
    r = rq.content
    return r


if __name__ == '__main__':
    # r = requests.get("http://localhost:8080")
    # #soup = BeautifulSoup(r, )
    # print(r.content)

    while True:
        flag += solve().decode()
        time.sleep(0.5)
        print(flag)
