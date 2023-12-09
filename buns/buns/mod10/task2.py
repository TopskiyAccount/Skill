import requests
import re

def get_h3_headers(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    # Use regex to find all <h3> tags
    h3_tags = re.findall(r'<h3.*?>(.*?)<\/h3>', response.text, re.DOTALL)
    return h3_tags

# Example usage:
url = 'https://www.w3schools.com/html/html_intro.asp'
result = get_h3_headers(url)

if result:
    print(result)
