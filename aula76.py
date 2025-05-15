import re
 
import requests
from bs4 import BeautifulSoup
 
url = 'https://www.techtudo.com.br/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='utf-8')
 
# if parsed_html.title is not None:
#     print(parsed_html.title.text)
 
top_jobs_heading = parsed_html.select_one('#techtudo > div.mrf-article-body > section > div.row.content-head.non-featured > div.title > h1')
 
if top_jobs_heading is not None:
    section = top_jobs_heading.parent
 
    if section is not None:
        for p in section.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())