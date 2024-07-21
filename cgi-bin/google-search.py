#!/usr/bin/env python3

import cgi
import cgitb
import requests
from bs4 import BeautifulSoup
import json
import sys

cgitb.enable()

print("Content-Type: application/json\n")

def google_search(query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    params = {'q': query, 'num': 10}
    try:
        response = requests.get('https://www.google.com/search', headers=headers, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        # Log the error to the server log
        print(f"Error fetching search results: {e}", file=sys.stderr)
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    for item in soup.find_all('div', attrs={'class': 'g'}, limit=10):
        title_element = item.find('h3')
        link_element = item.find('a')
        snippet_element = item.find('div', attrs={'class': 'IsZvec'})

        if title_element and link_element:
            title = title_element.text
            link = link_element['href']
            snippet = snippet_element.text if snippet_element else 'No snippet'
            results.append({
                'title': title,
                'link': link,
                'snippet': snippet
            })

        if len(results) >= 5:
            break

    return results

def main():
    form = cgi.FieldStorage()
    query = form.getvalue('query')

    if not query:
        print(json.dumps({'error': 'No query provided'}))
        return

    results = google_search(query)

    if results is None:
        print(json.dumps({'error': 'Failed to fetch search results'}))
    else:
        print(json.dumps(results))

if __name__ == "__main__":
    main()
