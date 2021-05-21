
#Dependencies
import pandas as pd
import os
from sqlalchemy import create_engine

#Extract CSV into DataFrames

read_path = os.path.join('Resources')
deaths_df = pd.read_csv(f'{read_path}/number-of-deaths-by-risk-factor.csv')

#Keep columns useful for analysis

cols_deaths = [ 'Entity',
                'Code',
                'Year',
                'Deaths - Secondhand smoke - Sex: Both - Age: All Ages (Number)', 
                'Deaths - Alcohol use - Sex: Both - Age: All Ages (Number)',
                'Deaths - Diet low in fruits - Sex: Both - Age: All Ages (Number)',
                'Deaths - Diet low in vegetables - Sex: Both - Age: All Ages (Number)',
                'Deaths - Low physical activity - Sex: Both - Age: All Ages (Number)',
                'Deaths - High body-mass index - Sex: Both - Age: All Ages (Number)',
                'Deaths - Smoking - Sex: Both - Age: All Ages (Number)',
                ]

deathsdf = deaths_df[cols_deaths].copy()
#Rename columns
cols_rename = {'Entity': 'Country_Name',
                'Code': 'Country_Code',
                'Deaths - Secondhand smoke - Sex: Both - Age: All Ages (Number)': 'Secondhand smoke',
                'Deaths - Alcohol use - Sex: Both - Age: All Ages (Number)' : 'Alcohol use',
                'Deaths - Diet low in fruits - Sex: Both - Age: All Ages (Number)': 'Diet low in fruits',
                'Deaths - Diet low in vegetables - Sex: Both - Age: All Ages (Number)': 'Diet low in vegetables',
                'Deaths - Low physical activity - Sex: Both - Age: All Ages (Number)': 'Low physical activity',
                'Deaths - High body-mass index - Sex: Both - Age: All Ages (Number)': 'High body-mass index',
                'Deaths - Smoking - Sex: Both - Age: All Ages (Number)': 'Smoking'
                }
deathsdf = deathsdf.rename(columns = cols_rename)

#Take most recent year of data (2017)

deathsdf = deathsdf[(deathsdf.Year==2017)]
#Review columns
print(deathsdf.info())

#Scrape Countries & Codes

url = 'https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes'
table = pd.read_html(url)

#Slice to DataFrame & Drop Level 0
countries_df = table[0]
countries_df.columns = countries_df.columns.droplevel(0)
#Select only necessary columns & change name
countries_df = countries_df[['Country name[5]', 'Alpha-3 code[5]']]
countries_df.columns = ['Country_Name', 'Country_Code']
#Review columns
print(countries_df.info())

#Join in order to only keep countries

deathsdf_c = pd.merge(deathsdf, countries_df, on='Country_Code')
print(deathsdf_c.info())



#Data Normalization
#deathsdf_transformed = deathsdf.melt(id_vars = ['Entity', 'Code', 'Year'], var_name = 'risk_factor', value_name='number_deaths')
#print(deathsdf_transformed.head())

#Write Path

#write_path = os.path.join('Output/')
#entities.to_csv(f'{write_path}entities.csv')


