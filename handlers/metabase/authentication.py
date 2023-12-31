import json
from handlers.sessions import *
from handlers.database.database import db_auth, get_login, get_password, delete_login_and_password

def auth():
    while True:
        db_auth('metabase')
        login = get_login('metabase')
        password = get_password('metabase')

        URL = "http://10.17.19.182:3001/api/session"

        payload = json.dumps(
            {
                "username":login,
                "password":password
            }
        )

        headers = {
            "accept" : "application/json",
            "content-type" : "application/json",
            "User-Agent": user_agent
        }

        res = session_1.post(URL, headers=headers, data=payload, timeout=100)
        if res.status_code == 200:
            cookies_dict = [
                {
                    "domain" : key.domain, 
                    "name" : key.name, 
                    "path" : key.path, 
                    "value" : key.value
                }
                for key in session_1.cookies
            ]

            for cookies in cookies_dict:
                session_2.cookies.set(**cookies)
            break
        elif res.status_code == 401:
            print(f'[STATUS {res.status_code}] Invalid username or password')
            delete_login_and_password('metabase')
        else:
            pass

        print(f'[STATUS {res.status_code}] Metabase authentication.\n')