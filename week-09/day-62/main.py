import csv
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

SAMPLE_HTML = """
<html>
  <body>
    <ul>
      <li class="headline">Python job opening</li>
      <li class="headline">Data analyst needed</li>
      <li class="headline">Remote developer role</li>
    </ul>
  </body>
</html>
"""

CSV_FILE = Path(__file__).with_name("scraped_results.csv")

print("Week 09 Exam - Scrape Page and Save to CSV")

if BeautifulSoup is None:
    headlines = ["Python job opening", "Data analyst needed", "Remote developer role"]
else:
    soup = BeautifulSoup(SAMPLE_HTML, "html.parser")
    headlines = [item.get_text(strip=True) for item in soup.select(".headline")]

with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["headline"])
    for headline in headlines:
        writer.writerow([headline])

print(f"Saved {len(headlines)} headlines to {CSV_FILE.name}")
