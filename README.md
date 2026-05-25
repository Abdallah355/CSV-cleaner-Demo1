# CSV-cleaner-Demo1
# CSV Contact Cleaner

A Python tool that takes a messy CSV file of contact information and produces a clean, 
structured output ready for review.

## What it does

- Strips extra spaces from names and capitalizes them properly
- Flags emails missing an @ symbol as invalid
- Standardizes phone numbers to digits only
- Outputs a clean CSV file ready for use

## Why I built this

Client data is rarely clean when it comes in. This tool automates the cleanup process 
instead of doing it manually row by row.

## How to run it

1. Add your contacts to `Contacts.csv`
2. Run the script: `python cleaner.py`
3. Check `Contacts_Cleaned.csv` for the cleaned output

## Tech used

- Python
- pandas