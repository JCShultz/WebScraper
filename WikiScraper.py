from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'
page =  requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('table', class_= 'wikitable sortable')
columns = table.find('tr')
column_names = columns.find_all('th')
column_titles = [title.text.strip() for title in column_names]



print(column_titles)




#print(column_data)