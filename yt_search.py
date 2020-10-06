from youtube_search import YoutubeSearch

results = YoutubeSearch('circunvalacion', max_results=1).to_dict()
print(results)

def get_first_yt_url(search_terms):
    result = YoutubeSearch(search_terms, max_results=1).to_dict()
    
    url_prefix = 'https://www.youtube.com'
    url_suffix = result['url_suffix']
    
    url = url_prefix + url_suffix
    return url
