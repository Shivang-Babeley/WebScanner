# scanner/crawler.py

import requests
from scanner.core import extract_links
from urllib.parse import urlparse

def crawl_site(base_url, max_depth,page_limit):
    visited = set()
    to_visit = [(base_url, 0)]

    while to_visit and len(visited) < page_limit:
        current_url, depth = to_visit.pop(0)

        if current_url in visited or depth > max_depth:
            continue

        print(f"[+] Crawling: {current_url}")
        visited.add(current_url)

        try:
            res = requests.get(current_url, timeout=5)
            if res.status_code != 200:
                continue

            links = extract_links(current_url, res.text)

            for link in links:
                if link not in visited:
                    to_visit.append((link, depth + 1))

        except requests.RequestException:
            continue

    return visited
