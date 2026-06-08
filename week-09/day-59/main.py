try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

SAMPLE_HTML = """
<html>
  <body>
    <table>
      <tr><th>Company</th><th>Role</th></tr>
      <tr><td>Softnan</td><td>Python Developer</td></tr>
      <tr><td>DataHub</td><td>Analyst</td></tr>
    </table>
  </body>
</html>
"""

print("Welcome to Job Post Scraper Demo!")

if BeautifulSoup is None:
    jobs = [("Softnan", "Python Developer"), ("DataHub", "Analyst")]
else:
    soup = BeautifulSoup(SAMPLE_HTML, "html.parser")
    rows = soup.find_all("tr")[1:]
    jobs = []
    for row in rows:
        columns = row.find_all("td")
        jobs.append((columns[0].get_text(strip=True), columns[1].get_text(strip=True)))

for company, role in jobs:
    print(f"{company}: {role}")
