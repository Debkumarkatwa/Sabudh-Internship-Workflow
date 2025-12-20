#!/usr/bin/env python3
"""
IndianExpress News Scraper


Scrapes latest articles from https://indianexpress.com/ 

"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import logging
from urllib.parse import urljoin

# === USER CONFIG ===
NAME = "Deb kumar modal"   # Your full name (used in CSV header)
BASE_URL = "https://indianexpress.com/"
OUTPUT_CSV = f"news_data_{NAME.replace(' ', '_')}.csv"
MAX_ARTICLES = 30
# ===================

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; NewsScraper/1.0; +https://example.com/bot)"
}

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def fetch(url, timeout=10, max_retries=3):
    """Fetch a URL with retries."""
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=timeout)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            logging.warning(f"Attempt {attempt} failed for {url}: {e}")
            time.sleep(1 + attempt)
    logging.error(f"Failed to fetch {url} after {max_retries} attempts.")
    return None


def parse_homepage_for_links(html):
    """
    Find article links and titles on the homepage.
    Uses multiple selectors to handle layout variations.
    """
    soup = BeautifulSoup(html, "html.parser")
    links = []
    candidate_selectors = [
        "a[href*='/article/']",
        "a[href*='/news/']",
        "h2 a",
        "h3 a",
        "section.top-news a",
        "div.top-story a",
        "div.title a",
    ]
    for sel in candidate_selectors:
        for a in soup.select(sel):
            href = a.get("href")
            if not href:
                continue
            if href.startswith("http"):
                url = href
            else:
                url = urljoin(BASE_URL, href)
            title = a.get_text(strip=True)
            if title:
                links.append((title, url))

    # Deduplicate preserving order
    seen = set()
    filtered = []
    for title, href in links:
        if href not in seen:
            seen.add(href)
            filtered.append((title, href))
    return filtered


def extract_article_text(html):
    """Extract readable text from an article page."""
    soup = BeautifulSoup(html, "html.parser")
    # Remove unwanted elements
    for tag in soup(["script", "style", "aside", "figure"]):
        tag.decompose()

    candidate_body_selectors = [
        "div.full-details",
        "div.article-content",
        "div.article-body",
        "div[itemprop='articleBody']",
        "div#content",
        "article",
    ]
    paragraphs = []
    for sel in candidate_body_selectors:
        container = soup.select_one(sel)
        if container:
            for p in container.find_all("p"):
                text = p.get_text(" ", strip=True)
                if text:
                    paragraphs.append(text)
            if paragraphs:
                break

    # Fallback: all <p> tags
    if not paragraphs:
        for p in soup.find_all("p"):
            text = p.get_text(" ", strip=True)
            if text:
                paragraphs.append(text)

    full_text = "\n\n".join(paragraphs).strip()
    return full_text


# def build_dataframe(items):
#     """Convert scraped items into a structured DataFrame."""
#     df = pd.DataFrame(
#         items,
#         columns=[
#             "NEWS_TITLE_" + NAME,
#             "NEWS_LINK",
#             "FULL_SCRAPED_TEXT",
#         ],
#     )
#     return df


def build_dataframe(items):
    """Convert scraped items into a structured DataFrame with clickable hyperlinks."""
    data = []
    for title, link, text in items:
        hyperlink = f'=HYPERLINK("{link}", "Open Link")'
        data.append((title, hyperlink, text))

    df = pd.DataFrame(
        data,
        columns=[
            "NEWS_TITLE_" + NAME,
            "NEWS_LINK",
            "FULL_SCRAPED_TEXT",
        ],
    )
    return df



def main():
    logging.info("Fetching Indian Express homepage...")
    homepage_html = fetch(BASE_URL)
    if not homepage_html:
        logging.error("Could not fetch homepage. Exiting.")
        return

    candidates = parse_homepage_for_links(homepage_html)
    logging.info(f"Found {len(candidates)} candidate links on homepage.")

    items = []
    for idx, (title, link) in enumerate(candidates):
        if len(items) >= MAX_ARTICLES:
            break
        logging.info(f"[{idx+1}] Scraping: {title} - {link}")
        article_html = fetch(link)
        if not article_html:
            continue
        text = extract_article_text(article_html)
        if not text:
            logging.warning(f"No text found for: {link}")
            continue
        items.append((title, link, text))
        time.sleep(random.uniform(1.0, 2.5))  # polite delay

    if not items:
        logging.error("No articles scraped.")
        return

    df_final = build_dataframe(items)
    df_final.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
    logging.info(f"✅ Saved {len(df_final)} articles to {OUTPUT_CSV}")


if _name_ == "_main_":
    main()