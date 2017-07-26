# -*- coding: utf-8 -*-
# This code will generate a set of nodes/edges for a network analysis of
# CPC codes used on a seed set of human selected patents.
#  Analysis is based on 8 digit maingroup CPC code.
"""
Created on July 17 2017

@author: Marcia
"""

import pandas as pd
#Read in the list of seed patents (human reviewed). 
#This file contains two columns, pat_num and title (of patent.)
patlist_df = pd.read_csv('/Users/Marcia/OneDrive/MV2_Internship/BodyArmorPatents_111.csv',
                         keep_default_na=False, na_values=[""])
#Read in the cpc master files in csv format that contain the cpc code info for all patents.                         
cpc780_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_780.csv',
                         keep_default_na=False, na_values=[""])            
cpc790_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_790.csv',
                         keep_default_na=False, na_values=[""]) 
cpc800_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_800.csv',
                         keep_default_na=False, na_values=[""])            
cpc810_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_810.csv',
                         keep_default_na=False, na_values=[""]) 
cpc820_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_820.csv',
                         keep_default_na=False, na_values=[""])            
cpc830_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_830.csv',
                         keep_default_na=False, na_values=[""]) 
cpc840_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_840.csv',
                         keep_default_na=False, na_values=[""])            
cpc850_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_850.csv',
                         keep_default_na=False, na_values=[""]) 
cpc860_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_860.csv',
                         keep_default_na=False, na_values=[""])            
cpc870_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_870.csv',
                         keep_default_na=False, na_values=[""]) 
cpc880_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_880.csv',
                         keep_default_na=False, na_values=[""])            
cpc890_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_890.csv',
                         keep_default_na=False, na_values=[""]) 
cpc900_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_900.csv',
                         keep_default_na=False, na_values=[""])            
cpc910_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_910.csv',
                         keep_default_na=False, na_values=[""]) 
cpc920_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_920.csv',
                         keep_default_na=False, na_values=[""])            
cpc930_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_930.csv',
                         keep_default_na=False, na_values=[""]) 
cpc940_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_940.csv',
                         keep_default_na=False, na_values=[""])
cpc950_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_950.csv',
                         keep_default_na=False, na_values=[""])
cpc960_df = pd.read_csv('/Users/Marcia/OneDrive/UNCC/DSBA_6440/CPC_MCF_Data/cpc_960.csv',
                         keep_default_na=False, na_values=[""])                         
#Concatinate all the cpc_df together into one df.
cpcmcf_df=pd.concat([cpc780_df,cpc790_df,cpc800_df,cpc810_df,cpc820_df,cpc830_df,
                     cpc840_df,cpc850_df,cpc860_df,cpc870_df,cpc880_df,cpc890_df,
                     cpc900_df,cpc910_df,cpc920_df,cpc930_df,cpc940_df,cpc950_df,
                     cpc960_df],axis=0)
#Inner merge the patnums with the cpc_df
seed_pns_and_all_cpcs = pd.merge(left=patlist_df,right=cpcmcf_df, left_on='pat_num', right_on='pat_num')

#So this file and df contains the seed patents and all the CPCs listed on each patent.
#It includes CPCs in all positions and values (FI, LI, LA); info for a given patent is 
#   contained on multiple lines, one CPC code per line.

#Now need to identify and put into a df just the CPC's we are interested in from the 
#  seed patents. Need just a column of "seed CPC's". We will look for all patents with 
#  these CPC's in the subsequent step.
#Just keep the CPC's in FI positions.
seed_cpc_df=seed_pns_and_all_cpcs[seed_pns_and_all_cpcs.pos_val == 'FI'] 
#Want to keep just the maingroup cpc column.
seed_cpc_df=seed_cpc_df[['main_group']]
seed_cpc_dedupe_df=seed_cpc_df.drop_duplicates(subset=None, keep='first', inplace=False)
#
#Now want to go back to the CPC master files and find all patents that use 
#    the seed CPC's in the FI position.
#Just keep the CPC's in FI positions.
first_cpcmcf_df=cpcmcf_df[cpcmcf_df.pos_val == 'FI']                    
#Inner merge the seed CPC's with the first_cpc_df, to get a list of patent
#    numbers that have the seed CPC's as a FI CPC.
expanded_pat_seed_df = pd.merge(left=seed_cpc_dedupe_df,right=first_cpcmcf_df, left_on='main_group', right_on='main_group')
#Keep just the patnum column from this df as that is all you need.
expanded_pat_seed_df=expanded_pat_seed_df[['pat_num']]
#Now get all cpcs (including LI and LA) for the patent set above. 
#Info for each patent will be on multiple lines, 1 line for each CPC on the patent.
#This is "ds1"; i.e. patents in the first degree of separation from 
#   the human curated seed patent set.
ds1_df = pd.merge(left=expanded_pat_seed_df,right=cpcmcf_df, left_on='pat_num', right_on='pat_num')

#Now generate edges and nodes table from final dataframe.
#Decided to use "copy" to make a complete new copy of the df, not just a reference to it.
first_df=ds1_df.copy()
#Rename main_group.
first_df.rename(columns = {'main_group':'fmain_group'}, inplace=True)
#Want to keep only main_groups that are First Invention.
first_df=first_df[first_df.pos_val == 'FI']
#Want to keep just two fields, the patnum and the maingroup
first_df=first_df[['pat_num', 'fmain_group']]
#Repeat to generate a list of patnums with just LI and LA maingroups.
later_df=ds1_df.copy()
later_df = later_df[later_df.pos_val != 'FI']
later_df.rename(columns = {'main_group':'lmain_group'}, inplace=True)
later_df=later_df[['pat_num', 'lmain_group']]
#Inner merge the fmain_groups with the lmain_groups by patnum, 
#  to create pairs of FI,Later for each patnum.
mg_pairs_df = pd.merge(left=first_df,right=later_df, left_on='pat_num', right_on='pat_num')

#Only keep pairs where fmain_group does not match lmain_group
#   (dont want nodes edging to themselves).
mg_unique_pairs_df=mg_pairs_df[mg_pairs_df.fmain_group != mg_pairs_df.lmain_group]
#Get a count of the pairs
network_all_df = mg_unique_pairs_df.groupby(['fmain_group','lmain_group']).size().reset_index().rename(columns={0:'count'})
#Want to keep node pairs with edge count greater than 19.
network_df=network_all_df[(network_all_df['count'] > 19)]
#Rename columns so dataframe can be imported into gephi as an edge table.
network_df.rename(columns = {'fmain_group':'source', 'lmain_group':'target', 'count':'weight' }, inplace=True)
#Write final df to csv file.
network_df.to_csv('/Users/Marcia/OneDrive/MV2_Internship/DS1_Edges_Table.csv', index=False)