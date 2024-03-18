from newsapi import NewsApiClient
import textwrap

def fetch_news(api_key, topics):
    # Initialize NewsApiClient with your API key
    newsapi = NewsApiClient(api_key=api_key)

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
                        paragraphs = textwrap.wrap(content, width=200)  # Wrap content into paragraphs
                        for paragraph in paragraphs[:100]:  # Display first 10 paragraphs
                            print(paragraph)
                print("Next--------------")
        else:
            print(f"Failed to fetch news for {topic}.")

# Example usage
api_key = '9d859a86c1274a5792a10f76fd0e1176'  # Replace 'YOUR_NEWS_API_KEY' with your actual API key
topics = ['business', 'technology', 'science', 'health', 'sports']
fetch_news(api_key, topics)