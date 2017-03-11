---
topic: "antipatterns"
desc: "Things to avoid in your code"
---

Definition
==========

An anti-pattern is something that:

* people frequently write in their code (that's the <em>pattern</em> part)
* but that is BAD and should NOT BE DONE (that's the <em>anti</em> part).

(The term <em>anti-pattern</em> does have a more formal definition in Computer Science and some history; for purposes of CS8, we'll focus on the informal definition above.)

This page is here as a place to collect some common anti-patterns often seen in code written by folks new to Python programming (e.g. code submitted by CS8 students in programming assignments, or answers to exam questions.)

There are various kinds of anti-patterns:

* In some cases, the code "works" in
  the sense that it "computes the correct result", but it is hard to
  read for other programmers, or difficult to maintain, or might lead to
  later bugs or errors.

* Other times it is just wasteful, in that it takes up
  space in the code for no good reason.

* And sometimes, it is just code that might "seem right", but is
  just plain wrong.

Example
=======

One example that occurs frequently is the explicit use of `return`
`true;` and `return` `false;` after evaluating a boolean expression.

```python

def xIsNegative(x):
  if x<0:
    return True
  else:
    return False 
    
```

The entire if statement here is completely unnecessary. It is far more
clear to simply write:

```python
def xIsNegative(x):
  return x<0
```


The useless else branch
-----------------------

Consider this code for counting the number of times that the value k occurs:

```python
  if a[i] == k:
    count = count + 1
  else:
    count = count + 0
```

So, this might seem to make sense if you think that you always need an else with an if.   But, the else part here is useless!  Adding 0 to a variable does
nothing!  Just write this, with no else clause:

```python
  if a[i] == k:
    count = count + 1
```

Another variation of this antipattern is the `x=x;` assignment, like
this:

```python
  if a[i]  % 2 != 0:
    sumEvens = sumEvens + a[i]
  else:
    sumEvens = sumEvens
```

Leave off this useless else clause.    The variable sumEvens will retain
its value without you copying it back onto itself everytime through the
code.


Formal Definition of Anti-Pattern
=================================

A more formal definition, from
[Wikipedia](http://en.wikipedia.org/wiki/Anti-pattern):

> An anti-pattern (or antipattern) is a common response to a recurring
> problem that is usually ineffective and risks being highly
> counterproductive.\[1\]\[2\]
>
> The term, coined in 1995 by Andrew Koenig,\[3\] was inspired by a
> book, Design Patterns, in which the authors highlighted a number of
> design patterns in software development that they considered to be
> highly reliable and effective. The term was popularized three years
> later by the book AntiPatterns, which extended its use beyond the
> field of software design and into general social interaction and may
> be used informally to refer to any commonly reinvented but bad
> solution to a problem. Examples include analysis paralysis, cargo cult
> programming, death march, groupthink and vendor lock-in.
