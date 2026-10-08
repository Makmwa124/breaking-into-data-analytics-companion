"""Run every statement in a .sql file against a SQLite database and print the results.

Usage (from the code folder):
    python run_sql.py ch05_sql_basics.sql ../data/bramblewood.db
"""
import sqlite3
import sys


def show(cursor):
    cols = [d[0] for d in cursor.description]
    rows = [["NULL" if v is None else str(v) for v in r] for r in cursor.fetchall()]
    widths = [max(len(c), *(len(r[i]) for r in rows)) if rows else len(c) for i, c in enumerate(cols)]
    print("  ".join(c.ljust(w) for c, w in zip(cols, widths)).rstrip())
    for r in rows:
        print("  ".join(v.ljust(w) for v, w in zip(r, widths)).rstrip())


sql_file, db = sys.argv[1], sys.argv[2]
text = open(sql_file, encoding="utf-8").read()
con = sqlite3.connect(db)
for stmt in [s.strip() for s in text.split(";") if s.strip()]:
    comments = [l for l in stmt.splitlines() if l.strip().startswith("--")]
    body = "\n".join(l for l in stmt.splitlines() if not l.strip().startswith("--")).strip()
    if not body:
        continue
    print("\n" + (comments[-1] if comments else "--"))
    show(con.execute(body))
