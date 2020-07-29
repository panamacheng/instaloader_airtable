from itertools import islice
from math import ceil
from instaloader import Instaloader, Profile, Hashtag
from lib import read_file, write_file
from config import *

IL = Instaloader()

# save unique comments by user.
def save_unique_comments_by_user(pfn): 
    file_data = read_file('csvs', 'Profile_Unique_Likes_n_Comments.csv')
    if file_data[0] :
        print('Successfully opened the Profile_Unique_Likes_n_Comments.csv file')
    else :
        print('Created Profile_Unique_Likes_n_Comments.csv file')

    profile = Profile.from_username(IL.context, pfn)
    posts_sorted_by_time = sorted(profile.get_posts(), key=lambda p: p.date_utc, reverse=True)

    for post in islice(posts_sorted_by_time, ceil(p_counts)):
        comments = post.get_comments()
        for comment in comments: 
            new_row = {
                '_Profile_Handle': pfn,
                '_user_id': comment.owner.userid,
                '_username': comment.owner.username,
                '_full_name': comment.owner.full_name,
                '_is_private': comment.owner.is_private,
                '_is_verified': comment.owner.is_verified,
                '_Date_of_Last_Like_or_Comment': '',
                '_Total_Comments_N_Likes': comment.likes_count, 
                '_Total_Comments': '',
                ' _Total_Likes': comment.likes_count,
                '_profile_pic_url': comment.owner.profile_pic_url,
                '_profile_url': comment.owner.external_url,
                '_Num_of_Followers': comment.owner.followers,
                '_Num_of_Posts': comment.owner.mediacount,
                '_Num_Following': comment.owner.followees,
                '_Profile_Text': comment.owner.biography
            }

            write_file('csvs', 'Profile_Unique_Likes_n_Comments.csv', new_row)

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

def save_new_posts_by_hashtag(hashtag): 
    hashtag = hashtag.replace("#", "")
    posts = Hashtag.from_name(IL.context, hashtag).get_posts()
    posts_sorted_by_time = sorted(posts, key=lambda p: p.date_utc, reverse=True)

    file_data = read_file('csvs', 'Hash_Tag_Export.csv')

    if file_data[0] :
        print('Successfully opened the Hash_Tag_Export.csv file')
    else :
        print('Created Hash_Tag_Export.csv file')

    for post in islice(posts_sorted_by_time, ceil(p_counts)):
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
            '_profile_url': post.owner_profile.external_url,
            '_Num_of_Followers': post.owner_profile.followers,
            '_Num_of_Posts': post.owner_profile.mediacount,
            '_Num_Following': post.owner_profile.followees,
            '_Profile_Text': post.owner_profile.biography
        }

        write_file('csvs', 'Hash_Tag_Export.csv', new_row)
