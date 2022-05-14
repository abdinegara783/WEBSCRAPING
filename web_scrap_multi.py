# mengimpor library
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Membuat object url
url = 'https://www.airbnb.com/s/Tangerang-Selatan--South-Tangerang-City--Banten--Indonesia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Tangerang%20Selatan%2C%20South%20Tangerang%20City%2C%20Banten%2C%20Indonesia&place_id=ChIJlcAZBLH6aS4R5K9KLBxIBoc&checkin=2021-04-01&checkout=2021-04-02&adults=1&source=structured_search_input_header&search_type=autocomplete_click'

# Membuat object page
page = requests.get(url)
page

# Mengambil informasi website 'page'
soup = BeautifulSoup(page.text, 'lxml')
soup

# Sekarang tutorial untuk pergi ke setiap halaman (1,2,3,dst)
hal_next = soup.find('a',{'aria-label':'Next'}).get('href')
hal_next

# menambahkan domain depan
hal_next_lengkap = 'https://www.airbnb.com'+hal_next
hal_next_lengkap

# Mulai seperti tahap awal
url = 'https://www.airbnb.com/s/Tangerang-Selatan--South-Tangerang-City--Banten--Indonesia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Tangerang%20Selatan%2C%20South%20Tangerang%20City%2C%20Banten%2C%20Indonesia&place_id=ChIJlcAZBLH6aS4R5K9KLBxIBoc&checkin=2021-04-01&checkout=2021-04-02&adults=1&source=structured_search_input_header&search_type=autocomplete_click'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

dataku = pd.DataFrame({'Links':[''], 'Judul':[''], 'Deskripsi':[''], 'Harga':[''], 'Rating':['']})

# Lakukan loop mencari panah sampai tidak ada (hal ke 15)
while True:   
    postings = soup.find_all('div', class_ = '_8ssblpx')
    for post in postings:
        try:
            link = post.find('a', class_='_gjfol0').get('href')
            link_lengkap = 'https://www.airbnb.com'+link
            judul = post.find('a', class_='_gjfol0').get('aria-label')
            harga = post.find('span', class_='_olc9rf0').text
            rating = post.find('span', class_='_10fy1f8').text
            deskripsi = post.find('div', class_='_kqh46o').text
            dataku = dataku.append({'Links':link_lengkap, 'Judul':judul, 
                                    'Deskripsi':deskripsi, 'Harga':harga, 'Rating':rating}, 
                                   ignore_index=True)
        except:
            pass
    
    try:
        hal_next = soup.find('a',{'aria-label':'Next'}).get('href')
        hal_next_lengkap = 'https://www.airbnb.com'+hal_next
        hal_next_lengkap
    except:
        print('Index sudah selesai')
        break
    
    url = hal_next_lengkap
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

#### tanpa rating ###
url = 'https://www.airbnb.com/s/Tangerang-Selatan--South-Tangerang-City--Banten--Indonesia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Tangerang%20Selatan%2C%20South%20Tangerang%20City%2C%20Banten%2C%20Indonesia&place_id=ChIJlcAZBLH6aS4R5K9KLBxIBoc&checkin=2021-04-01&checkout=2021-04-02&adults=1&source=structured_search_input_header&search_type=autocomplete_click'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
dataku2 = pd.DataFrame({'Links':[''], 'Judul':[''], 'Deskripsi':[''], 'Harga':['']})
postings = soup.find_all('div', class_ = '_8ssblpx')

while True:
    postings = soup.find_all('div', class_ = '_8ssblpx')
    for post in postings:
        link = post.find('a', class_='_gjfol0').get('href')
        link_lengkap = 'https://www.airbnb.com'+link
        judul = post.find('a', class_='_gjfol0').get('aria-label')
        harga = post.find('span', class_='_olc9rf0').text
        deskripsi = post.find('div', class_='_kqh46o').text
        dataku2 = dataku2.append({'Links':link_lengkap, 'Judul':judul, 
                                  'Deskripsi':deskripsi, 'Harga':harga}, 
                                 ignore_index=True)
    
    try:
        hal_next = soup.find('a',{'aria-label':'Next'}).get('href')
        hal_next_lengkap = 'https://www.airbnb.com'+hal_next
        hal_next_lengkap
    except:
        print('Index sudah selesai')
        break
    
    url = hal_next_lengkap
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
# Menghilangkan baris pertama
dataku2 = dataku2.iloc[1:]

# Menghilangkan baris pertama
dataku = dataku.iloc[1:]

# Eksport ke csv
dataku.to_csv('web_scrap_multi.csv', index=False)

# Membuka file yang sudah disimpan
buka = pd.read_csv('web_scrap_multi.csv')
