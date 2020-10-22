import pandas as pd
import numpy as np
import ImportingData
import re



df = ImportingData.LoadAdjustedCSV()

#print(df.shape)
#print(df.date_added.isnull().sum())

#Out of the 22,000 rows in the data set 21,878 of them have an empty date added value
#This makes that row's information not very informative

#Due to this the column is removed
#df = df.drop(['date_added'], axis = 1)


#x = df[df.has_expired != 'No']
#print(x.info)

#All of the rows have the value "No" in the has expired column

#Due to this removed the column
#df = df.drop(columns = ['has_expired'])
#print(df.columns)


# x = df[df.job_board != 'jobs.monster.com']
#print(x.shape)

#All the rows have the same url in job_board

#Due to this removed the column
#df = df.drop(columns = ['job_board'])

#All jobs are in the united states
#x = df[df.country != 'United States of America']
#print(x)

#Removed country and country_code columns
#df = df.drop(columns = ['country', 'country_code'])

#print(df.location.head())
#This shows that the location column has three different entries
#1: City, State, Zip 2:City, State, 3:Misread Information
#It would be ideal to turn everything into an entry 1 but we don't have the info to do that


#Next, I will remove the zipcodes from the data, and seperate out state from city, and then remove the incorrect entries
#df['location_no_num'] = df.location.str.replace('\d+', "")

#temp_df = df['location_no_num'].str.split(',')

#location_list = []
#state_list = []
#city_list = []
#for x in temp_df:
#     if len(x) == 2:
#         x[1] = x[1].strip()
#         if len(x[1]) == 2:
#             city_list.append(str(x[0]))
#             state_list.append(str(x[1]))
#             location_list.append(str(x[0] + ", " + x[1]))
#
#         else:
#             location_list.append('')
#             state_list.append('')
#             city_list.append('')
#     else:
#         location_list.append("")
#         state_list.append('')
#         city_list.append('')
#
#
# df = df.drop(columns = 'location_no_num')
#
# df['temp_location'] = pd.Series(data = location_list, index = df.index)
# df['temp_state'] = pd.Series(data = state_list, index = df.index)
#
#

# #Looking at the page url I noticed that the location of the job is embedded in the url
# df['contains_us'] = df['page_url'].str.contains('-us-', case = False)
#print(df.shape)
#print(df['contains_us'].sum())
#
#
# df['page_url'] = df['page_url'].str.lower()
# df['url_split'] = df['page_url'].str.split('-us-')
#
# state_list = []
# count = 0
# for x in df['url_split']:
#     if len(x) == 2:
#         x = x[0]
#         x = x.split('-')
#         state = x[-1]
#         city = x[-2]
#         if len(state) == 2:
#             state_list.append(state.upper())
#         else:
#             state_list.append("")
#     else:
#         state_list.append("")
#
#
# final_state_list = []
# pointer = 0
# for x in df['temp_location']:
#    if x == "":
#        final_state_list.append(state_list[pointer])
#
#    else:
#         final_state_list.append(df['temp_state'][pointer])
#
#    pointer +=1
#
# df['state'] = pd.Series(data = final_state_list, index = df.index)
#
# df = df.drop(columns = ['contains_us','url_split', 'temp_location', 'temp_state', 'location'])
# ImportingData.SaveAdjustedCSV(df)

