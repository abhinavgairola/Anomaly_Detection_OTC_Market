import twint
import os

if not os.path.exists('../Tweets_json'):
  os.mkdir('../Tweets_json')


with open('../Txt/Tickers.txt','r') as f:
  lines= (f.readlines())
All_cashtags=['$'+x.replace('\n','') for x in lines]

c = twint.Config()

for tags in All_cashtags:
    c.Search = tags 
    c.Since = '2016-01-01 8:00:00'
    c.Store_json=True
    c.Lang = 'en'
    c.Hide_output = True
    c.Output = '../Tweets_json/Tweets'+tags+'.json'
    twint.run.Search(c)
