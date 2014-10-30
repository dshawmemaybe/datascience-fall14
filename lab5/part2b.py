import re
import nltk
IN = re.compile(r'.*\b(in|at|on|for|about|above|below|to|of)\b')
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('PER','ORG',doc, corpus='ieer', pattern = IN):
        print(nltk.sem.rtuple(rel))
