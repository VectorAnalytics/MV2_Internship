# MV2_Internship
Files associated with DSBA Internship conducted by Marcia Price.

## Task 1: ID Set of Patents That Define Current Body Armor Technology 

I used the United Stated Patent and Trademark Organization's (USPTO's) Advanced Search function at http://appft.uspto.gov/netahtml/PTO/search-adv.html and entered the following search string to find patents with "armor" in the title, granted from Jan 1 2010 until Jun 30 2017: ((APT/1 AND TTL/armor) AND APD/20100101->20170630) where APD is application date (not the patent grant date), TTL is title, and APT/1 means I am searching for utility patents only. This search string yielded the most applicable set of patents; using "body armor" in the title was too specific (did not yield a large enough patent set) and using a keyword search on the abstract yielded too board/diverse of a patent set.

This search yielded 181 patents. Patent number and title for each of these 181 patents is available in this file: https://github.com/VectorAnalytics/MV2_Internship/blob/master/BodyArmorPatents_181.xlsx

This set of 181 armor patents was refined by reading each patent title, and ensuring that the title was reflective of a patent related to body armor. After this human review, I was left with 111 patents that best represent current body armor technology. I deleted patents related to vehicle armor and transparent armor. This downselected set of base body armor patents is available in this file:
https://github.com/VectorAnalytics/MV2_Internship/blob/master/BodyArmorPatents_111.xlsx

**Note:** this is a basic "search, copy, paste" method to generate a base set of patents from the USPTO's free online website. I'm able to develop a base set of patents using this method, but can only capture the patent number and the patent title from the USPTO's website. This is enough information to generate my first network analysis, based on patent technology codes. But I will need to secure access to more robust patent search functionality to gather patent assignee information for subsequent network analyses.

## Task (Download and convert text files to csv that contains CPC code data parsed as required for project)

The USPTO's CPC master classification files contain a list of all CPC technology codes used on a patent and the symbol position (first or last) and the classification value code (inventive or additive) of each CPC on the patent. This is the information I need to build my first network. The files are available in XML or txt in bulk at this location (patents are saved in sequential files of 100K patents, all available in a zip folder to download): https://bulkdata.uspto.gov/data2/patent/classification/cpc/

