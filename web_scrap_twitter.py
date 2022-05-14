# Mengimpor library
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd

# Persiapan layar maximize
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# persiapan driver Chrome
driver = webdriver.Chrome('D:/Megabagusid/Python Masterclass/Driver Chrome/chromedriver.exe', options=options)

# Masuk ke web twitter
driver.get('https://twitter.com/login')
time.sleep(2)

# Memasukkan username dan password
login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
login.send_keys('') # masukkan username twitter Anda
password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
password.send_keys('') # masukkan password twitter Anda
tombol = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/label/div[2]/div/input')))

# Menulis di kolom search
cari = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/label/div[2]/div/input')
target_cari = 'Elon Musk' # Bisa langsung diganti nama target
cari.send_keys(target_cari)
cari.send_keys(Keys.ENTER)
time.sleep(5)
orang = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a').click()
time.sleep(5)
pilihan = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[1]/div/div/div/div[2]/div/div[1]/a/div/div[1]/div[1]/span/span').click()

# Merubah HTML ke Python
soup = BeautifulSoup(driver.page_source, 'lxml')
postings = soup.find_all('div', class_='css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')

# cek tinggi
driver.execute_script('return document.body.scrollHeight')

# Persiapan dataframe awal
twit = pd.DataFrame({'isi':[]})

# Loop untuk mengambil semua twit
i = 0
while True:
    i = i+1
    for post in postings:
        twit = twit.append({'isi':post.text}, ignore_index=True)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight-2000)') #setting lagi tinggi layar
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all('div', class_ = 'css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
    print(i)
    if twit.index.stop > 200:
        break

twit_final = twit.copy()
twit_final.drop_duplicates(subset='isi', keep='first',inplace=True)
twit_final.reset_index(inplace = True)
twit_final.drop(['index'], axis = 1, inplace=True)

# Export ke csv
twit_final.to_csv('twit_elon.csv', index=False)

# Baca csv
coba = pd.read_csv('twit_elon.csv')

# Mencari kata Tesla
kata_tesla = []
for i in range(len(twit_final)):
    if 'tesla' in twit_final.isi[i].lower():
        kata_tesla.append(twit_final.isi[i])