"""
Here we are going insife rithmschool.com/blog website and scraping the blogs. after scraping, we will write them
inside a csv file
"""
import requests
from bs4 import BeautifulSoup
from csv import writer

def scrapBlogs():
    response = requests.get("https://www.rithmschool.com/blog")
    soup = BeautifulSoup(response.text,"html.parser")
    articles = soup.find_all("article")
    with open("scrapped.csv","w") as file:
        csv_writer = writer(file)
        csv_writer.writerow(["title","link","date"])
        for item in articles:
            a_tag = item.find("a")
            title = a_tag.get_text()
            link = a_tag["href"]
            date = item.find("time")["datetime"]
            csv_writer.writerow([title,link,date])