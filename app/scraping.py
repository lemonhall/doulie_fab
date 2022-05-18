# importing the modules
import requests
from bs4 import BeautifulSoup
from goose3 import Goose
from goose3.text import StopWordsChinese
import os


#工具类，用来辅助抓取网页的title和摘要的
# https://github.com/goose3/goose3
# pip3 install goose3
#https://www.geeksforgeeks.org/extract-title-from-a-webpage-using-python/
#pip3 install bs4
#pip3 install requests
#解决乱码问题
class Scraping():
	def get_title(url):
		# making requests instance
		reqs = requests.get(url)
		reqs.encoding = 'utf-8'
		soup = BeautifulSoup(reqs.text, 'html.parser')
		title = soup.find('title')
		return title.get_text()
	def goose_get_title(url):
		#print(type(url))
		g = Goose({'browser_user_agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0) ','stopwords_class': StopWordsChinese,'enable_image_fetching': True})
		article = g.extract(url=url)
		if article.top_image is None:
			pass
		else:
			src = article.top_image.src
			root = './app/static/uploads/'
			path = root + src.split('/')[-1]
			print(path)
			#这里本来还应该有个try的，但是为了调试方便，不放了，没有考虑图片重名的问题
			if not os.path.exists(root):
				print("root not exists")
				os.mkdir(root)
			if not os.path.exists(path):
				r=requests.get(src)
				with open(path,"wb") as f:
					f.write(r.content)
					f.close
					print("file save succ")
			else:
				print("file exists")
		return article
	#因为self调用的难点，我放弃了，直接放弃了这个方法
	def save_top_image(url):
		root = "./static/uploads/"
		path = root + url.split[-1]
		try:
			if not os.path.exist(root):
				os.mkdir(root)
			if not os.path.exist(path):
				r=requests.get(url)
				with open(path,"wb") as f:
					f.write(r.content)
					f.close
					print("file save succ")
			else:
				print("file exists")
		except:
			print("fail to save top_image")