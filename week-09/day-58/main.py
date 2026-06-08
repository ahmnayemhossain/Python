try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

SAMPLE_HTML = """
<html>
  <body>
    <h2>Headline One</h2>
    <h2>Headline Two</h2>
    <h2>Headline Three</h2>
  </body>
</html>
"""

print("Welcome to News Headline Scraper!")

if BeautifulSoup is None:
    headlines = ["Headline One", "Headline Two", "Headline Three"]
else:
    soup = BeautifulSoup(SAMPLE_HTML, "html.parser")
    headlines = [tag.get_text(strip=True) for tag in soup.find_all("h2")]

for index, headline in enumerate(headlines, start=1):
    print(f"{index}. {headline}")
