import httplib2
import bs4 as bs
from bs4 import BeautifulSoup, SoupStrainer


def parseLinksFromHTML(file,attribute):
    http = httplib2.Http()
    status, response = http.request(file)
    return bs.BeautifulSoup(response, 'html.parser',parseOnlyThese=SoupStrainer(attribute))