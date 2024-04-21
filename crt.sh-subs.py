import argparse
from crtsh import crtshAPI
import re

def validate_domain(domain):
    # Basic domain validation using a regular expression
    pattern = r"^(?:[-A-Za-z0-9]+\.)+[A-Za-z]{2,6}$"
    if re.match(pattern, domain):
        return True
    else:
        return False

def get_subdomains(target):
    try:
        api = crtshAPI()
        subdomains = api.search(target)
        return subdomains
    except Exception as e:
        print(f"Error fetching subdomains: {e}")
        return []

if __name__ == "__main__":
    # Personalize the description with your name
    description = "Tool by [Your Name] to collect subdomains from crt.sh for a given target domain."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("domain", help="Target domain for subdomain search")
    args = parser.parse_args()

    target_domain = args.domain.strip()
    
    if not validate_domain(target_domain):
        print("Invalid domain format. Please enter a valid domain.")
    else:
        subdomains_list = get_subdomains(target_domain)
        if subdomains_list:
            for subdomain in subdomains_list:
                print(subdomain['name_value'])
        else:
            print("No subdomains found.")
