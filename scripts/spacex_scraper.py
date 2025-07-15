
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Wikipedia URL for Falcon 9 and Falcon Heavy launches
url = 'https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches'

# Send GET request and parse content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all tables (one per year)
tables = soup.find_all('table', {'class': 'wikitable'})

# Initialize an empty list to store dataframes
df_list = []

for table in tables:
    try:
        df = pd.read_html(str(table))[0]
        df_list.append(df)
    except Exception as e:
        print(f"Skipping a table due to error: {e}")

# Combine all tables into one dataframe
launch_df = pd.concat(df_list, ignore_index=True)

# Save raw scraped data
launch_df.to_csv('../data/raw_spacex_launches.csv', index=False)

print("✅ Scraping complete. Data saved to 'data/raw_spacex_launches.csv'")
