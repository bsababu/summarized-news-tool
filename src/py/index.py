from bs4 import BeautifulSoup
import requests
import json

def pull_from_web(url):
    urll = requests.get(url)
    sup = BeautifulSoup(urll.text, 'html.parser')
    content_script = sup.find('script', type ='application/ld+json')
    if content_script:
        json_cont = json.loads(content_script.string)
        article_body = json_cont.get('articleBody', None)
        article_title = json_cont.get('headline', None)
        return (f"Title: {article_title} \n{article_body}")
    

url = 'https://www.newtimes.co.rw/article/17689/news/health/kagame-mulls-remuneration-of-community-health-workers'

if __name__ =="__main__":
    print(pull_from_web(url))