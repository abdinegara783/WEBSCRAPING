from bs4 import BeautifulSoup
import requests

url = 'https://www.goat.com/sneakers'
requests.get(url)
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
soup

postings = soup.find_all('div', class_='Grid__CellWrapper-sc-1njij7e-0 joqMUS')
postings
# Website ini dibangun mayoritas dengan JavaScript

from selenium import webdriver
driver = webdriver.Chrome('D:/Megabagusid/Python Masterclass/Driver Chrome/chromedriver_win32/chromedriver.exe')
driver.get(url)
