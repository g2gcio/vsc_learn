import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from bs4 import BeautifulSoup

import dataset
db = dataset.connect('sqlite:///sgtalk.db')

sgtable = db['authors']

page_list = ["https://sgtalk.org/mybb/Forum-Market-Talk",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=2",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=3",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=4",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=5",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=6",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=7",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=8",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=9",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=10",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=11",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=12",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=13",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=14",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=15",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=16",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=17",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=18",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=19",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=20",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=21",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=22",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=23",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=24",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=25",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=26",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=27",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=28",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=29",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=30"
]

#page_list = ["https://sgtalk.org/mybb/Forum-Market-Talk"]

for list in page_list:
    page = requests.get(list, verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find_all('tr', class_='inline_row')
    for t in table:
        subject = t.find('span', class_="subject_new")
        subject_title = subject.find('a').get("href").replace('Thread-','')
        author = t.find('div', class_="author smalltext")
        author_name = author.find('a')
        author_name1=author_name.get('href').replace('https://sgtalk.org/mybb/User-','')
#        print(subject_title,",",author_name1)
        sgtable.insert(dict(name=author_name1, article=subject_title))
