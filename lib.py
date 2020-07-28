import os
import pandas as pd

# Get instagram urls from arrary.
def get_ig_urls(array):
    ig_urls = []
    for url in array:
        if 'instagram.com' in url:
            ig_urls.append(url)
    return ig_urls

# get username by ig url
def get_ig_pfn(string):
    return string.split('/')[3]

# validate the file by name
def validate_file(file_name):
    parent_dir = os.getcwd() + '/csvs/'
    file = parent_dir + file_name
    
    if os.path.isfile(file):
        return True
    else:
        return False  

# validate the directory by dir_name
def validate_directory(dir_name):
    parent_dir = os.getcwd()
    if os.path.isdir(parent_dir + '/' + dir_name):
        return True
    else:
        path = os.path.join(parent_dir, dir_name)
        os.mkdir(path) 
        return False

# Read csv file by name
def read_file(dir_name, file_name):
    validate_directory(dir_name)
    if validate_file(file_name): 
        df = pd.read_csv(dir_name + '/' + file_name) 
        json = df.to_json(orient='records')
        return [True, json]
    else :
        header_columns = []
        if file_name == '_Profile_Posts_Export.csv':
            header_columns = ['_username','_media_id','_short_url','_date','_date(GMT)','_caption', \
                '_comments_count','_likes_count','_video_views','_video_url','_thumbnail_url', \
                    '_image_url','_location_id','_location_name','_location_url','_lat','_lng']

        if file_name == 'Hash_Tag_Export.csv':
            header_columns = ['_Hash_Tag','_media_id','_short_url','_date','_date(GMT)','_caption', \
                            '_comments_count','_likes_count','_video_views','_video_url','_thumbnail_url', \
                            '_image_url','_location_id','_location_name','_location_url','_lat','_lng' \
                            '_user_id','_username','_full_name','_profile_pic_url','_profile_url', \
                            '_Num_of_Followers','_Num_of_Posts','_Num_Following','_Profile_Text']
                            
        if file_name == 'Profile_Unique_Likes_n_Comments.csv':
            header_columns = ['_Profile_Handle','_user_id','_username','_full_name','_is_private', \
                            '_is_verified','_Date_of_Last_Like_or_Comment','_Total_Comments_N_Likes', \
                            '_Total_Comments',' _Total_Likes','_profile_pic_url','_profile_url', \
                            '_Num_of_Followers','_Num_of_Posts','_Num_Following','_Profile_Text']

        df = pd.DataFrame(columns=header_columns)
        df.to_csv(dir_name + '/' + file_name, index = False, header=True)
        
        return [False, []]

# Write csv file by name
def write_file(dir_name, file_name, new_row):
    df = pd.read_csv(dir_name + '/' + file_name) 
    df_marks = df.append(new_row, ignore_index=True)
    df_marks.to_csv(dir_name + '/' + file_name, index = False, header=True)
