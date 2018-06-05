---
topic: "CSV files"
desc: "reading and writing CSV (Comma Separated Value) files in Python"
---

CSV (Comma Separated Value) file are a very common way to get data from one program into another.   Most Spreadsheet programs,
(e.g. Excel, Google Sheets) 
can both import and export the values in a spreadsheet via CSV.  (CSV works with values only, not formulas).

CSV data typically looks something like this.  There is often a header row:

```
Course,Grade,Units
CMPSC 8,A,4.0
MATH 8,B+,5.0
CHEM 1A,B,3.0
CHEM 1AL,A-,2.0
```

To import this file into a Python dictionary, we can use this code:
