import sys
from requests import get
from bs4 import BeautifulSoup


languages_dict = {
    'english': ['eng', 'english', 'ingles', 'inglés', 'ing'],
    'spanish': ['spa', 'spanish', 'español', 'esp']
}


def set_lang(input_lang, langs_dict):
    for k in langs_dict.keys():
        if input_lang in langs_dict[k]:
            if k == 'english':
                return 'definition'
            if k == 'spanish':
                return 'definicion'
    return None

def define(language, word):
    if set_lang(language, languages_dict) is not None:
        url = f'https://www.wordreference.com/{set_lang(language, languages_dict)}/{word}'
        html_source = get(url).text

        soup = BeautifulSoup(html_source, 'lxml')

        ol = soup.find('ol')
        try:
            definition = ol.find('li').text
            return word.capitalize() + "; " + definition
        
        except AttributeError:
            definition = soup.find('p', id='noEntryFound').text
            return definition

    else:
        return 'Language not available'

