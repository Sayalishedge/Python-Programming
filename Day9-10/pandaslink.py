

import pandas as pd
df=pd.read_table('http://bit.ly/chiporders'); #by default separator is tab
df=pd.read_table('http://bit.ly/movieusers',sep="|",header=None);