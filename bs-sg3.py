import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from bs4 import BeautifulSoup
import dataset
import time

db = dataset.connect('sqlite:///sgtalk.db')
sgtable = db['authors']
rStart = 701
rEnd = 800
page_list = []

for i in range(rStart,rEnd):
    url='https://sgtalk.org/mybb/Forum-Market-Talk?page=' + str(i)
    page_list.append(url)

count = 1
for list in page_list:
    page = requests.get(list, verify=False, timeout=10)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find_all('tr', class_='inline_row')
    for t in table:
        subject = t.find('span', class_="subject_new")
        subject_title = subject.find('a').get("href").replace('Thread-','')
        author = t.find('div', class_="author smalltext")
        author_name = author.find('a')
        author_name1=author_name.get('href').replace('https://sgtalk.org/mybb/User-','')
#        print("%-20s " % author_name1, " ", subject_title)
        sgtable.insert(dict(name=author_name1, article=subject_title))
    print(rStart+count,count,"================")
    count+=1
#    time.sleep(5)