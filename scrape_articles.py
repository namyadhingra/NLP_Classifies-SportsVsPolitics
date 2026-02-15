import csv
import time
import requests
from bs4 import BeautifulSoup

# Input file must contain: category, url
INPUT_FILE = "url_indian_news.csv"

# Output file will contain: category, url, text
OUTPUT_FILE = "indian_news_with_text.csv"

# This header makes the request look like it came from a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def download_page(url):
    """
    Sends HTTP request to website and returns HTML content.
    """

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)

        # Check if request was successful
        if response.status_code == 200:
            return response.text
        else:
            print("Failed:", url, "Status:", response.status_code)
            return None

    except Exception as e:
        print("Error while fetching:", url)
        return None
def extract_article_text(html):
    """
    Parses HTML and extracts text inside <p> tags.
    """

    soup = BeautifulSoup(html, "html.parser")

    # Find all paragraph tags
    paragraphs = soup.find_all("p")

    # Extract clean text from each paragraph
    text = " ".join(p.get_text() for p in paragraphs)

    # Remove extra spaces
    text = text.replace("\n", " ").strip()

    # Filter very short pages
    if len(text) > 200:
        return text
    else:
        return None

def main():

    saved_count = 0

    with open(INPUT_FILE, "r", encoding="utf-8") as infile, \
         open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:

        reader = csv.DictReader(infile)

        writer = csv.DictWriter(outfile, fieldnames=["category", "url", "text"])
        writer.writeheader()

        for row in reader:

            url = row["url"]
            category = row["category"]

            print("Scraping:", url)

            # Step 1: Download page
            html = download_page(url)

            if html:
                # Step 2: Extract text
                article_text = extract_article_text(html)

                if article_text:
                    writer.writerow({
                        "category": category,
                        "url": url,
                        "text": article_text
                    })
                    saved_count += 1

            # Be polite to website (avoid rapid requests)
            time.sleep(1)

    print("Finished.")
    print("Total articles saved:", saved_count)


if __name__ == "__main__":
    main()
