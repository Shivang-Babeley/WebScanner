import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from scanner.utils import is_valid_url

def fetch_url(url):
    try:
        response = requests.get(url, timeout=5)
        return response
    except requests.RequestException:
        return None

def extract_links(base_url, html):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for tag in soup.find_all('a', href=True):
        full_url = urljoin(base_url, tag['href'])
        if is_valid_url(full_url):
            links.add(full_url)
    return list(links)
