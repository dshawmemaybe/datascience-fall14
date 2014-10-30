import nltk
import re

name = re.compile('([A-Z]+) ([A-Za-z]+)\/NNP')
results = open('part2.out', 'w')

for i in range (1,7):
    with open("file{}.html".format(i), "r") as myfile:
        data = myfile.read()   
        sentences = nltk.sent_tokenize(data)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        sentences = [nltk.pos_tag(sent) for sent in sentences]
        chunks = [nltk.ne_chunk(sent) for sent in sentences]
        for chunk in chunks:
            matches = name.findall(str(chunk))
            if matches:
                for match in matches:
                    results.write(match[0] + ", " + match[1] + "\n")
