from bs4 import BeautifulSoup
import requests
import json
from transformers import pipeline


root = "https://www.newtimes.co.rw/rwanda"

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

def allArticle():
    links =[]
    urll = requests.get(root)
    sup = BeautifulSoup(urll.text, 'html.parser')
    content_links = sup.find_all('div', class_ = "nt-latest-articles paddingDefault")
    if content_links:
        content_linkx = sup.find_all('div', class_ = "article-title")
        for lin in content_linkx:
            linkx = lin.find('a', href=True)
            if linkx:
                links.append(linkx['href'])
    for rink in links:
        print (pull_from_web(rink))
        print("\n---")

def summarize(article):
    summarize_body = pipeline("summarization", model="facebook/bart-large-cnn")
    return (
        summarize_body(
            article,
            max_length=350, 
            min_length=200, 
            do_sample=False)
        )

url = 'https://www.newtimes.co.rw/article/17689/news/health/kagame-mulls-remuneration-of-community-health-workers'

if __name__ =="__main__":
    # print(pull_from_web(url))
    print(allArticle())