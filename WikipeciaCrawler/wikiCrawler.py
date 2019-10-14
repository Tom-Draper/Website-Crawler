# wikiCrawler.py - continuously jumps between linked wikipedia pages starting
# from the main page

from urlStack import UrlStack
from webScraper import WebScraper
import time

url = 'https://en.wikipedia.org/wiki/Main_Page'

stack = UrlStack()
stack.push(url)

webScraper = WebScraper()

# Continuously requests a webpage and retrieves a random url on that webpage
# to then request
# If no urls found on a webpage, previous url popped off the stack and reused
for _ in range(100):
    url = webScraper.scrapeLinks(url)
    if url == None:
        url = stack.pop()
    stack.push(url)
    time.sleep(1)
    
