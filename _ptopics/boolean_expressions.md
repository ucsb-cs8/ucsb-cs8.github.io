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
* `3<5 or 5>8` evaluates to `True` because `3<5` is `True`
* `3>8 or 5<8` evaluates to `True` because `5<8` is `True`
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

# Applying `not` to boolean expressions with a single relational operator

Suppose we have a boolean expression with a single relational operator.  Placing a not in front of the expression is probably not the best way to change that expression to its opposite.   Here we show six relational expressions with not in front of them, each followed by a more concise expression that means the same thing:

| Original Expression | The opposite | A more concise equivalent |
|---------------------|-----------------|--------|
| `a < b`  | `not a < b` | `a >= b` |
| `a <= b` | `not a <= b` | `a > b` |
| `a > b`  | `not a > b` | `a <= b` |
| `a >= b` | `not a >= b` | `a < b` |
| `a == b`  | `not a == b` | `a != b` |
| `a != b` | `not a != b` | `a == b` |

There may be isolated cases where the version with `not` might be easier for people reading your code to understand.  However, in most cases, the more concise alternative <em>without</em> the `not` is preferred.

Note the opposite pairs:
* `<` and `>=` are opposites
* `>` and `<=` are opposites
* `==` and `!=` are opposites

# De Morgan's laws

When applying `not` to an entire expression involving `and` or `or`, it is necessary to remember De Morgan's laws.

These are two rules of logic that are credited to  Augustus De Morgan, a 19th-century British mathematian.

The concise statement of the laws are these:

| Original Expression | Equivalent Expression |
|----------------------|----------------------|
| `not (a and b)`     | `(not a) or (not b)` |
| `not (a or b)`     | `(not a) and (not b)` |

An even more concise way to say this: when "distributing" not inside the parentheses:
* `and` changes to `or`
* `or` changes to `and`

It may seem at first as if this transformation makes things more complicated.  For example:

| Original Expression | New Expresssion | 
|---------------------|-----------------|
| `not ( a == 0 or discriminant < 0 )` | `(not a==0) and (not discriminant < 0)` |  
| `not (x >= 0 and y >= 0)` | `(not x >= 0) or (not y >= 0)`  |

However, if we combine this with the rule that applying not to a relational expression simply changes the relational operator to it's opposite, then we can simplify further:

| Original Expression | New Expresssion | Even Simpler | 
|---------------------|-----------------|-----------------|
| `not ( a == 0 or discriminant < 0 )` | `(not a==0) and (not discriminant < 0)` | `a!=0 and discriminant >= 0` |  
| `not (x >= 0 and y >= 0)` | `(not x >= 0) or (not y >= 0)`  | `x < 0 and y > 0 `|

For the homework and exams, you should be prepared to convert an expression involving `not` into one that does not use `not` by applying these rules.
