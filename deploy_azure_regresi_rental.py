# Mengimpor library
import json
import requests

# Masukkan endpoint dan key
endpoint = 'MASUKKAN_ENDPOINT'
key = 'MASUKKAN_KEY'

# Kumpulan array yang akan kita prediksi 5 hari ke depan
x = [[1,1,2022,1,0,6,0,2,0.344167,0.363625,0.805833,0.160446],
    [2,1,2022,1,0,0,0,2,0.363478,0.353739,0.696087,0.248539],
    [3,1,2022,1,0,1,1,1,0.196364,0.189405,0.437273,0.248309],
    [4,1,2022,1,0,2,1,1,0.2,0.212122,0.590435,0.160296],
    [5,1,2022,1,0,3,1,1,0.226957,0.22927,0.436957,0.1869]]

# Merubah array menjadi format JSON
input_json = json.dumps({"data": x})

# Menyiapkan tipe konten dan autentifikasi untuk request
headers = {"Content-Type":"application/json",
        "Authorization":"Bearer " + key}

# Mengirim request
response = requests.post(endpoint, input_json, headers=headers)

# Jika kita mendapatkan respon valid, munculkan prediksinya
if response.status_code == 200:
    y = json.loads(response.json())
    print("Prediksi:")
    for i in range(len(x)):
        print (" Hari: {}. Prediksi rental: {}".format(i+1, max(0, round(y["result"][i]))))
else:
    print(response)