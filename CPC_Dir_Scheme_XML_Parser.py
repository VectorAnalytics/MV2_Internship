# -*- coding: utf-8 -*-
"""
Title
"""
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
        tuple = code.get('sort-key')
        title_parts = code.find_all('title-part')
        #print([tuple, level, title_parts])
        for title_part in title_parts[:1]:
            title_part_text = title_part.find('text').getText()
            #Below to remove symbols and workaround UnicodeEncodeError.
            title_part_text = title_part_text.encode('ascii', 'ignore').decode('ascii')
            #print([tuple, level, title_part_text])
            outfile.writerow([tuple, level, title_part_text])
