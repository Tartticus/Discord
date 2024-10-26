###### Hotdog bot a bot that just types nigga
import json
import sys
import random
import time
import os
from datetime import datetime
import requests



#Hotdog directory
directory = r"C:\Users\Matth\OneDrive\Documents\Discord\HotDogMemes"


# List all files in the directory and filter only image files (e.g., JPG, PNG)
images = [file for file in os.listdir(directory) if file.endswith(('.jpg', '.jpeg', '.png'))]

# Randomly select a hotdog
random_image = random.choice(images)
hotdog_path = os.path.join(directory, random_image)
print(f"Selected hotdog: {hotdog_path}")


def send_message(channel_id, message, token, hotdog_path):
    # Discord's message endpoint
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    
    # Prepare the headers with the correct token format
    with open(hotdog_path, 'rb') as file:
        header_data = {
            
            "Authorization": f"Bot {token}"  # Note the 'Bot ' prefix here
        }
    
        # The message payload
        message_data = {
            "content": message
        }
        files = {
               "file" : file} 

        # Send the POST request to Discord API
        response = requests.post(url, headers=header_data, data=message_data, files=files)

    

    # Print the full response for debugging
    print(f"Status Code: {response.status_code}")
    

    # Print the response JSON if the request was successful
    if response.status_code == 200:
        print("Hotdog sent successfully!")
        
    else:
        print(f"Failed to send message: {response.status_code} - {response.text}")




def main():
    token = ''
    channel_id = '1299770225688055920'
    message = "Hotdog of the day:"

    # Send the message
    send_message(channel_id, message, token, hotdog_path)

if __name__ == "__main__":
    main()
