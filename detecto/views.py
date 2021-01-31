from django.shortcuts import render
import pickle
import newspaper
from newspaper import Article
from sklearn import model_selection
from sklearn.linear_model import _logistic
import urllib


# Create your views here.
# our home page view
def home(request):
    if request.method == 'POST':
        url = request.POST.get('query')
        print(url)
        #url = "https://timesofindia.indiatimes.com/city/31-january-2021-live-latest-news-from-cities/liveblog/80608408.cms"
        #news = urllib.parse.unquote(url)
        article = Article(str(url))
        print(article.text)
        article.download()
        article.parse()
        article.nlp()
        print("Article's Title:")
        print(article.title)
        print("n")
        #print("Article's Text:")
        #print(article.text)
        print("n")
        print("Article's Summary:")
        print(article.summary)
        print("n")
        print("Article's Keywords:")
        print(article.keywords)
        detecting_fake_news(article.summary)
        result = "hello"#detecting_fake_news(url)
        return render(request, 'detecto/result.html', {'result': result})
        # {'dict':qry_entered,'search_results_key':scrape_function(qry_entered)})
    else:
        return render(request, 'detecto/index.html')

    # function to run for prediction


def detecting_fake_news(var):
    #retrieving the best model for prediction call
    # load_model = pickle.load(open('/home/rutuja/HACK - IT/Newser/final_model.sav', 'rb'))
    # prediction = load_model.predict([var])
    # prob = load_model.predict_proba([var])
    # find("newyorker", "trump")
    # return render(request, 'detecto/index.html')
    return (print("The given statement is "), print("The truth probability score is "))

# # our result page view
# def result(request):
#     news = request.GET['news']
#     result = detecting_fake_news(news)

