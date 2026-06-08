# Day 58 - News Headline Scraper

## What I Learned

- How BeautifulSoup reads HTML content
- How to find repeated tags from a page
- How scraping can be practiced with sample HTML

## Features

- Parses sample HTML headlines
- Prints a clean numbered list
- Falls back safely if `bs4` is unavailable

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to News Headline Scraper!
1. Headline One
2. Headline Two
3. Headline Three
```

## Mistakes I Fixed

- Used sample HTML so the script works without live websites
- Extracted only text from matching tags

## Future Improvement

- Fetch headlines from a real news page
