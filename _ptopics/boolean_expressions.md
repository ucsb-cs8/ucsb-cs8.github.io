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

# Combining booleans with `and` and `or`

If we combine two boolean expressions with `and`, they both must be true for the entire expression to be true.  If either or both is `False`, then the whole expression is `False`

Examples:

* `3>8 and 5>8` evaluates to `False` because both `3>8` and `5>8` are False
* `3<5 and 5>8` evaluates to `False` because `5>8` is `False`
* `3>8 and 5<8` evaluates to `False` because `3>8` is `False`
* `3<5 and 5<8` evalutes to `True` because both sides of the `and` are `True`

If we combine two boolean expressions with `or`, they both must be true for the entire expression to be true:

Examples:

* `3>8 or 5>8` evaluates to `False` because both `3>8` and `5>8` are False
* `3<5 or 5>8` evaluates to `False` because `3>5` is `True`
* `3>8 or 5<8` evaluates to `False` because `5>8` is `True`
* `3<5 or 5<8` evalutes to `True` because both sides of the `or` are `True`

# The six relational operators

There are six relational operators, each of which returns a boolean value:

| Operator | Meaning | Example use <br> that evaluates <br> to `True`  | Example use <br >that  evaluates <br> to `False` |
|----------|---------|-------------------------------------------------|--------------------------------------------------|
|  <       | is less than | `4 < 2 + 3`  | `4 < 2 + 2` |
|  <=      | is less than or equal to | `4 <= 2 + 2` | `4 <= 1 + 2` |
|  >       | is greater than | `5 > 2 + 2`  | `5 > 2 + 3` |
|  >=      | is greater than or equal to | `4 >= 2 + 2` | `4 >= 2 + 3` |
|  ==      | is equal to | `4 == 2 + 2` | `4 ==  2 + 3` |
|  !=      | is not equal to | `4 != 2 + 6` | `4 != 2 + 2` |

# The `not` operator 

The `not` operator is placed in front of a boolean expression, and changes `True` to `False` and `False` to `True`

```
>>> x = 3 < 4
>>> x
True
>>> not x
False
>>> not 4 == 2 + 2
False
>>>     
```

