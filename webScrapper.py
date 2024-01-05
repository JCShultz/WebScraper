from bs4 import BeautifulSoup
import requests

def scrapeBlogs():
  #scrape LinkedIn search
  pageToScrape = requests.get("https://www.tapaway.com.au/blog")
  soup = BeautifulSoup(pageToScrape.text, "html.parser")
  authors = soup.findAll('span', attrs= {'class':'tQ0Q1A'})
  titles = soup.findAll('a', attrs= {'class':'O16KGI pu51Xe lyd6fK mqysW5 has-custom-focus i6wKmL'})
  views = soup.findAll('span', attrs= {'class':'eYQJQu'})


  # PRINTS AUTHORS
  #for author in authors:
  #  print(author.text)

  # PRINTS TITLES
  #for title in titles:
  #  print(title.text)

  for author, title, view in zip(authors, titles, views):
    print(author.text + " - " + title.text + ' - Views: ' + view.text)

scrapeBlogs()