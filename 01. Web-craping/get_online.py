from bs4 import BeautifulSoup
import requests
import time

print('Masukkan kemampuan yang tidak sesuai dengan keahlian anda :')
bukan_kemampuan = input('>')
print(f'Hasil peyaringan : {bukan_kemampuan}')

def cari_pekerjaan():
	text_html = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=php&txtLocation=').text
	soup = BeautifulSoup(text_html, 'lxml')

	kerja = soup.find_all('li', class_ ='clearfix job-bx wht-shd-bx')
	for index, pekerjaan in enumerate(kerja):
		waktu_posting = pekerjaan.find('span', class_ = "sim-posted").span.text
		if 'few' in waktu_posting : 
			kemampuan = pekerjaan.find('span', class_ = 'srp-skills').text.replace(' ','')
			nama_perusahaan = pekerjaan.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
			info_detail = pekerjaan.header.h2.a['href']
			if bukan_kemampuan not in kemampuan:
				with open(f'pekerjaan-file/{index}.txt', 'w') as f:
					f.write(f'Nama Prusahaan : {nama_perusahaan.strip()} \n')
					f.write(f'Kemampuan yang dibutuhkan : {kemampuan.strip()} \n')
					f.write(f'Informasi Detail: {info_detail} \n')
				print(f'File telah tersimpan : {index}')


if __name__ == '__main__':
	while True:
		cari_pekerjaan()
		waktu_tunggu= 2
		print(f'Tunggu {waktu_tunggu} menit....')
		time.sleep(waktu_tunggu * 60)