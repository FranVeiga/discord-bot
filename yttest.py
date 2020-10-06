from bs4 import BeautifulSoup
from requests import get
import subprocess
def get_yt_result(query):
    query = "+".join(query.split(" "))
    url = "https://www.youtube.com/results?search_query=" + query
    source = get(url).text
    print(source)
    subprocess.Popen(f"echo {source}", shell=True)
    soup = BeautifulSoup(source, 'lxml')
    div = soup.find('div', id='dismissable')
    video_id = div.find('a', id='video-title').href
    video_url = 'https://youtube.com' + video_id

    return video_url

get_yt_result("circunvalacion")
