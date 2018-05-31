---
topic: "Practice Problems"
desc: "Practice Problems"
---

# Functions over lists

Reminders:
* Some of these might be uses of the accumulator pattern.  
* Others might be able to be solved with recursion
* Some can be solved with both techniques

Problems:

* Write a function `isListOfNumeric(numList1)` that returns `True` if the list is a list consisting
   of only int and float values, or is an empty list, otherwise returns `False`
   ```
   assert isListOfNumeric([])==True
   assert isListOfNumeric(23)==False
   assert isListOfNumeric([42])==True
   assert isListOfNumeric([40, 20, -6])==True
   assert isListOfNumeric(["42"])==False
   assert isListOfNumeric([42,"foo",13])==False
   ```

* Write `isListOfString` that returns `True` if the list is a list consisting
   of only int and float values, or is an empty list, otherwise returns `False`
   
   ```
   assert isListOfString([])==True
   assert isListOfString(23)==False
   assert isListOfString([42])==False
   assert isListOfString(["42"])==True
   assert isListOfString(["foo", "42", "bar"])==True
   assert isListOfString(["foo",13])==False
   ```
   
* Write a function `runningSum(numlist)` that, for a list of numbers, returns the running sum of that list.
   ```
   assert runningSum([10,5,10,5,-5,10])==[10,15,25,30,25,35]
   assert runningSum([1,2,3,4,5])==[1,3,6,10,15]
   ```
   
   For bonus points, throw ValueError if the parameter is not a list, or if any element of the list is not
   numeric (int or float).  (You may use a call to `isListOfNumeric1`)
   
* Write a function lengthOfEach that takes a list of strings, and returns the length of the each string on the list.
   ```
   assert lengthOfEach(["UCSB","UCI","Chico State")==[4,3,11]
   assert lengthOfEach(["Santa Barbara","Ventura","Oxnard"])==[13,7,6]
   ```

* Write a function makeEvenLength that takes a list of strings, and returns that same list of strings, except that any
   string with odd length has an extra space added to the end to make it have even length
   
   ```
   assert makeEvenLength(["UCSB","UCI","Chico State")==["UCSB","UCI ","Chico State "]
   assert makeEvenLength(["Santa Barbara","Ventura","Oxnard"])==["Santa Barbara ","Ventura ","Oxnard"]
   ```
# Functions over lists of dictionaries

* Write a function that calculates the GPA of a list of courses, where each course is a dictionary with
   keys `units`, `grade`, `course`.   Course is the name of the course (e.g. `"CHEM 1A"`, units is an int
   representing number of units, and grade is a letter grade, e.g. `A`, `A-`, `B+`, etc.
   
   ```
   courses1=[{},{},{}]
   ```
   
