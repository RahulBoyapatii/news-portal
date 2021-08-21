from django.shortcuts import render
import requests

def Index(request):
    return render(request, 'index.html')

def Channels(request):
        return render(request, 'channels.html')

def Country(request):
    import json

    country = request.GET.get('country')
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey=aeca53f9db2f4b06a14a72305f2c203b'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
    'articles' : articles
    }
    return render(request, 'country.html', context)

def Category(request):
    import json

    category = request.GET.get('category')
    url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey=aeca53f9db2f4b06a14a72305f2c203b'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
    'articles' : articles
    }
    return render(request, 'category.html', context)

def Keyword(request):
    import json

    keyWord = request.GET.get('keyWord')
    url = f'https://newsapi.org/v2/everything?q={keyWord}&apiKey=aeca53f9db2f4b06a14a72305f2c203b'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
    'articles' : articles
    }
    return render(request, 'keyword.html', context)

def Search(request):
    import json

    country = request.GET.get('country')
    category = request.GET.get('category')
    keyWord = request.GET.get('keyWord')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey=aeca53f9db2f4b06a14a72305f2c203b'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey=aeca53f9db2f4b06a14a72305f2c203b'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/everything?q={keyWord}&apiKey=aeca53f9db2f4b06a14a72305f2c203b'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
    'articles' : articles
    }

    return render(request, 'search.html', context)

def Abc(request):
    import json

    news_api_request = requests.get("https://newsapi.org/v2/top-headlines?sources=abc-news-au&apiKey=aeca53f9db2f4b06a14a72305f2c203b")

    api = json.loads(news_api_request.content)

    return render(request, 'abc.html', { 'api': api})

def Bbc(request):
    import json

    news_api_request = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=aeca53f9db2f4b06a14a72305f2c203b")

    api = json.loads(news_api_request.content)

    return render(request, 'bbc.html', { 'api': api})

def Alj(request):
    import json

    news_api_request = requests.get("https://newsapi.org/v2/top-headlines?sources=al-jazeera-english&apiKey=aeca53f9db2f4b06a14a72305f2c203b")

    api = json.loads(news_api_request.content)

    return render(request, 'Alj.html', { 'api': api})

def Fox(request):
    import json

    news_api_request = requests.get("https://newsapi.org/v2/top-headlines?sources=fox-news&apiKey=aeca53f9db2f4b06a14a72305f2c203b")

    api = json.loads(news_api_request.content)

    return render(request, 'fox.html', { 'api': api})

def Hindu(request):
    import json

    news_api_request = requests.get("https://newsapi.org/v2/top-headlines?sources=the-hindu&apiKey=aeca53f9db2f4b06a14a72305f2c203b")

    api = json.loads(news_api_request.content)

    return render(request, 'Hindu.html', { 'api': api})

def Tech(request):
    import json

    news_api_request = requests.get("https://newsapi.org/v2/top-headlines?sources=techradar&apiKey=aeca53f9db2f4b06a14a72305f2c203b")

    api = json.loads(news_api_request.content)

    return render(request, 'techradar.html', { 'api': api})

def Google(request):
    import json

    news_api_request = requests.get("https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=aeca53f9db2f4b06a14a72305f2c203b")

    api = json.loads(news_api_request.content)

    return render(request, 'Google.html', { 'api': api})
