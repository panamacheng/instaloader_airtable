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

 