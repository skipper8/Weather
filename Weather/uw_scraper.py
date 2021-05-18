#UW SCRAPER

#GOAL:
#Scrapes from UW weather data every 24 hours


#IMPORTS___________________________________________________
from bs4 import BeautifulSoup

class uw_scraper():
    def __init__(self):
        self.URL= 'https://a.atmos.washington.edu/data/data.php?loc=local'
        self.soup = BeautifulSoup(self.URL, 'html.parser')
    
    def gather(self, rate):
        
