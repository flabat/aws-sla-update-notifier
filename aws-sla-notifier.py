from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime

AWS_SLA_URL = 'https://aws.amazon.com/legal/service-level-agreements/'

r = requests.get(AWS_SLA_URL)
soup = BeautifulSoup(r.content, 'html.parser')  

# print(soup.body.findAll(text=re.compile('Service Level Agreement$')))

for link in soup.findAll('a', href=True, text=re.compile(r'Service Level Agreement$')):
    print(link['href'])
    r = requests.get(link['href'])
    soup = BeautifulSoup(r.content, 'html.parser')
    lastupdated = soup.body.findAll(text=re.compile('Last Updated'))
    lastupdated = lastupdated[0].strip('Last Updated')
    lastupdated = lastupdated.strip(':').lstrip().rstrip()
    # print(lastupdated)
    lastupdated_date = datetime.strptime(lastupdated, '%B %d, %Y')
    print(lastupdated_date)
    print(datetime.now() - lastupdated_date)
