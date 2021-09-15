from bs4 import BeautifulSoup

# membaca file index dan menampilkannya 
with open('index.html', 'r') as html_file :
	 content = html_file.read()
	 ## menampilkan isi index.html tampa menggunakan libaray
	 #print(content)


	 ## menampilkan isi index.html dengan menggunakan library BeautigulSoup
	 soup = BeautifulSoup(content, 'lxml')
	 ##menampilkan isi seluruh index.html
	 #print(soup.prettify())

	 ## mencari element html tertentu dengan fungsi find, disini mencari tag h5 pada index.html
	 ## karena di dalam index.html terdapat h5 yang lebih dari satu maka gunakan find_all untuk mencari seluruh h5 yang ada
	 #tags = soup.find('h5')

	 """
	 html_tags = soup.find_all('h5')
	 for judul in html_tags :
	 	print(judul.text)
	 """

	 course_cards = soup.find_all('div', class_='card')
	 for course in course_cards:
	 	course_name = course.h5.text
	 	course_des 	= course.p.text
	 	course_price = course.a.text.split()[-1]

	 	#print(course_name)
	 	#print(course_price)

	 	print(f'{course_name} Harga : {course_price}')

