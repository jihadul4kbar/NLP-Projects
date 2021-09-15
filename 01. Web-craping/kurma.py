from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.tripadvisor.com/Attraction_Review-g297733-d1036419-Reviews-or10-Kuta_Beach_Lombok-Lombok_West_Nusa_Tenggara.html').text


print(html_text)