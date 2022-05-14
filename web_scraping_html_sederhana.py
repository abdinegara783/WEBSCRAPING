# Mengimpor library
from bs4 import BeautifulSoup
import requests # library request digunakan untuk memanggil server

# Menuliskan alamat website dengan objek url
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'

# Meminta server hosting untuk mengambil url
requests.get(url)
# Jika hasilnya adalah [200] maka server membolehkan kita mengakses websitenya

halaman = requests.get(url)
halaman.text

# parser-lxml = Merubah format html menjadi format Python
soup = BeautifulSoup(halaman.text, 'lxml')
soup

# Mengakses tag header
soup.header

# Mengakses tag div
soup.div

# Tag adalah yang dimulai dengan tanda <, dan biasnaya berwarna ungu
# Mengambil tag h1
soup.h1

# Mengambil string dari tag dalam tag (nested tag)
soup.header.p
soup.header.p.string

# Mengambil tag a dalam <header>
a_awal = soup.header.a
a_awal

# Mendapatkan attributes nya saja
a_awal.attrs
a_awal['data-target']
a_awal['atribut-baru'] = 'ini adalah yang baru lo'
a_awal.attrs
a_awal

# Kombinasi tag <header> dan tag <div>
soup.header.div

# Mencari attribute tertentu dalam sebuah tag
soup.find('div', {'class':'side-collapse in'})
soup.find('div', {'id':'layout-footer'})
soup.find('div', class_ = 'side-collapse in')
soup.find('h4', class_ = 'pull-right price')

# Menggunakan find_all
soup.find_all('h4', class_ = 'pull-right price')

# Slicing hasil find_all
soup.find_all('h4', class_ = 'pull-right price')[2:5]

# Menggunakan filter beberapa tag sekaligus
soup.find_all(['h4', 'a', 'p'])
soup.find_all(['header', 'div'])
soup.find_all(id = True)
soup.find_all(class_ = True)

# Filter berdasarkan nama
nama = soup.find_all('a', class_='title')

# Filter berdasarkan harga
harga = soup.find_all('h4', class_ = 'pull-right price')

# Filter berdasarkan reviews
reviews = soup.find_all('p', class_ = 'pull-right')

# Filter berdasarkan deskripsi
deskripsi = soup.find_all('p', class_ = 'description')

harga1 = soup.find('h4', class_ = 'pull-right price')

# Membuat string dari list find_all
nama_produk_list = []
for i in nama:
    name = i.text
    nama_produk_list.append(name)

harga_list = []
for i in harga:
    price = i.text
    harga_list.append(price)

review_list = []
for i in reviews:
    riviw = i.text
    review_list.append(riviw)
    
deskripsi_list = []
for i in deskripsi:
    desk = i.text
    deskripsi_list.append(desk)

# Mengonversi semuanya ke dalam format DataFrame    
import pandas as pd
tabel = pd.DataFrame({'Nama Produk': nama_produk_list,
                      'Harga': harga_list,
                      'Reviews': review_list,
                      'Deskripsi Produk': deskripsi_list})    
    
