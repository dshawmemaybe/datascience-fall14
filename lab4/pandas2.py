import re

data = open('worldcup.txt','r')
results = open('pandas2.csv','w')
place = "1"

c = re.compile('.*{{fb\|([A-Z]+)}}.*')
y = re.compile('.*Cup\|([0-9]+).*')

country = ""

for line in data:
    split = line.split(',')
    for year in split:
        if y.match(year):
            results.write(country + ", " + y.match(year).group(1) + ", " + place + "\n")
    if place == "1":
        place = "2"
    elif place == "2":
        place = "3"
    elif place == "3":
        place = "4"
    else:
        place = "1"        
    if c.match(line):
        country = c.match(line).group(1)
        place = "1"

results.close()
