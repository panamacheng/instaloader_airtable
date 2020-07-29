import os
from airtable import Airtable
from config import * 

# Get all urls from '_URL' table.
def get_all_urls():
    airtable = Airtable(base_key, url_table_name, api_key=os.environ['AIRTABLE_KEY'])
    all_urls = airtable.get_all(fields=['_URL'])
    base_array = []
    for url in all_urls:
        base_array.append(url['fields']['_URL'])
    return base_array

# Get all hashtags from '_Hashtags' table
def get_all_hashtags():
    airtable = Airtable(base_key, hashtag_table_name, api_key=os.environ['AIRTABLE_KEY'])
    all_hashtags = airtable.get_all(fields=['_Hash_Tag'])
    base_array = []
    for hashtag in all_hashtags:
        if len(hashtag['fields']) > 0:
            base_array.append(hashtag['fields']['_Hash_Tag'])
    return base_array