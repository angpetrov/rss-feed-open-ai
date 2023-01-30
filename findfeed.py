import urllib.parse
import requests
import feedparser
from bs4 import BeautifulSoup

def find_feed(site):
    # Make a GET request to the given site
    response = requests.get(site)
    # Get the HTML content of the response
    html = response.text
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html, "html.parser")
    # List to store the possible feed URLs
    possible_feeds = []
    # Find all `link` tags with `rel` attribute equal to `alternate`
    feed_urls = soup.find_all("link", rel="alternate")

    # Iterate through the `link` tags and extract the URLs if they are of type `rss` or `xml`
    for link in feed_urls:
        link_type = link.get("type", None)
        if link_type:
            if "rss" in link_type or "xml" in link_type:
                href = link.get("href", None)
                if href:
                    possible_feeds.append(href)

    # Parse the URL of the site to extract the scheme (e.g., `http` or `https`) and hostname
    parsed_url = urllib.parse.urlparse(site)
    base = f"{parsed_url.scheme}://{parsed_url.hostname}"
    # Find all `a` tags in the HTML
    a_tags = soup.find_all("a")
    # Iterate through the `a` tags and extract the URLs if they contain `xml`, `rss`,    or `feed`
    for a in a_tags:
        href = a.get("href", None)
        if href:
            if "xml" in href or "rss" in href or "feed" in href:
                possible_feeds.append(base + href)

    # List to store the final feed URLs
    result = []
    # Iterate through the possible feed URLs and extract only the ones that have entries using `feedparser`
    for url in set(possible_feeds):
        feed = feedparser.parse(url)
        if len(feed.entries) > 0:
            if url not in result:
                result.append(url)

    # Return the final list of feed URLs
    return result
