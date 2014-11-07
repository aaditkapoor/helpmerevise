from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from django.utils import timezone
import wikipedia
import googleapiclient
import json
import wget
import random
import urllib.request
from urllib.parse import urlparse
def return_image_url(q):
	url = "https://www.google.co.in/search?site=imghp&tbm=isch&source=hp&biw=1366&bih=643&q=laws+of+motion&oq=%s&gs_l=img.3..0l10.1703.8384.0.8578.19.14.3.1.1.1.232.1981.0j8j3.11.0....0...1ac.1.58.img..5.14.1779.KMzyD-aRlfQ" % q
	return url

def home(request):
	return render_to_response('index.html',{'date': timezone.now()})

class Search:
	url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0"
	def __init__(self,query):
		"""
			Performs google search
		"""
		self.query = query
		query = urllib.parse.urlencode({'q':self.query})
		self.response = urllib.request.urlopen(self.url + '&q=%s' % self.query)
		self.result = self.response.read().decode("utf8")
		self.data = json.loads(self.result)
		self.response_data = self.data['responseData']

	def __str__(self):
		print ("Query: %s" % self.query)

	def search_wikipedia(self):
		try:
			items = wikipedia.search(self.query)
			flag = True if self.query in items else random.choice(items)
			if flag:
				self.page = wikipedia.page(self.query)
				self.summary = wikipedia.summary(self.query)
		except:
			print("Something wrong...")

def search(request):
	query = request.GET.get('q',' ')

	search = Search(query)
	search.search_wikipedia()

	



