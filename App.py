from flask import Flask, render_template, json
from newsapi import NewsApiClient
from config import api_key


app = Flask(__name__)


@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key)
    topheadlines = newsapi.get_top_headlines(country="us")
    articles = topheadlines['articles']


    news = []
    url = []
    source = []
    img = []
    desc = []

    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        img.append(myarticles['urlToImage'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])
        source.append(myarticles['source'])

    mylist = zip(news, desc, img, url, source)
    return render_template(
        'index.html', 
        title="home",
        context = mylist
    )

@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key)
    topheadlines = newsapi.get_top_headlines(
    sources="abc-news, al-jazeera-english, associated-press, axios, bbc-news, bloomberg, business-insider, buzzfeed, cbs-news, cnn, independent, msnbc, mtv-news, national-geographic, nbc-news, newsweek, new-york-magazine, politico, the-hill, the-huffington-post, the-wall-street-journal,the-washington-post, time, usa-today, vice-news")
    
    articles = topheadlines['articles']
    
    news = []
    img = []
    desc = []
    url = []
    source = []
    
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        img.append(myarticles['urlToImage'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])
        source.append(myarticles['source'])
    
    mylist = zip(news, desc, img, url, source)
    return render_template(
        'bbc.html',
        title="BBC",
        context=mylist
        )




@app.route('/nazinews')
def nazinews():
    newsapi = NewsApiClient(api_key)
    nazinewz = newsapi.get_top_headlines(sources="breitbart-news, fox-news, national-review,  the-american-conservative, the-hill, the-jerusalem-post,  the-washington-times")

    articles = nazinewz['articles']

    news = []
    img = []
    desc = []
    url = []
    source = []

    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        img.append(myarticles['urlToImage'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])
        source.append(myarticles['source'])
    
    mylist = zip(news, desc, img, url, source)
    return render_template(
        'nazinews.html',
        title="FAR RIGHT XTREEEMISTS WHO LOVE MTN DEW",
        context=mylist
    )


if __name__ == "__main__":
    app.run(debug=True)