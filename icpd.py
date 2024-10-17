import requests
import logging
import os

# Set up logging for icpd.py
logging.basicConfig(filename='icpd.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_domains(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        return response.text.splitlines()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching domains: {e}")
        return []

def save_new_domains(new_domains, filename):
    try:
        with open(filename, 'w') as file:  # Open in write mode to clear the file
            for domain in new_domains:
                file.write(f"{domain}\n")
        logging.info(f"Saved {len(new_domains)} new domains to {filename}")
    except Exception as e:
        logging.error(f"Error saving new domains: {e}")

def update_existing_domains(new_domains, existing_domains_file):
    try:
        with open(existing_domains_file, 'a') as file:  # Open in append mode
            for domain in new_domains:
                file.write(f"{domain}\n")
        logging.info(f"Updated existing domains with {len(new_domains)} new entries.")
    except Exception as e:
        logging.error(f"Error updating existing domains: {e}")

def main():
    url = "https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/main/data/domains.txt"  # Your specified source
    new_domains_file = 'new_domains.txt'
    existing_domains_file = 'existing_domains.txt'

    # Read existing domains
    existing_domains = set()
    if os.path.exists(existing_domains_file):
        with open(existing_domains_file, 'r') as file:
            existing_domains = set(file.read().splitlines())
    else:
        logging.warning(f"{existing_domains_file} does not exist. Please create it with existing domains.")
        return

    # Fetch new domains
    new_domains = fetch_domains(url)

    # Filter out already existing domains
    new_unique_domains = set(new_domains) - existing_domains

    # Save new unique domains to new_domains.txt
    if new_unique_domains:
        save_new_domains(new_unique_domains, new_domains_file)
        # Update existing_domains.txt with the new domains
        update_existing_domains(new_unique_domains, existing_domains_file)
    else:
        logging.info("No new unique domains retrieved.")

if __name__ == "__main__":
    main()

