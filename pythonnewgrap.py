"""#pip install newsapi-python
from newsapi import NewsApiClient

# Initialize NewsApiClient with your API key
api_key = '9d859a86c1274a5792a10f76fd0e1176' # Get your API key from https://newsapi.org/
newsapi = NewsApiClient(api_key=api_key)

# Define parameters for fetching news
country = 'in'  # You can change this to any country code according to your preference
category = 'business'  # You can change this to any category like 'business', 'sports', 'technology', etc.

# Fetch top headlines
top_headlines = newsapi.get_top_headlines(country=country, category=category)

# Display top headlines
if top_headlines['status'] == 'ok':
    print("Top Headlines:")
    for article in top_headlines['articles']:
        print(f"Title: {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print("--------------")
else:
    print("Failed to fetch news. Check your API key or parameters.")
"""
"""from newsapi import NewsApiClient

# Initialize NewsApiClient with your API key
api_key = '9d859a86c1274a5792a10f76fd0e1176'  # Replace 'YOUR_NEWS_API_KEY' with your actual API key
newsapi = NewsApiClient(api_key=api_key)

# Define topics you want to fetch news for
topics = ['business', 'technology', 'science', 'health', 'sports']

# Fetch and display top headlines for each topic
for topic in topics:
    print(f"Top Headlines for {topic.capitalize()}:")
    top_headlines = newsapi.get_top_headlines(category=topic)
    if top_headlines['status'] == 'ok':
        for article in top_headlines['articles']:
            print(f"Title: {article['title']}")
            print(f"Source: {article['source']['name']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
            print("--------------")
    else:
        print(f"Failed to fetch news for {topic}.")
"""

#multiple with content
from newsapi import NewsApiClient
import textwrap

# Initialize NewsApiClient with your API key
api_key = '9d859a86c1274a5792a10f76fd0e1176'  # Replace 'YOUR_NEWS_API_KEY' with your actual API key
newsapi = NewsApiClient(api_key=api_key)

# Define topics you want to fetch news for
topics = ['business', 'technology', 'science', 'health', 'sports']

# Fetch and display top headlines for each topic
for topic in topics:
    print(f"Top Headlines for {topic.capitalize()}:")
    top_headlines = newsapi.get_top_headlines(category=topic)
    if top_headlines['status'] == 'ok':
        for article in top_headlines['articles']:
            print(f"Title: {article['title']}")
            print(f"Source: {article['source']['name']}")
            print(f"URL: {article['url']}")
            print("Content:")
            article_content = newsapi.get_everything(q=article['title'])  # Fetch full content of the article
            if article_content['status'] == 'ok' and len(article_content['articles']) > 0:
                content = article_content['articles'][0]['content']
                if content:
                    paragraphs = textwrap.wrap(content, width=100)  # Wrap content into paragraphs
                    for paragraph in paragraphs[:10]:  # Display first 10 paragraphs
                        print(paragraph)
            print("--------------")
    else:
        print(f"Failed to fetch news for {topic}.")
        