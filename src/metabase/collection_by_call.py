import json
from src.sessions import user_agent, session_2

def collect_information(call_id: str):
    URL = 'http://10.17.19.182:3001/api/dashboard/2/dashcard/13/card/13/query'
    
    payload = {
        "parameters": [
            {
                "type": "id",
                "value": [f"{call_id}"],
                "id": "b4564115"
            }
        ],
        "dashboard_id": 1
    }
    
    headers = {
        "accept" : "application/json",
        "content-type" : "application/json",
        "User-Agent": user_agent
    }
    
    json_payload = json.dumps(payload)
    res = session_2.post(URL, headers=headers, data=json_payload)
    
    if res.status_code == 202:
        res_json = res.json()
        data_json = res_json['data']['rows'][0]
        return data_json, call_id
    else:
        pass