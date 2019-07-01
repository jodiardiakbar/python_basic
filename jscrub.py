# .  grep any char seperti huruf, angka, space , namun berhenti pada new line
# \w  grep word char seperti huruf dan angka tapi tidak character seperti &
# \s  grep space, new tab, new line, dll
# \s+  grep lebih dari 1 kali space
# .+ grep semuanya
# \S grep angka, number, character
# [.] grep character titik
# re.findall(r'pattern', 'str', re.IGNORECASE) atau re.DOTALL


# webscrapping script using regex (no html soup)
# inspired by drchuck python web data course
# code by Jodiardi Akbar <jodiardi.akbar@gmail.com>
# Jakarta, 1 July 2019
# disclaimer : 
# this is for learning purposes, any illegal activity using this script are strictly prohibited
# related file is drchuck

import urllib
import re

# define url, grep it, and write it to a file
url = "http://www.dr-chuck.com"
html = urllib.urlopen(url).read()
#print html
f = open("drchuck", "w")
f.write(html)

# open the file to start regex it
f1 = open('drchuck', 'r')

# regex using this pattern to grep URLs http or https
# r'(http\S*)\"' 
# http - grep http 
# \S - follow by non-whitespace char 
# * - and repeat greping the non-whitespace char
# (http\S*) - only grep pattern inside bracket and leave out the one at outside, which is \"
# \" - grep " (double quote character)
websites = re.findall(r'(http\S*)\"', f1.read())
for website in websites:
    print website