import os
import time
import requests

# Configuration
combined_results_path = '/home/kali/ICPD/combined_results.txt'  # Path to your combined_results.txt
bot_token = '7732597991:AAFUKo6UKgErvlwsGDVuKyJXC5SenwxIEeY'  # Your bot token
chat_id = '1993641298'  # Your chat ID

# Function to send a message via Telegram
def send_telegram_message(url):
    message = f"{url} Has some vulnerabilities sir!"
    url_api = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url_api, data=payload)
    
    # Check the response and print it
    if response.ok:
        print(f"Message sent: {message}")
    else:
        print(f"Failed to send message: {response.json()}")

# Monitor combined_results.txt for changes
last_modified_time = os.path.getmtime(combined_results_path)
notified_urls = set()  # To keep track of notified URLs

while True:
    time.sleep(60)  # Check every minute
    current_modified_time = os.path.getmtime(combined_results_path)

    if current_modified_time != last_modified_time:
        last_modified_time = current_modified_time
        with open(combined_results_path, 'r') as file:
            # Read the URLs from combined_results.txt
            urls = file.readlines()
            for url in urls:
                url = url.strip()  # Remove any surrounding whitespace
                if url and url not in notified_urls:  # Check if the URL is not empty and not already notified
                    send_telegram_message(url)  # Send each URL
                    notified_urls.add(url)  # Add to notified URLs set

        # Optionally, reset notified_urls after some condition or time
        # Example: Reset after 1 hour (3600 seconds)
        # time.sleep(3600)
        # notified_urls.clear()

