import re

http = re.compile('http.*')

a = open('products_out.csv','r')
b = open('product_mapping.csv','r')

correct_hash = {}
for line in b:
    amazon = line.split(',')[0].replace('"',"")
    google = line.split(',')[1].replace('"',"")
    correct_hash[amazon] = google

correct = 0
total = 0;
for line in a:
    amazon_id = ''
    google_id = ''
    if (line.split(',')[1] == 'amazon') and (line.split(',')[10] == 'google'):
        amazon_id = line.split(',')[2]
        google_id = line.split(',')[11]
    elif (line.split(',')[10] == 'amazon') and (line.split(',')[1] == 'google'):
        amazon_id = line.split(',')[11]
        google_id = line.split(',')[2]
        
    if amazon_id != '' and google_id != '' and (amazon_id != google_id):
        if http.match(amazon_id):
            if google_id in correct_hash:
                if correct_hash[google_id].strip() == amazon_id.strip():
                    correct += 1
            total += 1
        else:
            if amazon_id in correct_hash:
                if correct_hash[amazon_id].strip() == google_id.strip():
                    correct += 1
            total += 1

print "{}/{} correct".format(correct, total)

