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
driver = webdriver.Chrome('D:/Megabagusid/Python Masterclass/Driver Chrome/chromedriver.exe', options=options) # Ganti sesuai lokasi driver chrome di komputer Anda

# Masuk ke website Jobstreet
driver.get('https://www.jobstreet.co.id/')
time.sleep(5)

# memasukkan kota semarang
kotak_input = driver.find_element_by_xpath('//*[@id="locationAutoSuggest"]')
# coba kita masukkan kota semarang --> bisa diganti terserah
kotak_input.send_keys('semarang')

# Menekan tombol cari
tombol_cari = driver.find_element_by_xpath('//*[@id="contentContainer"]/div/div[1]/div/div/div/div[2]/div/form/div/div/div[2]/div[4]/button').click()
time.sleep(5)

# Persiapkan dataframe
dataku = pd.DataFrame({'Link':[],
                       'Posisi':[],
                       'Perusahaan':[],
                       'Gaji':[],
                       'Lokasi':[],
                       'Tanggal':[]})

# Merubah ke lxml python
soup = BeautifulSoup(driver.page_source, 'lxml')
postings = soup.find_all('div', class_='sx2jih0 zcydq83w zcydq835 zcydq85e zcydq84n zcydq81w zcydq82k zcydq89w zcydq89n')

# Mulai looping
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
dataku.to_csv('D:/Megabagusid/Python Masterclass/daftar_lowongan.csv') # sesuaikan dengan direktori kita ingin menyimpan file csv nya

############################
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
import datetime 

# Masukkan email pengirim dan penerima
pengirim = '' # masukkan email pengirim (email robot)
penerima = '' # masukkan tujuan email 

# Menambah keterangan waktu di email
waktu = datetime.datetime.now() 

# Kirim email dan tentukan Subject, From dan To
msg = MIMEMultipart()
msg['Subject'] = 'Lowongan Pekerjaan Baru Jobstreet' # sesuaikan judulnya
msg['From'] = pengirim
msg['To'] = ''.join(penerima)
#text = "Ini adalah email dari robot webscraping:\n===========================\nLowongan pekerjaan baru pada %s \n===========================\n\n\n===========================\n\n" % (waktu)
text = "Ini adalah email dari robot webscraping:\n===========================\nLowongan pekerjaan baru pada: \n===========================\n{}-{}-{}\npukul {}:{}\n===========================\n\n".format(
    waktu.day, 
    waktu.month,
    waktu.year,
    waktu.hour,
    waktu.minute)

msg.attach(MIMEText(text, 'plain'))

# Kirim file yang ingin dikirimkan
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('D:/Megabagusid/Python Masterclass/daftar_lowongan.csv', 'rb').read()) # sesuaikan dengan direktori file csv kita
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="daftar_lowongan.csv"')
msg.attach(part)

# Masuk ke login email kita
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = '', password = '') # masukkan user (email pengirim) dan password dengan benar
s.sendmail(pengirim, penerima, msg.as_string())
s.quit()