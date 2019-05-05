from env_variables import *
from newsapi import NewsApiClient
import requests
import json
import asyncio

#Init
newsapi = NewsApiClient(api_key=news_api_key)

all_articles = newsapi.get_everything(q='tesla',
                                      domains='bbc.co.uk',
                                      language='en',
                                      page=2)
url = (f'https://newsapi.org/v2/everything?q=bitcoin&from=2019-04-05&sortBy=publishedAt&apiKey={news_api_key}')
response = requests.get(url)
response_json = response.json()
