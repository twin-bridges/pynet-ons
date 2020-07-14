#! /usr/bin/env python
import os
from pprint import pprint
import requests


SLACK_TOKEN = os.environ["SLACK_TOKEN"]
SLACK_BASE_URL = "https://slack.com/api"
SLACK_BASE_HEADERS = {
    "content-type": "application/x-www-form-urlencoded",
    "Authorization": f"Bearer {SLACK_TOKEN}",
}


def get_selected_channel(channel_name):
    resp = requests.post(f"{SLACK_BASE_URL}/channels.list", headers=SLACK_BASE_HEADERS)
    channels = resp.json()["channels"]
    for channel in channels:
        if channel["name"] == channel_name:
            return channel["id"]


def send_message(channel_id, message):
    msg_data = {}
    msg_data["channel"] = channel_id
    msg_data["text"] = message
    resp = requests.post(
        f"{SLACK_BASE_URL}/chat.postMessage", data=msg_data, headers=SLACK_BASE_HEADERS
    )
    resp_json = resp.json()
    resp_info = {}
    resp_info["status_code"] = resp.status_code
    resp_info["user"] = resp_json["message"]["username"]
    resp_info["timestamp"] = resp_json["message"]["ts"]
    return resp_info


def main():
    channel_id = get_selected_channel("random")
    resp_info = send_message(channel_id, "racecar")
    pprint(resp_info)


if __name__ == "__main__":
    main()
