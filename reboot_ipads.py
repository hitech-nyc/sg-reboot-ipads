import requests
import datetime
import json as JSON
import os
import time
import argparse


# Scheduled reboot time 
SCHEDULED_TIME = 7
# Fetch the Kandji token from environment variables
AUTH = os.getenv('KANDJI_TOKEN')
if not AUTH:
    raise ValueError("Environment variable KANDJI_TOKEN not set")


def reboot_ipad(device_id):
    """Reboot the iPad."""

    url = f"https://seatgeek.clients.us-1.kandji.io/api/v1/devices/{device_id}/action/restart"
    headers = {'Authorization': AUTH}
    response = requests.post(url, headers=headers)
    return response.json()


def load_ipads():
    """Load iPad data from JSON file."""

    with open('conferenceroom_ipads.json', 'r') as file:
        return JSON.load(file)


def reboot_all_ipads():
    """Reboot all iPads listed in the JSON file."""

    ipads = load_ipads()
    for ipad, ipad_id in ipads.items():
        print(f"Rebooting {ipad}...")
        response = reboot_ipad(ipad_id)
        print(f"{ipad}: {response}")


def run_daily_schedule():
    """Run the script daily"""

    print(f"Scheduled mode activated. Waiting for {SCHEDULED_TIME}AM...")
    while True:
        now = datetime.datetime.now()
        if now.hour == SCHEDULED_TIME and now.minute == 0:
            print(f"Running reboot at {now.strftime('%Y-%m-%d %H:%M:%S')}")
            reboot_all_ipads()
            time.sleep(60)  # Wait 1 minute to prevent multiple executions in the same minute
        time.sleep(30) 

# ------------ MAIN
def main():
    parser = argparse.ArgumentParser(description="Reboot iPads using Kandji MDM API.")
    parser.add_argument('-m', choices=['daily', 'once'], required=True,
                        help="Specify 'daily' to run at 9 AM every day or 'once' to run immediately.")
    args = parser.parse_args()

    if args.m == 'daily':
        run_daily_schedule()
    else:
        print(f"Running reboot now at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        reboot_all_ipads()

if __name__ == '__main__':
    main()
