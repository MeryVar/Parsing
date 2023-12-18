import requests
from bs4 import BeautifulSoup


def parse_html_from_url(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        print(soup)

    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch the URL. {e}")


url_to_parse = "https://www.list.am/en/category/16"
parse_html_from_url(url_to_parse)
