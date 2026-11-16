# T6A – Control Flow Katas

Three short Python programs that practice **variables, `for` loops, nested loops, and `if / elif / else` conditionals**, using warehouse and distribution-center scenarios (scanner checks, audit calendars, shelf locations, and incident validation).

## Why This Was Built

This repo was built as part of the i.c.stars T6A control-flow exercise. The goal is to practice:

- Writing loops that repeat work a fixed number of times
- Making decisions with conditionals and guard clauses
- Working with lists, tuples, and dictionaries
- Committing small, incremental changes to Git as the solution develops

## Project Structure

```
t6a-control-flow/
├── kata1.py     # Scanner Health Checks – simple for loop
├── kata2.py     # Warehouse Audit Calendar – loop + if/elif/else rules
├── kata3.py     # Location Codes (Option A) + Incident Validation (Option B)
├── test.py      # Scratch file used for warm-up practice (not part of the katas)
├── setup.ps1    # Windows setup script provided with the assignment
└── README.md    # Project documentation
```

## Requirements

- **Python 3** (no external libraries needed – only built-in Python is used)
- **Git** (to clone the repository)
- Windows PowerShell, macOS Terminal, or any Linux shell

All data the programs need is defined directly inside the `.py` files, so there is nothing else to download.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/mariiakit-official/t6a-control-flow.git
   cd t6a-control-flow
   ```

2. Check that Python 3 is installed:

   ```bash
   python --version
   ```

   On Windows you may need `py --version` instead.

> **Windows shortcut:** the included `setup.ps1` checks for Git and Python, configures your Git name/email, clones the repo, and opens it in VS Code. Run it from PowerShell in the folder where you keep your code.

## How to Use

Run each kata from the project folder:

```bash
python kata1.py
python kata2.py
python kata3.py
```

(On Windows, use `py` instead of `python` if needed.)

## The Katas

### Kata 1 – Scanner Health Checks (`kata1.py`)

A branch checks its handheld scanners every 15 minutes. The program prints the first 10 check times.

- `check_interval` and `check_count` are stored in variables so the schedule is easy to change.
- A `for` loop over `range(1, check_count + 1)` multiplies the check number by the interval.

**Sample output:**

```
Check 1: 15 minutes after shift start
Check 2: 30 minutes after shift start
...
Check 10: 150 minutes after shift start
```

### Kata 2 – Warehouse Audit Calendar (`kata2.py`)

Prints the audit type for each day of a month using these rules:

| Rule | Result |
|------|--------|
| Day divisible by 3 **and** 5 | `FULL AUDIT` |
| Day divisible by 5 | `Scanner audit` |
| Day divisible by 3 | `Cycle count` |
| Any other day | `Normal operations` |

- A dictionary `months_days` maps each month to its number of days, so the loop length is set **dynamically** by changing the `month` variable (currently `'October'`, 31 days).
- The "both" case (`FULL AUDIT`) is checked **first**, so it is not caught by the single-rule branches.

**Sample output:**

```
Day 1 Normal operations
Day 3 Cycle count
Day 5 Scanner audit
Day 15 FULL AUDIT
Day 30 FULL AUDIT
```

### Kata 3 – Location Codes & Incident Validation (`kata3.py`)

Both options of Kata 3 were completed (the stretch goal).

**Option A – Location Codes (nested loop):** prints codes for 3 aisles × 4 shelves, one row per aisle. `print(..., end=" ")` keeps each aisle's codes on one line, and an empty `print()` starts the next row.

```
A1-S1 A1-S2 A1-S3 A1-S4
A2-S1 A2-S2 A2-S3 A2-S4
A3-S1 A3-S2 A3-S3 A3-S4
```

**Option B – Incident Validation (guard clauses):** loops through a list of incident tuples and skips any with a missing branch or a severity outside 1–3, printing the reason.

```
LOGGED INC-1001 at DC-North (severity2)
SKIPPED INC-1002 : missing branch
SKIPPED INC-1003 : severity 5 is not 1-3
LOGGED INC-1004 at DC-North (severity3)
```

## Technical Decisions

- **Variables instead of hard-coded numbers** (`check_interval`, `check_count`, `month`) make the programs easy to adjust without rewriting the logic.
- **Dictionary lookup for month length** (Kata 2) lets the calendar adapt to any month instead of being fixed at 30 days.
- **Most specific condition first** (Kata 2): `day % 3 == 0 and day % 5 == 0` is tested before the single checks so that days like 15 and 30 are labeled `FULL AUDIT`.
- **Kata 2 approaches:** a first version used `if / elif` statements without a loop (kept as comments in the file for reference); the final version uses a loop. The nested loop in the final version was kept as practice with nested iteration — a single loop would produce the same output.
- **`end=" "` in `print()`** (Kata 3A) prevents a new line after each code so a whole aisle prints on one row.
- **Guard clauses** (Kata 3B) check for invalid data first and skip it with a clear message, so only valid incidents reach the "logged" branch. The severity check also handles a record that has no severity value (`len(incident) > 2`).
- **Small, frequent commits** document how each solution was built step by step (see the Git history).

## Author

Mariia Kit – [GitHub: mariiakit-official](https://github.com/mariiakit-official)
