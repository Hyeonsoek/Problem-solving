import requests

def start_api(url, auth):
    url = url + "/start"
    header = {
                'X-Auth-Token': auth,
                'Content-Type': 'application/json'
            }
    data = {'problem': 1}

    req = requests.post(url, headers=header, data=data)
    return req.json()

def locations_api(url, auth):
    url = url + "/locations"
    header = {
                'Authorization': auth,
                'Content-Type': 'application/json'
            }

    req = requests.get(url, headers=header)
    return req.json()

def trucks_api(url, auth):
    url = url + "/trucks"
    header = {
                'Authorization': auth,
                'Content-Type': 'application/json'
            }

    req = requests.post(url, headers=header)
    return req.json()

def trucks_api(url, auth, data):
    url = url + "/simulate"
    header = {
                'Authorization': auth,
                'Content-Type': 'application/json'
    }
    commands = {"commands":\
                    [{"truck_id": i, "command": j} for i, j in enumerate(data)]}

    req = requests.put(url, headers=header, data=commands)
    return req.json()

def score_api(url, auth):
    url = url + "/score"
    header = {
        'Authorization': auth,
        'Content-Type': 'application/json'
    }

    req = requests.get(url, headers=header)
    return req.json()