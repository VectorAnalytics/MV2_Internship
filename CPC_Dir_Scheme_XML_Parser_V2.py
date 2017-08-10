# -*- coding: utf-8 -*-
"""
Title
"""
#This code correctly gets the CPC symbol, not the sort-key, to use as the tuple.
#Fixes problem I had of missing definitions for maingroups that used all 8 digits.
#Note: In cpc xml files, the sort-key is missing 1 digit of the maingroup. Yikes! 
from bs4 import BeautifulSoup
import csv
import os
path = '/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPCSchemeXML201705'
outfile = csv.writer(open('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_Defs/cpc-scheme-all.csv', 'w'))
outfile.writerow(['tuple','level', 'scheme'])
for filename in os.listdir(path):
    fullname = os.path.join(path, filename)
       
    infile = open(fullname, 'rb')
    contents = infile.read()

    soup = BeautifulSoup( contents ,'lxml'  )
    #print(soup.prettify())
    codes = soup.find_all('classification-item')
    for code in codes:
        level = code.get('level')
        #print (level)
        #tuple = code.get('sort-key')
        tuple = code.find('classification-symbol').string
        #ttuple_text = tuple.getText()
        #Below to remove symbols and workaround UnicodeEncodeError.
        #ttuple_text = ttuple_text.encode('ascii', 'ignore').decode('ascii')
        title_parts = code.find_all('title-part')
        #print([tuple, level, title_parts])
        #The title_part text grab needs to be improved, as I am missing some relevant
        #  text using below code. 90% of defs are complete, other 10% is not 
        #  wrong, just missing some useful text.
        for title_part in title_parts[:1]:
            title_part_text = title_part.find('text').getText()
            #Below to remove symbols and workaround UnicodeEncodeError.
            title_part_text = title_part_text.encode('ascii', 'ignore').decode('ascii')
            #print([tuple, level, title_part_text])
            outfile.writerow([tuple, level, title_part_text])
