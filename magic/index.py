from bs4 import BeautifulSoup
import requests
import json
from transformers import pipeline

def pull_from_web(url):
    try:
        urll = requests.get(url)
        sup = BeautifulSoup(urll.text, 'html.parser')
        content_script = sup.find('script', type ='application/ld+json')
        if content_script:
            json_cont = json.loads(content_script.string)
            article_body = json_cont.get('articleBody', None)
            article_title = json_cont.get('headline', None)
            inshamake = summarize(article_body)
            return (f"Title: {article_title} \n{inshamake[0].get('summary_text')}")
    except:
        return f"enable to retrieve with {urll.status_code}"



def summarize(article):
    summarize_body = pipeline("summarization", model="facebook/bart-large-cnn")
    return (
        summarize_body(
            article,
            max_length=250, 
            min_length=30, 
            do_sample=False)
        )

url = 'https://www.newtimes.co.rw/article/17689/news/health/kagame-mulls-remuneration-of-community-health-workers'

if __name__ =="__main__":
    print(pull_from_web(url))