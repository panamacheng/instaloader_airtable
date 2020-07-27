from flask import Flask
from config import *
from library.airTable import *
from library.instaLoader import *
from library.lib import *

app = Flask(__name__)

all_urls = get_all_urls()
ig_urls = get_ig_urls(all_urls) 

len_ig_urls = len(ig_urls)

print(len_ig_urls)
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

if __name__ == "__main__":
    app.run(host=app_host, port=app_port, debug=True)