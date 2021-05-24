#UW SCRAPER

#GOAL:
#Scrapes from UW weather data every 24 hours


#IMPORTS___________________________________________________
from bs4 import BeautifulSoup
import requests

class uw_scraper():
    def __init__(self):
        self.URL= 'https://a.atmos.washington.edu/cgi-bin/list_uw.cgi'
        self.soup = BeautifulSoup(requests.get(self.URL).content, 'html.parser')
    
    def gather(self):
        latest = self.soup.find('b')
        new_url = latest.a
        return  new_url.get('href')
