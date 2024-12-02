# This file will query the custom search api to get our search results.

from setting import *
import requests
from requests.exceptions import RequestException
import pandas as pd
from storage import Database_storage
from urllib.parse import quote_plus



# def search_api(query, pages = int(RESULT_COUNT/10)):
#     result = []
#     url = "https://www.googleapis.com/customsearch/v1"
#     for i in range(0, pages):
#         # start = i * 10 + 1
#         params = {
#             'q' : query, # quote_plus is ensure that we are properly formatting our query to be in url. for examle we know there is no space in url so we can say quote_plus is remove the spaces and formate them into the url.
#             'key' : "AIzaSyAnJyEUVFoI09m_QITT_jY9QxukyQLAJkk",
#             'cx' : "e1adf3e1a35ac4f07"
#         }
            

#         response = requests.get(url, params=params) # here the response data is in the json formate
#         data = response.json() # here data is the dictionary
#         result += data["items"] # store the key of the items into result list
 
#     result_df = pd.DataFrame.from_dict(result) # here we change the list of dict into dataframes.
#     result_df["rank"] = list(range(1,result_df.shape[0]+1))

#     result_df = result_df[["link", "rank", "snippet", "title"]]
#     return result_df

def search_api(url, query):
    params = {
        'q' : query, # quote_plus is ensure that we are properly formatting our query to be in url. for examle we know there is no space in url so we can say quote_plus is remove the spaces and formate them into the url.

        'key' : "AIzaSyAnJyEUVFoI09m_QITT_jY9QxukyQLAJkk",
        'cx' : "e1adf3e1a35ac4f07",
    }
            
        
    response = requests.get(url, params=params)
    result = response.json()['items']

    for item in result:
        print(item['link'])


# def scrape_page(links):
#     html = []
#     for link in links:
#         try:
#             data = requests.get(link, timeout=5)
#             html.append(data.text)

#         except RequestException:
#             html.append("")
    
#     return html

# def search(query):
#     columns = ["query","rank","link","title","snippet","html","created"]
#     storage = DBStorage()

#     stored_result = storage.query_result(query)
#     if stored_result.shape[0] > 0:
#         stored_result["created"] = pd.to_datetime(stored_result["created"])
#         return stored_result[columns]

search_query = "fortuner"
url = "https://www.googleapis.com/customsearch/v1"
search_api(url,search_query)





