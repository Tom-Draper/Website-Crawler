# webScraper.py - requests a wikipeia webpage url and extracts links to other
# wikipedia pages.
# Narrows down list to links found inside content text and returns a random url
# from that list 

from random import randint
import requests
from bs4 import BeautifulSoup
import re

class WebScraper:
    
    # Requests a url and returns the webpage html as text
    def requestWebpage(self, url):
        # Remove 'https://en.wikipedia.org' from url and display
        print('Requesting ' + url[30:] + '...')
        
        res = requests.get(url)
        try:
            res.raise_for_status()
            res.status_code == requests.codes.ok
        except Exception as ex:
            print('There was a problem: %s' % (ex))
        return res.text
    
    # Gets url webpage html and extracts all links to a list
    # Narrows down list to links found inside main text
    # Formats and returns a random link
    def scrapeLinks(self, url):
        html = self.requestWebpage(url)
        soup = BeautifulSoup(html, 'html.parser')
        
        pageContent = soup.find('div', {'id': 'content'})
        pageLinks = pageContent.find_all('a', href=True)
        
        links = [] # To build a list of usable links
        for pageLink in pageLinks:
            # If link follows regex pattern, it is usable and appended to links list
            linkMatch = re.findall(r'/wiki/[a-zA-Z_]+$', pageLink['href'])
            if (linkMatch): 
                links.append(linkMatch[0])
            
        # Select random link from the list
        rand = randint(0, len(links) - 1)
        newLink = links[rand]
        
        # Ensure link is a full url
        if newLink[0] == '/':
            newLink = 'https://en.wikipedia.org' + newLink
        return newLink