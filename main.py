import pandas as pd
from scraper import get_article_data
from transformation import get_words
from stats import calc_occurrences

if __name__ == "__main__":
    articles = pd.DataFrame(columns=[
        "URL",
        "Accessed Date", 
        "Accessed Time", 
        "Description", 
        "Content",
        "Words"
    ])


    dataset_path = "./datasets/"
    article_url = input("Enter article's url: ")
    article_name = input("Enter article name: ")
    article = get_article_data(article_url)
    article["Words"] = get_words(article["Content"])
    article["Occurrences"] = calc_occurrences(article["Words"])
    articles = articles.append(article, ignore_index=True)

    articles.to_csv(dataset_path+article_name+".csv", index=False)
    