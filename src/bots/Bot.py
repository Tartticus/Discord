import json
import sys
import random
import time
from datetime import datetime
import requests


def send_message(channel_id, message, token):
    # Prepare the headers with the correct token format
    header_data = {
        "Content-Type": "application/json",
        "Authorization": f"Bot {token}"  # Note the 'Bot ' prefix here
    }

    # The message payload
    message_data = json.dumps({
        "content": message
    })

    # Discord's message endpoint
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"

    # Send the POST request to Discord API
    response = requests.post(url, headers=header_data, data=message_data)

    # Print the full response for debugging
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    # Print the response JSON if the request was successful
    if response.status_code == 200:
        print("Message sent successfully!")
        print(f"Response JSON: {response.json()}")
    else:
        print(f"Failed to send message: {response.status_code} - {response.text}")




def main():
    # Niggabot token
    token = 'your token herre'
    channel_id = '1299505788749873209'
    message = "your message"

    # Send the message
    send_message(channel_id, message, token)

if __name__ == "__main__":
    main()
