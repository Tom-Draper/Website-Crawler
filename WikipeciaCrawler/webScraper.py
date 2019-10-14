from random import randint
import requests
from bs4 import BeautifulSoup
import re

class WebScraper:
    
    def requestWebpage(self, url):
        print('Requesting ' + url[30:] + '...')
        
        res = requests.get(url)
        try:
            res.raise_for_status()
            res.status_code == requests.codes.ok
        except Exception as ex:
            print('There was a problem: %s' % (ex))
        return res.text
    
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
        link = links[rand]
        
        # Ensure link is a full url
        if link[0] == '/':
            link = 'https://en.wikipedia.org' + link
        return link