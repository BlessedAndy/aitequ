'''
Created on Sep 17, 2016

@author: Andy Zhang
'''

#import the library used to query a website
from urllib.request import urlopen
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
baidu = "https://www.baidu.com"
sap = "http://www.sap.com"
lifehack = "http://www.lifehack.org"
#Query the website and return the html to the variable 'page'
page = urlopen(wiki)

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page,"html.parser")

print(soup)