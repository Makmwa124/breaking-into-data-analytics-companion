"""Chapter 4: recalculate bramblewood_2025_solution.xlsx outside Excel and print the Summary sheet.
Needs: pip install formulas   (takes about a minute)"""
import formulas

book = "../data/bramblewood_2025_solution.xlsx"
sol = formulas.ExcelModel().loads(book).finish().calculate()


def value(sheet, cell):
    key = f"'[bramblewood_2025_solution.xlsx]{sheet.upper()}'!{cell}"
    return sol[key].value[0, 0]


print("Sales!H2 =", value("Sales", "H2"), "  Sales!I2 =", value("Sales", "I2"))
for r in range(1, 8):
    cells = [value("Summary", f"{c}{r}") for c in "ABCDEF"]
    print("  ".join(f"{v:>9,.0f}" if isinstance(v, float) else f"{str(v):>9}" for v in cells))
