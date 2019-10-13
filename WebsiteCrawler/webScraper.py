from random import randint
import requests
from bs4 import BeautifulSoup

class WebScraper:
    
    def requestWebpage(self, url):
        print('Requesting ' + url + '...')
        
        res = requests.get(url)
        try:
            res.raise_for_status()
            res.status_code == requests.codes.ok
        except Exception as ex:
            print('There was a problem: %s' % (ex))
        return res.text
    
    def scrape(self, url):
        html = self.requestWebpage(url)
        soup = BeautifulSoup(html, 'html.parser')
        
        pageContent = soup.find('div', {'id': 'content'})
        links = pageContent.find_all('a', href=True)
        # Get 20 hrefs after initial page links
        links = links[:38]
        for link in links:
            print(link['href'])
        # Find first usable link
        rand = randint(0, len(links))
        
        link = links[rand]['href']
        if link[0] == '/':
            link = 'https://en.wikipedia.org' + link
        return link