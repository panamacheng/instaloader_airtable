from airTable import *
from instaLoader import *
from lib import *

# all_urls = get_all_urls()
# ig_urls = get_ig_urls(all_urls) 

# len_ig_urls = len(ig_urls)

# def download_media(len_temp):
#     ig_username = get_ig_pfn(ig_urls[len_temp])

#     download_posts_by_username_top(ig_username)
#     download_posts_by_username_bottom(ig_username)
#     download_posts_by_username_middle(ig_username)
#     len_temp += 1

#     if len_temp < len_ig_urls: 
#         download_media(len_temp)

# len_temp = 0
# download_media(len_temp)

all_hashtags = get_all_hashtags()
print(all_hashtags)
