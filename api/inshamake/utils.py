import aiohttp
import asyncio
from bs4 import BeautifulSoup
import requests
import json
from transformers import pipeline
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from functools import partial
from concurrent.futures import ThreadPoolExecutor

root = "https://www.newtimes.co.rw/rwanda"


def pull_from_web_2(url):
    try:
        response = requests.get(url)
        sup = BeautifulSoup(response.text, 'html.parser')
        content_script = sup.find('script', type='application/ld+json')
        if content_script:
            json_cont = json.loads(content_script.string)
            article_body = json_cont.get('articleBody', None)
            article_title = json_cont.get('headline', None)
            if article_body:
                inshamake = summarize(article_body)
                return {
                    "Title": article_title,
                    "body": inshamake[0].get('summary_text')
                }
    except Exception as e:
        return f"Unable to retrieve with {str(e)}"


def allArticle_2():
    urll = requests.get(root)
    sup = BeautifulSoup(urll.text, 'html.parser')
    content_links = sup.find_all('div', class_="article-title")
    if content_links:
        for lin in content_links[6:11]:
            linkx = lin.find('a', href=True)
            if linkx:
                art = pull_from_web_2(linkx['href'])
                if "error" not in str(art):
                    yield art

def _format_articles(articles):
    formatted_body = ""
    for article in articles:
        title = article.get("Title", "")
        body = article.get("body", "")
        formatted_body += f"Title: {title}\n\n"
        formatted_body += f"Body: {body}\n\n"
        formatted_body += "-----------------------\n\n"
    return formatted_body.strip()

def send_email(reveiver):
    host= "smtp-mail.outlook.com" #use smtp-mail.outlook.com | smtp.gmail.com
    port = 587
    pswrd = "..." #your password
    sender = "oscobo@live.com"
    
    try:
        article = allArticle_2()
        body = _format_articles(article)
        msg = MIMEMultipart()
        msg["From"] = sender  #use email corresponding to smtp host
        msg["Subject"] = "Latest news"
        msg.attach(MIMEText(body, "plain"))
        smtp = smtplib.SMTP(host, port)
        statCode, response = smtp.ehlo() # check the availability of the server
        print("Server is on. \n",statCode,response)
        smtp.starttls()
        statusLogin, responseLogin = smtp.login(sender,pswrd)
        print(f"Logging in: {statusLogin} {responseLogin}")
        
        smtp.sendmail(sender,reveiver,msg.as_string().encode('utf-8'))
        smtp.quit()
        return {
            "status": "success",
            "message": f"Email sent successfully. to {reveiver}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def summarize(article):
    summarize_body = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarize_body(
        article,
        max_length=130,
        min_length=30,
        do_sample=False
    )