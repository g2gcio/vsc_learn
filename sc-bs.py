import requests
from bs4 import BeautifulSoup

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

list = ["https://sgtalk.org/mybb/Forum-Market-Talk",
        'https://sgtalk.org/mybb/Forum-Market-Talk?page=2',
        'https://sgtalk.org/mybb/Forum-Market-Talk?page=3',
        'https://sgtalk.org/mybb/Forum-Market-Talk?page=4',
        'https://sgtalk.org/mybb/Forum-Market-Talk?page=5']

list = ["https://sgtalk.org/mybb/Forum-Market-Talk"]


counter = 1
for i in list:
    data = requests.get(i, verify=False)

    soup = BeautifulSoup(data.text, "html.parser")
    for span in soup.find_all("a", class_="gothread"):
        print(span)
        print(counter,"-------------------------------------------------")
        counter = counter + 1
