from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'
page =  requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#gets table containing desired scraping info
table = soup.find('table', class_= 'wikitable sortable')

#gets first column
columns = table.find('tr')
column_names = columns.find_all('th')
column_titles = [title.text.strip() for title in column_names]

#gets rows with in table
body = table.find('tbody')
rows = body.find_all('tr')
row_values = [value.text.split("\n") for value in rows]

#cleans empty strings from row_values
for row in row_values:
  for element in row:
    element.strip()
    if(element == ''):
      row.remove(element)
  print(row)

  #creates .csv of information scrapped from Wiki
  df = pd.DataFrame(row_values)
  df.to_csv('Top 50 Largest Companies in the World by Revenue.csv', index=False, encoding='utf-8')

