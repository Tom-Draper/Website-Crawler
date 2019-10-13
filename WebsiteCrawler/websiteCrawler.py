from urlStack import UrlStack
from webScraper import WebScraper
import time


startUrl = 'https://en.wikipedia.org/wiki/Main_Page'

stack = UrlStack()
stack.push(startUrl)
webScraper = WebScraper()

url = stack.peek()
for _ in range(100):
    url = webScraper.scrape(url)
    if url == None:
        url = stack.pop()
    stack.push(url)
    time.sleep(1)
    
