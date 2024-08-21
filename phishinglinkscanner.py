import re

# Function to load a list from a text file
def load_list_from_file(phishinglinkscanner):
    with open(phishinglinkscanner, 'r') as file:
        return [line.strip() for line in file]

# Load phishing keywords and domains from files
PHISHING_KEYWORDS = load_list_from_file('phishing_keywords.txt')
PHISHING_DOMAINS = load_list_from_file('phishing_domains.txt')

def is_phishing_url(url):
    # Check if the URL contains any known phishing keywords
    for keyword in PHISHING_KEYWORDS:
        if keyword in url.lower():
            return True

    # Check if the URL's domain matches any known phishing domains
    for domain in PHISHING_DOMAINS:
        if domain in url.lower():
            return True

    return False

def main():
    while True:
        # Prompt the user for a URL to check
        url = input("Enter the URL to check (or type 'q' to quit): ")

        if url.lower() == 'q':
            print("Exiting the scanner. Goodbye!")
            break

        # Scan the URL using the phishing detection function
        if is_phishing_url(url):
            print("Warning: This URL appears to be suspicious!")
        else:
            print("This URL seems to be safe.")

if __name__ == "__main__":
    main()
