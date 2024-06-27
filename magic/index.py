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
            return {"Title": article_title,
                    "body": inshamake[0].get('summary_text')
                    }
    except Exception as e:
        return f"enable to retrieve with {str(e)}"

def allArticle():
    articles = []
    urll = requests.get(root)
    sup = BeautifulSoup(urll.text, 'html.parser')
    content_links = sup.find_all('div', class_ = "article-title")
    if content_links:
        for lin in content_links[6:11]:
            linkx = lin.find('a', href=True)
            if linkx:
                art = pull_from_web(linkx['href'])
                if "error" not in art:
                    articles.append(art)
                print(pull_from_web(linkx['href']))
                print('\n')
    return articles 

def summarize(article):
    summarize_body = pipeline("summarization", model="facebook/bart-large-cnn")
    return (
        summarize_body(
            article,
            max_length=130, 
            min_length=30, 
            do_sample=False)
        )

if __name__ =="__main__":
    # print(pull_from_web(url))
    print(allArticle())