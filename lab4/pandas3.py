import re
import numpy
import pandas as pd

data = pd.read_csv("pandas2.csv", names=['country', 'year', 'place'])

result = data.pivot('country','year','place')

print result
