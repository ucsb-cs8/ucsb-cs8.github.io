---
topic: "boolean expressions"
desc: "and, or, not and De Morgan's law"
---

# Boolean: `True` or `False`

* Boolean expressions are those that evaluate to either `True` or `False`
* Examples include:
   * `3 < 4`, which evaluates to `True`
   * `1 + 2 == 7` which evaluates to `False`
   
# Boolean Variables

Boolean values can be assigned to variables.  For example:

```
x = 3 < 4
```

If we then examine `type(x)` we see that it is of type `bool`, as this Python shell session shows:

```
>>> x = 3 < 4
>>> x   
True
>>> type(x)
<class 'bool'>
>>> 
```


