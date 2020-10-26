import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from string import ascii_lowercase
f = open ("subinpost.txt","a")
for c in ascii_lowercase:

	for x in range(5):
		url = 'https://auspost.com.au/postcode/suburb-index/'+c+str(x)

		response = requests.get(url)

		soup = BeautifulSoup(response.text, "html.parser")

		for strings in soup.body.find_all("a", class_='suburb-listing'): f.write(str(strings)+ '\n')

f.close()