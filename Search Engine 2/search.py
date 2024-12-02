
# from setting import *
import requests
from requests.exceptions import RequestException
import pandas as pd
# from storage import Database_storage
from urllib.parse import quote_plus

# API_KEY = open("AIzaSyAnJyEUVFoI09m_QITT_jY9QxukyQLAJkk").read()
# SEARCH_ENGINE_ID = open("e1adf3e1a35ac4f07").read()

# search_query = "Top 5 pc games"

# url = "https://www.googleapis.com/customsearch/v1"

# params =  {
#     'q' : search_query,
#     'key' : "AIzaSyAnJyEUVFoI09m_QITT_jY9QxukyQLAJkk",
#     'cx' : "e1adf3e1a35ac4f07",

# }

# response = requests.get(url, params=params)
# result = response.json()['items']

# for item in result:
#     print(item['link'])

def search_api(url, query):

    params =  {
    'q' : query,
    'key' : "AIzaSyAnJyEUVFoI09m_QITT_jY9QxukyQLAJkk",
    'cx' : "e1adf3e1a35ac4f07",

    }

    response = requests.get(url, params=params)
    result = response.json()['items']

    for item in result:
        print(item['link'])


search_query = "Top 5 pc games"
url = "https://www.googleapis.com/customsearch/v1"

search_api(url, search_query)