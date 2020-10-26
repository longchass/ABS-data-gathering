import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from string import ascii_lowercase

f = open("SA2.txt", "r")
data = f.readlines()
e = open("SA2url.txt", "a")

for i in data : e.write("https://itt.abs.gov.au/itt/r.jsp?RegionSummary&region="+i+" "+"&dataset=ABS_REGIONAL_ASGS2016&geoconcept=ASGS_2016&measure=MEASURE&datasetASGS=ABS_REGIONAL_ASGS2016&datasetLGA=ABS_REGIONAL_LGA2018&regionLGA=LGA_2018&regionASGS=ASGS_2016" + '\n')