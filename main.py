import json
from scanner.core import fetch_url, extract_links
from scanner.analyzer import analyze_headers
from scanner.vuln_scanner import check_common_paths
from scanner.crawler import crawl_site

def run_recursive_scan(target_url, max_depth,page_limit):
    print(f"[+] Starting recursive scan on: {target_url}")
    
    crawled_urls = crawl_site(target_url, max_depth,page_limit)
    all_results = []

    for url in crawled_urls:
        print(f"[+] Analyzing: {url}")
        response = fetch_url(url)

        if not response:
            print(f"[-] Failed to fetch {url}")
            continue

        headers_info = analyze_headers(response.headers)
        #links = extract_links(url, response.text)
        vuln_results = check_common_paths(url)

        result = {
            "url": url,
            "status_code": response.status_code,
            "headers": headers_info,
            #"links_found": list(links),
            "Vulnerabilities": vuln_results
        }

        all_results.append(result)

    with open("reports/output.json", "w") as f:
        json.dump(all_results, f, indent=2)

    print(f"[✓] Recursive scan complete. {len(all_results)} pages analyzed.")
    print("[✓] Results saved to reports/output.json")

# Entry point
if __name__ == "__main__":
    run_recursive_scan("https://www.dvwa.co.uk/", max_depth=2,page_limit=20)





