# -*- coding: utf-8 -*-
# This code will generate a good definition for CPC maingroups.
"""
Created on Aug 5 2017

@author: Marcia
"""

import pandas as pd
#Read results of CPC scheme xml parsing. 
all_defs_df = pd.read_csv('/Users/Marcia/OneDrive/MV2_Internship/cpc-scheme-all.csv',
                         keep_default_na=False, na_values=[""])
#Create df of just level 5 definitions
l5_df=all_defs_df[['tuple', 'scheme', 'level']].copy()
l5f_df=l5_df[l5_df.level == 5]
l5f_df.rename(columns = {'tuple':'subclass', 'scheme':'l5_def'}, inplace=True)                            
l5f_df.drop('level', axis=1, inplace=True)
#Create df of just level 7 definitions
l7_df=all_defs_df[['tuple', 'scheme', 'level']].copy()
l7f_df=l5_df[l7_df.level == 7]
l7f_df.rename(columns = {'tuple':'maingroup', 'scheme':'l7_def'}, inplace=True)        
l7f_df.drop('level', axis=1, inplace=True)
#Create subclass from maingroup in l7f_df.
l7f_df['subclass']=l7f_df.maingroup.str[:4]
#Clean the '/00' off the maingroup.
l7f_df['maingroup']=l7f_df['maingroup'].astype(str)
l7f_df['maingroup']=l7f_df['maingroup'].str.split('/', 1).str[0].str.strip()
#Inner merge the l5_df with the l7_df
mg_defs_df = pd.merge(left=l5f_df,right=l7f_df, left_on='subclass', right_on='subclass')
mg_defs_df['mg_def']=mg_defs_df['l5_def'] + ' - ' + mg_defs_df['l7_def']
mg_defs_df.drop(['l5_def','l7_def','subclass'], axis=1, inplace=True)

#Save  df to csv file.
mg_defs_df.to_csv('/Users/Marcia/OneDrive/MV2_Internship/mg_defs.csv', index=False)
