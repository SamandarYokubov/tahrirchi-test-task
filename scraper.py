import requests
from bs4 import BeautifulSoup
from datetime import datetime 



# scraper is valid solely for articles on uznews.uz
def get_article_data(url):
    article_data = {
        "URL": url,
        "Accessed Date": str(datetime.now().date()),
        "Accessed Time": str(datetime.now().time()).split('.')[0],
        "Description": "",
        "Content": ""
    }

    article_html = requests.get(url)
    article = BeautifulSoup(article_html.content, "html.parser")

    article_data["Description"] = article.find("p", itemprop="description").text
    article_post = article.find("div", class_="post")
    article_posts = article_post.find_all("div", class_="ce-paragraph cdx-block")
    for article_post in article_posts:
        article_data["Content"] += " " + article_post.text.replace(u'\xa0', u' ')
    return article_data
