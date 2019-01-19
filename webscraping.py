# webscraping_v-1-0.py
# created by jodiardi.akbar@gmail.com on 19 January 2019
# this is a webscraping script for educational purpose only
# it will scrap url and save it into a file
# credit to Py4E Course running by Dr Chuck and Team

import urllib
from BeautifulSoup import *

url = raw_input('Enter: ')
name = raw_input('File Name: ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# retrieve a list of achor tags
# each tag is like a dictionary of HTML attributes

tags = soup('a')

for tag in tags:
	print tag.get('href', None)


# open a file as variable name

with open(name, 'a') as f:
	for tag in tags:
		content = tag.get('href', None)
		f.write(content + '\n')