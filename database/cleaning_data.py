
#Dependencies
import pandas as pd
import os
from config import key
from sqlalchemy import create_engine

#### DEATHS BY RISK FACTOR
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
#print(countries_df.info())

#Join in order to only keep countries & Keep necessary columns

deathsdf_c = pd.merge(deathsdf, countries_df, on='Country_Code')
deathsdf_c = deathsdf_c.iloc[:, 0:10]
#print(deathsdf_c.info())


#Data Normalization
deathsdf_transformed = deathsdf_c.melt(id_vars = ['Country_Name_x', 'Country_Code', 'Year'], var_name = 'risk_factor', value_name='number_deaths')
#Name columns match with table in database
deathsdf_transformed.columns = ['country_name', 'country_code', 'year', 'risk_factor', 'number_of_deaths']
#print(deathsdf_transformed)


###HEIGHT 
#Read Files
height_w_df = pd.read_csv(f'{read_path}/average-height-of-women.csv')
height_m_df = pd.read_csv(f'{read_path}/average-height-of-men.csv')

#Rename columns 
height_w_df.columns = ['Country_Name', 'Country_Code', 'Birth_Year', 'Height']
height_m_df.columns = ['Country_Name', 'Country_Code', 'Birth_Year', 'Height']
#Group by Year of birth
height_w_df = height_w_df.groupby(['Country_Name', 'Country_Code'])['Height'].mean()
height_m_df = height_m_df.groupby(['Country_Name', 'Country_Code'])['Height'].mean()

#Reset index
height_w_df = height_w_df.reset_index()
height_m_df = height_m_df.reset_index()

#Join women & men tables to have just one height table
height_df = pd.merge(height_w_df, height_m_df, on=(['Country_Code', 'Country_Name']), suffixes= ('_women', '_men'))

#Join in order to only keep countries & Keep necessary columns
height_c = pd.merge(height_df, countries_df, on='Country_Code')
height_c = height_c.iloc[:, 0:4]

#Data Normalization
height_c.columns = ['country_name', 'country_code', 'Female', 'Male']
height_transformed = height_c.melt(id_vars = ['country_name', 'country_code'], var_name = 'sex', value_name='height')
#print(height_transformed.head())



#Create database connection

db_url = f'postgresql://postgres:{key}@localhost:5432/health_db'
engine = create_engine(db_url)

#Confirm tables
print(engine.table_names())

#Load DataFrame into database

deathsdf_transformed.to_sql(name = 'deaths_risk_factors',
                            con = engine,
                            if_exists= 'append',
                            index = False)

height_transformed.to_sql(name = 'height',
                            con = engine,
                            if_exists= 'append',
                            index = False)



