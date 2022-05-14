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

# Persiapan driver Chrome
driver = webdriver.Chrome('D:/Megabagusid/Python Masterclass/Driver Chrome/chromedriver.exe', options=options) # Ganti sesuai lokasi path komputer Anda

# Masuk ke website Jobstreet
driver.get('https://www.jobstreet.co.id/')
time.sleep(5)

kotak_input = driver.find_element_by_xpath(('//*[@id="locationAutoSuggest"]'))
# Coba kita masukkan kota semarang --> silakan diubah sendiri, atau biarkan saja kosong
kotak_input.send_keys('semarang')

# Pencet tombol CARI
tombol_cari = driver.find_element_by_xpath('//*[@id="contentContainer"]/div/div[1]/div/div/div/div[2]/div/form/div/div/div[2]/div[4]/button').click()
time.sleep(5)

# Persiapkan dataframe untuk menyimpan informasinya
dataku = pd.DataFrame({'Link':[], 'Posisi':[], 'Perusahaan':[], 'Gaji':[], 'Lokasi':[], 'Tanggal':[]})

'''
ini adalah step awal sebelum dimasukkan ke while loop

# merubah ke lxml
soup = BeautifulSoup(driver.page_source, 'lxml')
postings = soup.find_all('div', class_='sx2jih0 zcydq82k zcydq89w zcydq81w zcydq8r zcydq832')

for post in postings:
    link = post.find('a', class_='DvvsL_0 _1p9OP').get('href')
    link_lengkap = 'https://www.jobstreet.co.id'+link
    posisi = post.find('div', class_='sx2jih0 _2j8fZ_0 sIMFL_0 _1JtWu_0').text
    perusahaan = post.find('span', class_='sx2jih0 zcydq82b zcydq8r iwjz4h0').text
    lokasi = post.find('span', class_='sx2jih0 zcydq82b _18qlyvc0 _18qlyvcv _18qlyvc3 _18qlyvc6').text
    tanggal = post.find('span', class_='sx2jih0 zcydq82b _18qlyvc0 _18qlyvcx _18qlyvc1 _18qlyvc6').text
    try:
        gaji = post.find_all('span', class_='sx2jih0 zcydq82b _18qlyvc0 _18qlyvcv _18qlyvc3 _18qlyvc6')[1].text
    except:
        gaji='NA'
    dataku = dataku.append(
        {'Link': link_lengkap,
         'Posisi': posisi,
         'Perusahaan': perusahaan,
         'Gaji': gaji,
         'Lokasi': lokasi,
         'Tanggal': tanggal}, ignore_index=True)
'''

# Merangkai semuanya
i = 0
while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all('div', class_='sx2jih0 zcydq82k zcydq89w zcydq81w zcydq8r zcydq832')
    i += 1
    # looping postings
    for post in postings:
        link = post.find('a', class_='DvvsL_0 _1p9OP').get('href')
        link_lengkap = 'https://www.jobstreet.co.id'+link
        posisi = post.find('div', class_='sx2jih0 _2j8fZ_0 sIMFL_0 _1JtWu_0').text
        perusahaan = post.find('span', class_='sx2jih0 zcydq82b zcydq8r iwjz4h0').text
        lokasi = post.find('span', class_='sx2jih0 zcydq82b _18qlyvc0 _18qlyvcv _18qlyvc3 _18qlyvc6').text
        tanggal = post.find('span', class_='sx2jih0 zcydq82b _18qlyvc0 _18qlyvcx _18qlyvc1 _18qlyvc6').text
        try:
            gaji = post.find_all('span', class_='sx2jih0 zcydq82b _18qlyvc0 _18qlyvcv _18qlyvc3 _18qlyvc6')[1].text
        except:
            gaji='NA'
        dataku = dataku.append({'Link': link_lengkap,
                                'Posisi': posisi,
                                'Perusahaan': perusahaan,
                                'Gaji': gaji,
                                'Lokasi': lokasi,
                                'Tanggal': tanggal},
                               ignore_index=True)
    
    # Mencoba untuk menuju halaman selanjutnya
    if i==1:
        try:
            lanjut = soup.find('a', class_='sx2jih0 zcydq85e zcydq84n zcydq88 zcydq81x zcydq82k zcydq898 zcydq81q zcydq827 zcydq826 _1ouuf_0').get('href')
            driver.get('https://www.jobstreet.co.id'+lanjut)
        except:
            break 
    else:
        try:
            lanjut = soup.find_all('a', class_='sx2jih0 zcydq85e zcydq84n zcydq88 zcydq81x zcydq82k zcydq898 zcydq81q zcydq827 zcydq826 _1ouuf_0')[1].get('href')
            driver.get('https://www.jobstreet.co.id'+lanjut)
        except:
            break 

# Export semuanya ke csv
dataku.to_csv('daftar_lowongan.csv')
