from airTable import *
from instaLoader import *
from lib import *

all_urls = get_all_urls()
ig_urls = get_ig_urls(all_urls) 
len_ig_urls = len(ig_urls)

def export_profile_post(len_temp):
    ig_username = get_ig_pfn(ig_urls[len_temp])
    save_new_top_posts_by_profile(ig_username)
    save_new_middle_posts_by_profile(ig_username)
    save_new_bottom_posts_by_profile(ig_username)
    save_unique_comments_by_user(ig_username)
    
    len_temp += 1

    if len_temp < len_ig_urls: 
        export_profile_post(len_temp)

len_temp = 0
export_profile_post(len_temp)

all_hashtags = get_all_hashtags()
len_ig_hashtags = len(all_hashtags)
def export_hashtag_post(len_hashtag_temp):
    hashtag = all_hashtags[len_hashtag_temp]
    save_new_posts_by_hashtag(hashtag)

    len_hashtag_temp += 1
    if len_hashtag_temp < len_ig_hashtags:
        export_hashtag_post(len_hashtag_temp)

len_hashtag_temp = 0
export_hashtag_post(len_hashtag_temp)
