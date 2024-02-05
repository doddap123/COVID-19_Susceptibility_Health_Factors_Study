import pandas as pd
import numpy as np
def insight1():
  df = pd.read_csv('Cleaned_BRFSS__Table_of_Tobacco_Use_GroupBy_Location_Question_Response.csv', low_memory=False)

  hhs_region_dict = {'Connecticut': 1, 'Maine': 1, 'Massachusetts': 1, 'New Hampshire': 1, 'Rhode Island': 1,'Vermont': 1,
  'New York': 2, 'New Jersey': 2, 'Puerto Rico': 2, 'Virgin Islands': 2, 'Delaware': 3, 'Maryland':3, 'Pennsylvania':3, 'Virginia':3,
   'West Virginia':3, 'District of Columbia': 3, 'Alabama': 4, 'Florida': 4, 'Georgia': 4, 'Kentucky': 4, 'Mississippi': 4, 'North Carolina': 4,
    'South Carolina': 4,'Tennessee': 4, 'Illinois': 5, 'Indiana': 5, 'Michigan': 5, 'Minnesota': 5, 'Ohio': 5, 'Wisconsin': 5,
    'Arkansas': 6, 'Louisiana': 6,'New Mexico': 6, 'Oklahoma': 6, 'Texas': 6, 'Iowa': 7, 'Nebraska': 7, 'Missouri':7, 'Kansas':7,
    'Colorado':8, 'Montana':8, 'North Dakota':8, 'South Dakota':8, 'Utah':8, 'Wyoming':8, 'Arizona':9, 'California':9, 'Hawaii':9, 'Nevada':9, 
    'Guam':9, 'Alaska':10, 'Idaho':10, 'Oregon':10, 'Washington':10}
  df['HHS Region'] = df.apply(lambda row: hhs_region_dict[row.locationdesc], axis=1)
  tobacco_hhs = df.groupby(['HHS Region', 'question','response']).aggregate({'data_value':'mean', 'confidence_limit_low': 'mean', 'confidence_limit_high': 'mean', 'sample_size':'sum'})
#   tobacco_hhs.to_csv('bruh.csv')
  covid_hhs = pd.read_csv('Cleaned_Provisional_COVID-19_Deaths_by_HHS_Region__Race__and_Age_Group_By_Group_By_Location.csv', low_memory=False)
  covid_hhs = covid_hhs[:-1]
  covid_hhs['HHS Region'] = covid_hhs['HHS Region'].astype(int)
  combined = pd.merge(tobacco_hhs, covid_hhs, on=['HHS Region'] ,how='left')
  combined = combined.rename(columns={'data_value': 'Percentage of Adults who are Current Smokers'})
  with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(tobacco_hhs)
  combined['Percentage of Adults who are Current Smokers'] = combined['Percentage of Adults who are Current Smokers']/100
  corr = combined['Percentage of Adults who are Current Smokers'].corr(combined['Proportion of Covid Deaths to Total Deaths'])
  print(corr)
  pass
def insight2():
    obesity = pd.read_csv('Cleaned_Obesity_Stats_By_States.csv', low_memory=False)
    covid_hhs = pd.read_csv('Cleaned_Provisional_COVID-19_Deaths_by_HHS_Region__Race__and_Age_Group_By_Group_By_Location.csv', low_memory=False)
    hhs_region_dict = {'Connecticut': 1, 'Maine': 1, 'Massachusetts': 1, 'New Hampshire': 1, 'Rhode Island': 1,'Vermont': 1,
  'New York': 2, 'New Jersey': 2, 'Puerto Rico': 2, 'Virgin Islands': 2, 'Delaware': 3, 'Maryland':3, 'Pennsylvania':3, 'Virginia':3,
   'West Virginia':3, 'District of Columbia': 3, 'Alabama': 4, 'Florida': 4, 'Georgia': 4, 'Kentucky': 4, 'Mississippi': 4, 'North Carolina': 4,
    'South Carolina': 4,'Tennessee': 4, 'Illinois': 5, 'Indiana': 5, 'Michigan': 5, 'Minnesota': 5, 'Ohio': 5, 'Wisconsin': 5,
    'Arkansas': 6, 'Louisiana': 6,'New Mexico': 6, 'Oklahoma': 6, 'Texas': 6, 'Iowa': 7, 'Nebraska': 7, 'Missouri':7, 'Kansas':7,
    'Colorado':8, 'Montana':8, 'North Dakota':8, 'South Dakota':8, 'Utah':8, 'Wyoming':8, 'Arizona':9, 'California':9, 'Hawaii':9, 'Nevada':9, 
    'Guam':9, 'Alaska':10, 'Idaho':10, 'Oregon':10, 'Washington':10}
    obesity = obesity.rename(columns={'States, district, & territories\n': 'states'})
    obesity['states'] = obesity['states'].apply(str.strip)
    obesity['HHS Region'] = obesity.apply(lambda row: hhs_region_dict[row.states], axis=1)
    obesity["Overweight (incl. obese) adults(mid-2000s)\n"] = obesity["Overweight (incl. obese) adults(mid-2000s)\n"].str.replace("%","").astype(float)
    obesity["Obese children and adolescents(mid-2000s)"] = obesity["Obese children and adolescents(mid-2000s)"].str.replace("%","").astype(float)
    obesity["Obese adults (2020)"] = obesity["Obese adults (2020)"].str.replace("%","").astype(float)
    obesity["Obese adults (mid-2000s)\n"] = obesity["Obese adults (mid-2000s)\n"].str.replace("%","").astype(float)
    obesity = obesity.groupby(['HHS Region']).aggregate({"Overweight (incl. obese) adults(mid-2000s)\n":'mean', "Obese children and adolescents(mid-2000s)": 'mean', "Obese adults (2020)": 'mean', "Obese adults (mid-2000s)\n":'mean'})
    covid_hhs = covid_hhs[:-1]
    covid_hhs['HHS Region'] = covid_hhs['HHS Region'].astype(int)
    combined = pd.merge(obesity, covid_hhs, on=['HHS Region'],how='left')
    combined['Proportion of Covid Deaths to Total Deaths'] = combined['Proportion of Covid Deaths to Total Deaths']*100
    combined.to_clipboard()
    # print(combined)
    corr = combined['Obese adults (2020)'].corr(combined['Proportion of Covid Deaths to Total Deaths'])
    print(corr)

    # covid_hhs['HHS Region'] = covid_hhs.apply(lambda row: hhs_region_dict[row.states], axis=1)
    pass




############ Function Call ############
# insight1()
insight2()