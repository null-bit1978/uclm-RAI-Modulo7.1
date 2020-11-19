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

#compilamos la página para trabajar sobre ella
page = requests.get(url).text

#aquí va toda la funcionalidad del script
def find_form(url):
    pattern = re.compile(r"<form (\w|\W)+<\/form>") #utilizamos este patrón en búsqueda del formulario. Definido a base de prueba y error, así que desconocemos su grado de universalidad
    match = pattern.search(url)
    if match:
        return match.group(0)
    else:
        return None

def find_links(url):
    pattern = re.compile(r'href="(https?:\/\/[\w.\/?=,&-]+)') # este patrón también se ha definido a base de prueba y error.
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








