---
topic: "CSV files"
desc: "reading and writing CSV (Comma Separated Value) files in Python"
---


CSV (Comma Separated Value) file are a very common way to get data from one program into another.   Most Spreadsheet programs,
(e.g. Excel, Google Sheets) 
can both import and export the values in a spreadsheet via CSV.  (CSV works with values only, not formulas).

# Pre-requisite knowlege

Before reading this page, you should be familiar with:

* [Files](https://ucsb-cs8.github.io/ptopics/files/) in general
* [Dictionaries](https://ucsb-cs8.github.io/ptopics/dictionaries/), a data type for mapping keys to values.

# What CSV files look like

CSV data typically looks something like this.  There is often a header row:

```
Course,Grade,Units
CMPSC 8,A,4.0
MATH 8,B+,5.0
CHEM 1A,B,3.0
CHEM 1AL,A-,2.0
```

This might be stored, for example, in a file called `grades.csv`

# Importing a CSV file to list of dicts

To import this file into a list of Python dictionaries, we can use the code below.  

(Note that this approach works best with relatively small CSV files, ones where the entire file fits into the computer's memory.  Files of up to a few MB are probably fine.  If you notice that your computer locks up when you try this on large files, you'll need a different approach.)

```
import csv
import pprint
with open('grades.csv') as csvfile:
   rows = list(csv.DictReader(csvfile))

pprint.pprint(rows)
```

As a reminder, `pprint.pprint(value)` prints out a value in a nice way so we can read it easily.
Here's what the code above prints.  As you can see, what we get is a list of dictionaries, one for each row.
Also,  as a reminder, `python3 -i grades.py` is a Unix command to  run the file `grades.py` and then get the Python prompt (similar to doing the `"Run"` command in IDLE3).

```
(cli-extra)pconrad@localhost:~/cs8$ python3 -i grades.py 
[{'Course': 'CMPSC 8', 'Grade': 'A', 'Units': '4.0'},
 {'Course': 'MATH 8', 'Grade': 'B+', 'Units': '5.0'},
 {'Course': 'CHEM 1A', 'Grade': 'B', 'Units': '3.0'},
 {'Course': 'CHEM 1AL', 'Grade': 'A-', 'Units': '2.0'}]
>>> 
```

At the Python prompt, we can then print out values from the variable rows to work with different parts of the CSV file:

```
>>> rows[0]
{'Course': 'CMPSC 8', 'Grade': 'A', 'Units': '4.0'}
>>> rows[0]['Course']
'CMPSC 8'
>>> rows[3]
{'Course': 'CHEM 1AL', 'Grade': 'A-', 'Units': '2.0'}
>>> rows[3]['Grade']
'A-'
>>> 
```

# Exporting list of dicts to CSV

The following code from [this StackOverflow article](https://stackoverflow.com/questions/3086973/how-do-i-convert-this-list-of-dictionaries-to-a-csv-file) illustrates how to output a list of dict objects to a CSV file with a header.

```
import csv
toCSV = [{'name':'bob','age':25,'weight':200},
         {'name':'jim','age':31,'weight':180}]
keys = toCSV[0].keys()
with open('people.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)

```

The result should be the following output written to `people.csv`:

```
age,weight,name
25,200,bob
31,180,jim
```
