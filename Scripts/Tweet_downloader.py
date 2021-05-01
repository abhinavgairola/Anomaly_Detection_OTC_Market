import datetime
print(datetime.datetime.today())
print(datetime.datetime(2021, 4, 12, 7, 39, 55, 173504).weekday())
print(datetime.datetime.today().weekday())
import twint

import os


with open('../Txt/Tickers.txt','r') as f:
  lines= (f.readlines())
All_cashtags=['$'+x.replace('\n','') for x in lines]
print(All_cashtags)
ttt
c = twint.Config()
#c.Username = 
for tags in All_cashtags[0:100]:
    c.Search = tags 
    c.Since = '2016-01-01 8:00:00'
    c.Store_json=True
    c.Lang = 'en'
    c.Hide_output = True
    c.Output = 'Tweets_json/Tweets'+tags+'.json'
    twint.run.Search(c)
