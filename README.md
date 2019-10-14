# Wikipedia-Crawler

Simple project that endlessly crawls wikipedia, following links from the main page.   
The program initally uses the request module to request and retrieve the html for the Wikipedia main page. Using the Beautiful Soup module, the href tags are extracted from the content section of the html. Each of the links inside these href tags are analysed and matched against regular expressions pattern to ensure only the links found inside the actual Wikipedia content body are stored. A random link is selected from this final list of URLs. This URL is then called and the cycle continues.

-------------------------------------------------------

### How to Use

Run wikiCrawler.py
