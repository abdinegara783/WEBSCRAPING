from bs4 import BeautifulSoup
import requests

url = 'https://www.goat.com/sneakers'
requests.get(url)
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
soup

postings = soup.find_all('div', class_='ProductTemplatePriceDisplay__LowestPrice-nfz87-3 dHaKT')
postings

from selenium import webdriver
driver = webdriver.Chrome('D:/Megabagusid/Python Masterclass/Driver Chrome/chromedriver.exe')
driver.get(url)

# Belajar menggunakan XPath (ekspresi lokasi untuk menuju ke html/xml)
driver.find_element_by_xpath('//*[@id="0"]/div[2]/div/p/span').text
driver.find_element_by_xpath('//*[@id="1"]/div[2]/h2').text
# Menggunakan full XPath
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[3]/div[4]/div/ul/div[1]/div[1]/div/a/div/div/div[2]/div/p/span').text
# Merubah nomor id
driver.find_element_by_xpath('//*[@id="0"]/div[2]/div/p/span').text
driver.find_element_by_xpath('//*[@id="1"]/div[2]/div/p/span').text
driver.find_element_by_xpath('//*[@id="2"]/div[2]/div/p/span').text
driver.find_element_by_xpath('//*[@id="0"]/div[2]/h2').text
driver.find_element_by_xpath('//*[@id="1"]/div[2]/h2').text
driver.find_element_by_xpath('//*[@id="2"]/div[2]/h2').text

# Scraping dengan for loop
for i in range(0,20):
    harga = driver.find_element_by_xpath('//*[@id="'+str(i)+'"]/div[2]/div/p/span').text
    nama = driver.find_element_by_xpath('//*[@id="'+str(i)+'"]/div[2]/h2').text
    if (i==0):
        print('='*15,'List Produk','='*15)
    print(nama,'=',harga)
    
url2 = 'https://www.google.com'
driver.get(url2)

# Belajar memasukkan input dan menggunakan keyboard
from selenium.webdriver.common.keys import Keys    
kotak = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')    
kotak.send_keys('wisata Indonesia')    
kotak.send_keys(Keys.ENTER)    

# Belajar menggunakan klik kiri
kotak = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')    
kotak.send_keys('masyarakat Indonesia')       
kotak.send_keys(Keys.ESCAPE) 
tombol = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
tombol.click()
driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()


# Kembali ke Goat.com
driver.get(url)
# mengambil screenshot
driver.save_screenshot('D:\Megabagusid\Python Masterclass\Web scraping\semua.png')
# mengambil satu gambar
driver.find_element_by_xpath('//*[@id="3"]/img').screenshot('D:\Megabagusid\Python Masterclass\Web scraping\item1.png')

# Belajar scrolling halaman
driver.execute_script('return document.body.scrollHeight')
driver.execute_script('window.scrollTo(0,20000)')
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
driver.execute_script('window.scrollTo(0,document.body.scrollHeight-2000)')
# infinite scrolling
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight-2000)')

# Belajar mengatur jeda waktu
driver.get(url2)
import time

kotak = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')    
kotak.send_keys('wisata Indonesia') 
time.sleep(10)   
kotak.send_keys(Keys.ENTER)   