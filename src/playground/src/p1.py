from ops_tracker_cvache import ops
import requests
import json

def main():
    # tracker = ops.ops_tracker(id="test1", tracker_address="http://127.0.0.1:8000/tracker")
    # tracker.start()
    payload = {
            "id": "123",
            "project": "proj",
            "level": "START",
            "timestamp": "1234"
        }
    r = requests.put(url="http://127.0.0.1:8000/tracker", data=json.dumps(payload))
    print(r.text)
    return

if __name__ == "__main__":
    main()

    