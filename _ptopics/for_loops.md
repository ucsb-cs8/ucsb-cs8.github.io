---
topic: "for loops"
desc: "for loops in Python, from basic to advanced"
---

# Basic for loop over a list

```python
schools = ["UCSB","UCLA","UCI","Cal Poly"]
for s in schools:
   print(s,len(s))
```

Output:
```
UCSB 4
UCLA 4
UCI 3
Cal Poly 8
```

# Basic for loop with counter

```python
>>> for i in range(4):
...    print(i)
... 
0
1
2
3
>>> 
```

# For loop over a list using `range(len(thelist))`

```python
schools = ["UCSB","UCLA","UCI","Cal Poly"]
for i in range(len(schools)):
   print(i,schools[i])
```

```
0 UCSB
1 UCLA
2 UCI
3 Cal Poly
```

# For loop over a list with index and values

```python
schools = ["UCSB","UCLA","UCI","Cal Poly"]
for i,s in enumerate(schools):
    print(i,s)
    
```

Output:

```
0 UCSB
1 UCLA
2 UCI
3 Cal Poly
```


# For more information:

* <http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/>
