# # import requests
import pandas as pd
# # import json
# # from pandas import json_normalize
# # resp = requests.get("https://chronicdata.cdc.gov/api/views/bq95-jg9r/rows.json?")
# # json = resp.json()
# # # print(json['data'])
# # # create dataframe from json
# # print(json[data])
# # # df = pd.DataFrame.from_dict(json['data'])
# # # # remove unnecessary columns
# # # df = df[['confidence_limit_high', 'question', 'year', 'locationdesc', 'response', 'confidence_limit_low', 'sample_size']]
# # # # remove rows with NaN values in confidence limit high/low
# # # df.dropna(subset=['confidence_limit_high'], inplace=True)
# # # df.dropna(subset=['confidence_limit_low'], inplace=True)
# # # print(df)
# # # df2 = df.groupby(['question','response']).count()
# # # df2 = df.groupby(['question','response']).aggregate({'year':"count"})
# # # # df2.drop(['confidence_limit_high', 'locationdesc', 'confidence_limit_low'], axis=1, inplace=True)
# # # df2.rename(columns={'year':'number of responses'}, inplace=True)
# # # df3 = df.groupby(['question', 'response', 'locationdesc']).aggregate({'sample_size':'sum'})
# # print(df)
# import requests
# import pandas as pd
# import json
# from pandas import json_normalize
# import copy
# import re

# resp = requests.get("https://chronicdata.cdc.gov/api/views/bq95-jg9r/rows.json?")
# json = resp.json()
# # print(json['data'])
# # create dataframe from json
# listoflists = json['data']
# for idx in range(len(listoflists)):
#     row = copy.deepcopy(listoflists[idx])
#     row = row[8:]
#     row = row[:-2]
#     listoflists[idx] = row
# headers = json['meta']['view']['columns']
# headers = headers[8:]
# headers = headers[:-2]
# for idx, column in enumerate(headers):
#     column_name = column['fieldName']
#     headers[idx] = column_name
# df = pd.DataFrame(data=listoflists, columns=headers)
# df = df[['confidence_limit_high', 'question', 'year', 'locationdesc', 'data_value','response', 'confidence_limit_low', 'sample_size']]
# # remove rows with NaN values in confidence limit high/low
# df.dropna(subset=['confidence_limit_high'], inplace=True)
# df.dropna(subset=['confidence_limit_low'], inplace=True)
# df['sample_size'] = df['sample_size'].astype(int)
# df['data_value'] = df['data_value'].astype(float)
# df['year'] = df['year'].astype(int)
# df_selected = df.loc[df['year'] < 2020]
# df = df.drop(df_selected.index)
# question = "Adults who are current smokers (variable calculated from one or more BRFSS questions)"
# question = re.escape(question)
# df = df[df['question'].str.contains(question)]
# df = df[df['response'].str.contains('Yes')]
# df['confidence_limit_low'] = df['confidence_limit_low'].astype(float)
# df['confidence_limit_high'] = df['confidence_limit_high'].astype(float)
# df2 = df.groupby(['question','response']).aggregate({'data_value':'mean','sample_size':'sum'})
# df3 = df.groupby(['locationdesc', 'question','response']).aggregate({'data_value':'mean','confidence_limit_low':'mean', 'confidence_limit_high':'mean','sample_size':'sum'})
# df3.to_csv('Cleaned_BRFSS__Table_of_Tobacco_Use_GroupBy_Location_Question_Response.csv')

def summary1():
  df1 = pd.read_csv("Cleaned_BRFSS__Table_of_Tobacco_Use.csv")
  df2 = pd.read_csv("Cleaned_BRFSS__Table_of_Tobacco_Use_GroupBy_Location_Question_Response.csv")
  df3 = pd.read_csv("Cleaned_BRFSS__Table_of_Tobacco_Use_GroupBy_Question_Response.csv")
  df4 = pd.read_csv('Cleaned_Obesity_Stats_By_States.csv')
  df5 = pd.read_csv('Cleaned_Provisional_COVID-19_Deaths_by_HHS_Region__Race__and_Age.csv')
  df6 = pd.read_csv('Cleaned_Provisional_COVID-19_Deaths_by_HHS_Region__Race__and_Age_Group_By_Group_By_Location.csv')
  df7 = pd.read_csv('Cleaned_Provisional_COVID-19_Deaths_by_HHS_Region__Race__and_Age_Group_By_Time_Period.csv')
  writer = pd.ExcelWriter("summary.xlsx", engine="xlsxwriter")
  df1.to_excel(writer, sheet_name="Sheet1")
  df2.to_excel(writer, sheet_name="Sheet2")
  df3.to_excel(writer, sheet_name="Sheet3")
  df4.to_excel(writer, sheet_name="Sheet4")
  df5.to_excel(writer, sheet_name="Sheet5")
  df6.to_excel(writer, sheet_name="Sheet6")
  df7.to_excel(writer, sheet_name="Sheet7")
  writer.save()
############ Function Call ############
summary1()