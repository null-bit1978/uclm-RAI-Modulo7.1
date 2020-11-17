import requests
import re
import sys
from termcolor import colored

if len(sys.argv) == 1:
    print("Usage: python3 scraper.py <url>")
    sys.exit(1)

url = sys.argv[1]
status = requests.get(url).status_code

if status != 200:
    print(f"Connection returned the status {status}, try with a different url.")
    sys.exit(1)

page = requests.get(url).text

def find_form(url):
    pattern = re.compile(r"<form (\w|\W)+<\/form>")
    match = pattern.search(url)
    if match:
        return match.group(0)
    else:
        return None

def find_links(url):
    pattern = re.compile(r'href="(https?:\/\/[\w.\/?=,&-]+)')
    matches = re.findall(pattern, page)
    return matches

form = find_form(page)
if form:
	print(form)
else:
	print(colored("No form found on this page", "red"))

links = find_links(page)
for link in links:
    print(colored(link, "green"))








