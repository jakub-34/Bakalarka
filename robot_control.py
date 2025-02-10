import requests
import sys
from poses import Pose


url = "http://192.168.104.100:5012"

velocity = 50
payload = 0


def start():
    start_url = url + "/state/start"

    data = {
        "orientation": {
            "w": 1,
            "x": 0,
            "y": 0,
            "z": 0
        },
        "position": {
            "x": 0,
            "y": 0,
            "z": 0
        }
    }

    response = requests.put(start_url, json=data)

    if response.status_code == 200 or response.status_code == 204:
        return
    
    else:
        print("Error starting robot", file=sys.stderr)
        sys.exit(1)


def put_pose(position: Pose):
    pose_url = url + "/eef/pose"

    params = {
        "velocity": velocity,
        "payload": payload
    }

    data = position.to_dict()

    response = requests.put(pose_url, params=params, json=data)

    if response.status_code == 200 or response.status_code == 204:
        return

    else:
        print("Error setting pose", file=sys.stderr)
        sys.exit(1)