from itertools import islice
from math import ceil
from instaloader import Instaloader, Profile

IL = Instaloader()
p_counts = 20    # counts of post

def download_posts_by_username_top(pfn): # pfn: profile name
    profile = Profile.from_username(IL.context, pfn)
    posts_sorted_by_time = sorted(profile.get_posts(), key=lambda p: p.date_utc, reverse=True)
    
    for post in islice(posts_sorted_by_time, ceil(p_counts)):
        IL.download_post(post, 'Top')

def download_posts_by_username_bottom(pfn): # pfn: profile name
    profile = Profile.from_username(IL.context, pfn)
    posts_sorted_by_time = sorted(profile.get_posts(), key=lambda p: p.date_utc, reverse=False)
    
    for post in islice(posts_sorted_by_time, ceil(p_counts)):
        IL.download_post(post, 'Bottom')

# get profile posts duration
def download_posts_by_username_middle(pfn): 
    profile = Profile.from_username(IL.context, pfn)
    posts_sorted_by_likes = sorted(profile.get_posts(),
                                key=lambda p: p.likes + p.comments,
                                reverse=True)

    for post in islice(posts_sorted_by_likes, ceil(p_counts)):
        IL.download_post(post, "Middle") 