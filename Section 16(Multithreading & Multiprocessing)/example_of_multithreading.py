'''
Real world example: MultiThreading for I/O-bound Tasks.
Scenerio: Web Scraping.
'''

'''
https://docs.langchain.com/oss/python/deepagents/data-analysis

https://docs.langchain.com/oss/python/deepagents/deep-research

https://docs.langchain.com/oss/python/deepagents/content-builder
'''

import threading
import BeautifulSoup
import requests

urls = [
    'https://docs.langchain.com/oss/python/deepagents/data-analysis',

'https://docs.langchain.com/oss/python/deepagents/deep-research',

'https://docs.langchain.com/oss/python/deepagents/content-builder'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(soup.text)
    
threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content,args=(url))
    threads.append(thread)
    thread.start()