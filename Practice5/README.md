# Practice 5: Python Regular Expressions (RegEx) & Receipt Parsing

This repository contains exercises for mastering Python regular expressions and a practical receipt parsing example.

## 1. Objective
- Learn Python RegEx (search, match, findall, split, sub)
- Practice metacharacters, special sequences, and quantifiers
- Parse receipt data from `raw.txt` using Python `re` module

## 2. Files

- **receipt_parser.py** – Python script that:
  - Extracts all prices from receipt
  - Finds product names
  - Calculates total amount
  - Extracts date and time
  - Detects payment method
  - Outputs structured JSON to console and `parsed_receipt.json`

- **raw.txt** – Example receipt file

- **README.md** – This file

## 3. Usage

```bash
# Run parser
python receipt_parser.py

# The structured JSON output will be saved to parsed_receipt.json