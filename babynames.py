
# excercise google python course : Regular Expression
# instructor : Professor Nick Parlante
# code by Jodiardi Akbar <jodiardi.akbar@gmail.com>
# jakarta, 27-06-2019


import re

# open file
f = open("Popular Baby Names 1990.html", "r")
# regex to find 1990
year = re.search(r"(Popularity) (in) (\d\d\d\d)", f.read())
# print the year
print year.group(3)

# open the same file
f = open("Popular Baby Names 1990.html", "r")
# regex to find names and numbers (the name counter), resulting a list
names_and_numbers = re.findall(r"<td>[A-Z]\w+</td><td>\d+</td>\s+<td>[A-Z]\w+</td>\s+<td>\d+</td>", f.read())
#print names_and_numbers

# open new file as a container
f1 = open("Temp1990.txt", "w")
# loop the list and write to the file
for name_and_number in names_and_numbers:
    f1.write(name_and_number)

# open the container file    
f2 = open("Temp1990.txt", "r")
# regex to find names and resulting a list
names = re.findall(r"[A-Z]\w+", f2.read())
#print names

# open again the container file
f3 = open("Temp1990.txt", "r")
# regex to find numbers and resulting a list
numbers = re.findall(r"\d+", f3.read())
#print numbers

# create dict from both lists to form a key:values relation
dict_names_numbers = dict(zip(names, numbers))
#print dict_names_numbers

# loop through the dict and print it, sorted by key
for key in sorted(dict_names_numbers):
    print "%s %s" % (key, dict_names_numbers[key])


