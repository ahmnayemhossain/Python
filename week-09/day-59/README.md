# Day 59 - Job Post Scraper Demo

## What I Learned

- How HTML tables can be parsed row by row
- How to skip headers before reading data rows
- How repeated table cells become structured output

## Features

- Parses sample job rows from a table
- Extracts company and role values
- Prints clean job summaries

## How to Run

```bash
python main.py
```

## Example Output

```text
Welcome to Job Post Scraper Demo!
Softnan: Python Developer
DataHub: Analyst
```

## Mistakes I Fixed

- Skipped the header row before reading data
- Extracted company and role from the correct columns

## Future Improvement

- Save job rows to CSV
