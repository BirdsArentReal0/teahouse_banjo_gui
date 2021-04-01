import teahaz
import requests
import json

global TEAHAZ_LINK
TEAHAZ_LINK = "https://teahaz.co.uk"


global SESSION
SESSION = requests.Session()


def login(x):
    url = TEAHAZ_LINK+"/login/"+x["chatroom"]
    data = {"username":x["username"],"password":x["password"]} 
    server_res = SESSION.post(url = url,json = data)
    if server_res.status_code != 200:
        print("nem az úgy nem lesz jó: "+server_res.text)
        return False
    else:
        print("az úgy jo lesz")
        return True

def get_messagees(x):
    url = TEAHAZ_LINK+"/api/v0/message/"+x["chatroom"]
    data = {"username":x["username"],"time":"2"}
    server_res = SESSION.get(url=url,headers=data)
    if server_res.status_code != 200:
        print("nem az úgy nem lesz jó: "+server_res.text)
    else:
        print("az úgy jo lesz")
        return server_res.text
    
if __name__ == "__main__":
    print("megbocsátok")
    with open("user_config.json", "r") as infile:
        x = json.loads(infile.read())
    x = x[0]
    if login(x):  
        print(get_messagees(x))