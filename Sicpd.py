import requests
import logging
import os

# Set up logging for Sicpd.py
logging.basicConfig(filename='sicpd.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_subdomains(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        return response.text.splitlines()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching subdomains: {e}")
        return []

def save_new_subdomains(new_subdomains, filename):
    try:
        with open(filename, 'w') as file:  # Open in write mode to clear the file
            for subdomain in new_subdomains:
                file.write(f"{subdomain}\n")
        logging.info(f"Saved {len(new_subdomains)} new subdomains to {filename}")
    except Exception as e:
        logging.error(f"Error saving new subdomains: {e}")

def update_existing_subdomains(new_subdomains, existing_subdomains_file):
    try:
        with open(existing_subdomains_file, 'a') as file:  # Open in append mode
            for subdomain in new_subdomains:
                file.write(f"{subdomain}\n")
        logging.info(f"Updated existing subdomains with {len(new_subdomains)} new entries.")
    except Exception as e:
        logging.error(f"Error updating existing subdomains: {e}")

def main():
    url = "https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/main/data/wildcards.txt"  # Your specified source
    new_subdomains_file = 'new_subdomains.txt'
    existing_subdomains_file = 'existing_subdomains.txt'

    # Read existing subdomains
    existing_subdomains = set()
    if os.path.exists(existing_subdomains_file):
        with open(existing_subdomains_file, 'r') as file:
            existing_subdomains = set(file.read().splitlines())
    else:
        logging.warning(f"{existing_subdomains_file} does not exist. Please create it with existing subdomains.")
        return

    # Fetch new subdomains
    new_subdomains = fetch_subdomains(url)

    # Filter out already existing subdomains
    new_unique_subdomains = set(new_subdomains) - existing_subdomains

    # Save new unique subdomains to new_subdomains.txt
    if new_unique_subdomains:
        save_new_subdomains(new_unique_subdomains, new_subdomains_file)
        # Update existing_subdomains.txt with the new subdomains
        update_existing_subdomains(new_unique_subdomains, existing_subdomains_file)
    else:
        logging.info("No new unique subdomains retrieved.")

if __name__ == "__main__":
    main()

