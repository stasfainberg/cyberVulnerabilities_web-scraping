import requests
from bs4 import BeautifulSoup
import time
import hashlib

# URL of the website to monitor
url = "https://example.com/publications"

# Function to fetch and parse the webpage
def fetch_publications():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract publication elements (update the selector to match the website)
        publications = soup.select('.publication-title')  # Example: CSS selector
        return [pub.text.strip() for pub in publications]
    except requests.RequestException as e:
        print(f"Error fetching the website: {e}")
        return []

# Monitor for new publications
def monitor_publications():
    global previous_hash
    publications = fetch_publications()
    if not publications:
        return

    # Generate a hash of the publication list
    current_hash = hashlib.sha256(str(publications).encode('utf-8')).hexdigest()

    # Compare with the previous hash
    if current_hash != previous_hash:
        print("New publications detected!")
        print("\n".join(publications))
        previous_hash = current_hash  # Update the hash

# Initialize with an empty hash
previous_hash = ""

# Run the script periodically
while True:
    monitor_publications()
    time.sleep(60)  # Check every 60 seconds
