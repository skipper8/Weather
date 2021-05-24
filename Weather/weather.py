#WEATHER APP

#GOAL:
#A weather predictor model that can guess the weather of a particular locationup to 14 days in advance with an 80% accuracy

#IMPORTS
from uw_scraper import uw_scraper

#test scraper
uw = uw_scraper()
print(uw.gather())
