import requests
from bs4 import BeautifulSoup


#this method takes in a url of your choosing and the html tag you want to parse
def scrape_it(url, tag_name, attributes=None):
    #Uses the requests library to send an HTTP GET request to the specified URL.
    #The response object contains the webpage’s content, status code, headers, etc.
    response = requests.get(url)
    #Passes the response’s text (HTML content) to BeautifulSoup, which parses the HTML into a navigable structure.
    soup = BeautifulSoup(response.content, 'html.parser')
    #here we tell our instance of BeautifulSoup to find all html elements
    #this can be leveraged to find
    tags = soup.find_all(tag_name, attrs=attributes)
    for tag in tags:
        #print the text of each span
        print(tag.name, " ", tag.get_text(strip=True))


#call my method and use it for victoria secret's website
print(scrape_it('https://www.victoriassecret.com/us/', 'span'))
print(scrape_it('https://www.victoriassecret.com/us/', 'h2'))
print(scrape_it('https://webscraper.io/test-sites/e-commerce/allinone', 'div', {"class": "col-lg-12"}))
