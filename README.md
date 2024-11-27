# Kandji iPad Reboot Script
This script automates the rebooting of conference room iPads managed via Kandji MDM. It can either perform immediate reboots or schedule daily reboots at a specified time.

# Features
Scheduled Reboot: Automatically reboots iPads at X daily.
Manual Reboot: Run an immediate reboot of all specified iPads.

### Requirements
Python 3.8 or higher


# Set Up Instructions:
Ensure that the KANDJI_TOKEN environment variable is set with your Kandji API token.


## Install dependencies:
`pip install requests`

Create a JSON file with iPad data:

File: conferenceroom_ipads.json
```
{
  "ipad_name_1": "device_id_1",
  "ipad_name_2": "device_id_2"
}
```

## Set the Kandji API token:

`export KANDJI_TOKEN="your_kandji_api_token_here"`

# Usage
### Immediate Reboot:
To run the reboot process immediately:
`python reboot_ipads.py -m once`
### Scheduled Daily Reboot:
To schedule the reboot at 7:00 AM every day:
`python reboot_ipads.py -m daily`


# Script Overview
Main Functions:
reboot_ipad(device_id): Sends a request to Kandji's API to reboot a specific iPad.
load_ipads(): Reads the iPad list and their IDs from the conferenceroom_ipads.json file.
reboot_all_ipads(): Iterates through all iPads in the JSON file and reboots them.
run_daily_schedule(): Keeps the script running, triggering the reboot process at the specified time (7:00 AM).
## Customization:
Scheduled Time: Adjust the SCHEDULED_TIME variable if a different reboot time is needed.
API Endpoint: Ensure that the API endpoint matches your Kandji configuration.
## Logging and Monitoring
The script prints log messages to the console, indicating when reboots are initiated and completed.
It waits 1 minute after each scheduled reboot to avoid multiple triggers within the same minute.
## Troubleshooting
Ensure the KANDJI_TOKEN is valid and has sufficient permissions.
Verify the conferenceroom_ipads.json file contains correct device IDs.
Check network connectivity to the Kandji API endpoint.
