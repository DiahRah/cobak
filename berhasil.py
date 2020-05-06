import requests
from bs4 import BeautifulSoup #librarypython
import pymysql

db = pymysql.connect("localhost","root","","indana")
cursor = db.cursor()

my_url = 'https://www.goodreads.com/search?utf8=%E2%9C%93&q=youtubers&search_type=books'

r = requests.get(my_url)

request = r.content

soup = BeautifulSoup(request, "html.parser")

containers = soup.findAll("tr", {"itemscope":""})

for container in containers:
	title = container.find("a", {"class":"bookTitle"}).find('span').text

	author = container.find('a', {"class": "authorName"}).find('span').text

	print(author)

	cursor.execute('''insert into buku(Judul_Buku, Pengarang) VALUES(%s,%s)''',(title, author))
	cursor.execute('insert into nama_buku(nama_buku) VALUES(%s)',(title))
	cursor.execute('insert into pengarang(Pengarang) VALUES(%s)',(author))


print ("data saved")

db.commit()
db.close()
