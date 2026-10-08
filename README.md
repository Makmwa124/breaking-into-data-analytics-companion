# Breaking Into Data Analytics After 30: companion files

Free practice files for the book **Breaking Into Data Analytics After 30: A Career-Change Roadmap with the Skills That Matter, Three Portfolio Projects and a 90-Day Plan to Your First Analyst Job** by Mathew Kariuki.

This repository holds everything you need to follow the book: the practice data for the three portfolio projects, every SQL query, Python script, Excel formula and DAX measure in the book (numbered by chapter), and the templates for the skills audit, the 90-day plan, STAR interview stories and your project write-ups. Every output printed in the book was produced by these files.

## Download

Click the green **Code** button above, then **Download ZIP**. Unzip it somewhere easy to find, such as your Documents folder. You do not need a GitHub account or Git.

## What's here

| Folder / file | What it is | Chapters |
|---|---|---|
| `data/bramblewood_sales.csv`, `bramblewood_products.csv`, `bramblewood_stores.csv` | Bramblewood Supplies click-and-collect orders, 2024 to 2025 (raw, with 12 planted duplicates) | 4 to 7, 10, 15 |
| `data/bramblewood.db` | The same data, cleaned, as a SQLite database (open it in DB Browser for SQLite) | 5, 10, 15 |
| `data/bramblewood_2025.xlsx` | 2025 orders for the Excel chapter, ready for you to add formulas | 4 |
| `data/bramblewood_2025_solution.xlsx` | The same workbook with every formula filled in | 4 |
| `data/quokka_members.csv` | Quokka Fitness gym memberships, for the churn project | 8, 11 |
| `data/riverbend_appointments.csv` | Riverbend Community Health appointments, 2025, for the operations dashboard | 12, 15 |
| `code/` | Every code example, named by chapter (`ch05_sql_basics.sql`, `ch11_project2_churn.py`, ...) | All |
| `code/run_sql.py` | Runs any `.sql` file against a SQLite database and prints the results | 5, 10, 15 |
| `templates/transferable_skills_audit.xlsx` | The skills audit | 3 |
| `templates/90_day_tracker.xlsx` | The 13-week plan with hours and deliverables | 17 |
| `templates/star_stories_worksheet.md` | Six STAR interview stories | 15 |
| `templates/cv_bullet_rewriter.md` | Turn duties into analyst-style achievements | 14 |
| `templates/project_writeup_template.md` | README skeleton for your portfolio projects | 10 to 13 |

## Quick start

1. **SQL:** install DB Browser for SQLite (sqlitebrowser.org), open `data/bramblewood.db`, go to **Execute SQL** and paste a query from `code/ch05_sql_basics.sql`. Or, with Python installed: `cd code` then `python run_sql.py ch05_sql_basics.sql ../data/bramblewood.db`.
2. **Python:** install Anaconda (or run `pip install -r requirements.txt`), then from the `code` folder run, for example, `python ch06_python_basics.py`. Scripts that draw charts save them as PNG files in the folder you run them from.
3. **Excel:** open `data/bramblewood_2025.xlsx` and follow Chapter 4.
4. **Power BI:** load the three Bramblewood CSV files into Power BI Desktop and follow Chapter 7. `code/ch07_check_dax_in_pandas.py` prints the values your cards should show.

Tested with Python 3.13 and pandas 3.0 (pandas 2.x works too; one printed data type differs, as Chapter 6 explains).

## Get the book

Paperback and Kindle editions are on Amazon. The PDF bundle with a printable cheat sheet is on Gumroad at [mathewkariuki.gumroad.com](https://mathewkariuki.gumroad.com).

## About

Bramblewood Supplies, Quokka Fitness, Riverbend Community Health and every person named in the examples are fictional, and the data was generated for teaching. These files are free to use for learning, including in your own portfolio projects (please change the question so the work is yours). The book is © 2026 Mathew Kariuki. All rights reserved.

Spotted a problem with an example or the data? Please open an issue.
