import json
from typing import List

import requests
from fetchers import BASE_URL, fetch_available_play_devices
from user_token import get_user_token

# TODO: Proper typing.
type Device = any


def play_track(track_id: str, context: str, device: Device) -> None:
    print(f"Will play track {track_id} on {device["name"]} in {context}")

    endpoint = "/me/player/play"
    user_token = get_user_token()

    r = requests.put(BASE_URL + endpoint, headers={
        "Authorization": f"Bearer {user_token}"
    },
        data=json.dumps({
            "context_uri": f"spotify:album:{context}",
            "device_id": device["id"],
        }))

    # TODO: Error handling
    assert r.ok, f"Error playing song -> status {r}, {r.json()["error"]["message"]}"

    print("Should now be playing.")


def get_available_devices() -> List[Device]:
    devices = fetch_available_play_devices()["devices"]
    return devices


def get_device_selection(devices: List[Device]) -> Device:
    for i, device in enumerate(devices):
        print(
            f"{i + 1} - {device["name"]} {device["is_active"] and "(*)" or ""}")

    idx = int(input("Which device? >")) - 1
    return devices[idx]


if __name__ == "__main__":
    test_track_id = "11Uoi1YLyhhhf8BgEpQ4dh"  # Take it! Take it! , by Yaeger
    test_context = "1jzob45PzKBXnvQ6fQpNTC"  # Album containing the test song^
    devices = get_available_devices()
    print("Your available devices are", list(
        map(lambda device: device["name"], devices)))
    selected_device = get_device_selection(devices)
    print("OK, using", selected_device["name"])

    play_track(test_track_id, test_context, selected_device)
