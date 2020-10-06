import requests
import os
from bs4 import BeautifulSoup
import dryscrape

SG4D = 'https://www.singaporepools.com.sg/en/product/Pages/4d_results.aspx'
result = requests.get(SG4D)
session = dryscrape.Session()
session.visit(SG4D)
response = session.body()

soup = BeautifulSoup(response)
soup.find(id="intro-text")

#print(result.text)

output_file = open('result.txt', 'w', encoding="utf-8")
#output_file.write(result.text)
output_file.write(soup)

#print(result.status_code)
