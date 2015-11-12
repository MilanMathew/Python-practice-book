# Given an url of a webpage, 
# print all the *visible* links in it.
import os
import sys
import urllib
import re

def execute():
    url = sys.argv[1]
    data = urllib.urlopen(url)
    links = re.findall(r'<a.*?>.*?</a>', data.read()) 
    for link in links:
        print link[link.find('>')+1: -4]
    return 

execute()
