#!/usr/bin/env python
# -*- coding: ascii -*-
#-----------------------------------------------------------------------------
"""Scrapes http://data.worldbank.org/country/ for country data.
    No keywords.
"""

__author__ = 'Vedant Misra'
__license__ = 'BSD'
__vcs_id__ = '$Id$'
__version__ = '0.1' 

# Initialization
import os
import csv
import urllib
from operator import itemgetter

url0 = "http://data.worldbank.org/sites/default/files/countries/en/"
url1 = "_en.xml"

def generateCountries(country_list):
    """Returns list of tuples sorted by each tuple's first element.  Tuples
    are of the form 
	('korea-republic', 'Korea')
	('trinidad-and-tobago', 'Trinidad and Tobago')
    """
    f = open(country_list, 'r')
    r = csv.reader(f)

    countryDict = {}
    for row in r:
	countryDict[row[0]] = row[1]
   
    return sorted(countryDict.iteritems(), key=itemgetter(1))

def scrape(countries):
    """Copy the contents of files at the specified URL to a local file.
    """
    for country in countries:
	url = url0 + country + url1
	print "Getting", url
	webFile = urllib.urlopen(url)
	localFile = open(os.path.join(os.pardir, 'data', \
	    url.split('/')[-1]), 'w')
	localFile.write(webFile.read())
	webFile.close()
	localFile.close()

def test():
    """ Testing Docstring"""
    pass

if __name__=='__main__':
    countryURLS = generateCountries(
	os.path.join(os.pardir, 'code', 'country_list.csv')).keys()
    scrape(countryURLs)


