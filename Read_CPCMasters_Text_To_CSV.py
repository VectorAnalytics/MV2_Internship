#!/usr/bin/env python
# -- coding: utf-8 -- 

# This code reads CPC Master Classification Files in Text format,
#    splits out the patnum and pieces of the CPC code that we need.
#     Including a header row for panda dfs.
# You have to process one CPC file at a time, changing the filenames in the code below.
import csv
import sys
csv.field_size_limit(sys.maxsize)
#Opening the file I write to before getting in the "for" loop.
outfile = open('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data_csv/cpc_960.csv', 'w')
wr =  csv.writer(outfile, dialect='excel') 
wr.writerow(["kind_code","pat_num", "main_group","pos_val", "cpc_sec", "cpc_class","cpc_subclass","cpc_main_grp4","cpc_subgroup"])
#with open('/Users/Marcia/OneDrive/DSBA_6880/CPC_MCF_Data/cpc_test', \
with open('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data_csv/US_Grant_CPC_MCF_9600000.txt', \
    encoding='utf-8', errors='ignore' ) as cpcfile:
    cpclist = csv.reader(cpcfile)
    #Skip the header row    
    #next(cpclist)   
    for row in cpclist:
        kind_code=str(row[0])[0:2] 
        pat_num=str(row[0])[10:17]
        main_group=(str(row[0])[17:25]).replace(" ","")
        cpc_sec=str(row[0])[17:18]
        cpc_class=str(row[0])[18:20]
        cpc_subclass=str(row[0])[20:21]
        cpc_main_grp4=str(row[0])[21:25]
        cpc_subgroup=str(row[0])[26:32]
        pos_val=str(row[0])[40:42]
        #Put all variables into one list.        
        pat_list=[kind_code,pat_num,main_group,pos_val,cpc_sec,cpc_class,cpc_subclass,cpc_main_grp4,cpc_subgroup]
        wr =  csv.writer(outfile, dialect='excel')
        #Write one row at a time to the open outfile.        
        wr.writerow(pat_list) 
#Needed to close outfile officially as I didn't use "with open" to open it.   
outfile.close()   
#print(row_count)          