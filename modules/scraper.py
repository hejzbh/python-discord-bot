import requests
from bs4 import BeautifulSoup

class NewsScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        # 1) Fetch news list and get first post URL
        list_response = requests.get(self.url)
        if list_response.status_code != 200:
            return None

        list_html = BeautifulSoup(list_response.content, "html.parser")
        a_tag = list_html.select_one(".category-article-list .row .col-md-12 .search-item .search-txt a")
        post_url = a_tag["href"]
        if post_url is None:
            return

        # 2) Fetch the post content
        post_response = requests.get(post_url)
        if post_response.status_code != 200:
            return None

        post_html = BeautifulSoup(post_response.content, "html.parser")
        post_content_element = post_html.select_one(".story-content")
        post_content_text = post_content_element.getText(strip=True)

        return post_content_text[0:1000]
