from itertools import islice
from math import ceil
from instaloader import Instaloader, Profile, Hashtag
from lib import read_file, write_file

IL = Instaloader()
p_counts = 20    # counts of post

# save post data to csv
def save_post_data_to_csv_by_profile(dir_name, file_name, posts):
    file_data = read_file(dir_name, file_name)
    if file_data[0] :
        print('Successfully opened the _Profile_Posts_Export.csv file')
    else :
        print('Created _Profile_Posts_Export.csv file')

    for post in islice(posts, ceil(p_counts)):
        new_row = { 
            '_username': post.owner_username, 
            '_media_id': post.mediaid, 
            '_short_url': post.shortcode, 
            '_date': post.date_local, 
            '_date(GMT)': post.date_utc, 
            '_caption': post.caption, 
            '_comments_count': post.comments, 
            '_likes_count': post.likes, 
            '_video_views': post.video_view_count, 
            '_video_url': post.video_url, 
            '_thumbnail_url': post.url, 
            '_image_url': post.url, 
            # '_location_id': post.location == None and None or post.location['id'], 
            # '_location_name':post.location == None and None or post.location['name'], 
            # '_location_url': post.location == None and None or post.location['slug'], 
            # '_lat': post.location == None and None or post.location['lat'],
            # '_lng': post.location == None and None or post.location['lng']
            '_location_id': post.location, 
            '_location_name':post.location, 
            '_location_url': post.location, 
            '_lat': post.location,
            '_lng': post.location
        }

        write_file(dir_name, file_name, new_row)
        # print(post.owner_username, post.mediaid, post.shortcode, post.date_local, post.date_utc, post.caption, \
        #     post.comments, post.likes, post.video_view_count, post.video_url, post.url, post.location)

def save_new_top_posts_by_profile(pfn): # pfn: profile name
    profile = Profile.from_username(IL.context, pfn)
    posts_sorted_by_time = sorted(profile.get_posts(), key=lambda p: p.date_utc, reverse=True)
    save_post_data_to_csv_by_profile('csvs', '_Profile_Posts_Export.csv', posts_sorted_by_time)

def save_new_bottom_posts_by_profile(pfn): # pfn: profile name
    profile = Profile.from_username(IL.context, pfn)
    posts_sorted_by_time = sorted(profile.get_posts(), key=lambda p: p.date_utc, reverse=False)
    save_post_data_to_csv_by_profile('csvs', '_Profile_Posts_Export.csv', posts_sorted_by_time)
    

# get profile posts duration
def save_new_middle_posts_by_profile(pfn): # pfn: profile name
    profile = Profile.from_username(IL.context, pfn)
    posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda p: p.likes + p.comments, reverse=True)
    save_post_data_to_csv_by_profile('csvs', '_Profile_Posts_Export.csv', posts_sorted_by_likes)


def save_new_posts_by_hashtag(hashtag): 
    hashtag = hashtag.replace("#", "")
    posts = Hashtag.from_name(IL.context, hashtag).get_posts()
    file_data = read_file('csvs', 'Hash_Tag_Export.csv')
    if file_data[0] :
        print('Successfully opened the Hash_Tag_Export.csv file')
    else :
        print('Created Hash_Tag_Export.csv file')

    for post in posts:
        new_row = { 
            '_Hash_Tag': hashtag, 
            '_media_id': post.mediaid, 
            '_short_url': post.shortcode, 
            '_date': post.date_local, 
            '_date(GMT)': post.date_utc, 
            '_caption': post.caption, 
            '_comments_count': post.comments, 
            '_likes_count': post.likes, 
            '_video_views': post.video_view_count, 
            '_video_url': post.video_url, 
            '_thumbnail_url': post.url, 
            '_image_url': post.url, 
            '_location_id': post.location == None and post.location or None, 
            '_location_name':post.location == None and post.location or None, 
            '_location_url': post.location == None and post.location or None, 
            '_lat': post.location == None and post.location or None, 
            '_lng': post.location == None and post.location or None, 
            # '_location_id': post.location == None and post.location.id or None, 
            # '_location_name':post.location == None and post.location.name or None, 
            # '_location_url': post.location == None and post.location.slug or None, 
            # '_lat': post.location == None and post.location.lat or None, 
            # '_lng': post.location == None and post.location.lng or None, 
            '_user_id': post.owner_profile.userid,
            '_username': post.owner_username, 
            '_full_name': post.owner_profile.full_name,
            '_profile_pic_url': post.owner_profile.profile_pic_url,
            '_profile_url': 'https://instagram.com/' + post.owner_profile.username,
            '_Num_of_Followers': post.owner_profile.followers,
            '_Num_of_Posts': post.owner_profile.mediacount,
            '_Num_Following': post.owner_profile.followees,
            '_Profile_Text': post.owner_profile.biography
        }

        write_file('csvs', 'Hash_Tag_Export.csv', new_row)
