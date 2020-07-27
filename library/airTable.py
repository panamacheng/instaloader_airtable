import os
from airtable import Airtable
from config import * 

# Get all urls from '_URL' table.
def get_all_urls():
    airtable = Airtable(base_profile_key, table_profile_name, api_key=os.environ['AIRTABLE_KEY'])
    all_urls = airtable.get_all(fields=['_URL'])
    base_array = []
    for url in all_urls:
        base_array.append(url['fields']['_URL'])
    return base_array

