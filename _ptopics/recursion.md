---
topic: "recursion"
desc: "functions that call themselves"
---


A recursive function is one that calls itself.

# The two parts of a recursive function

A correctly written recursive function has:

* at least one base case 
* at least one recursive call that moves towards the base case

# What does it mean to move towards the base case

Examples:

| parameter to function | base case | progress towards the base case |
|-----------------------|-----------|--------------------------------|
| a list called `alist` | `if alist==[]` (empty list) | recursive call on a shorter list (e.g. (`alist[1:]` or `alist[:-1]`) |
| a string `s` | `if s==""` (empty string) | recursive call on a shorter string (e.g. (`s[1:]` or `s[:-1]`) |
| a positive integer `n` | `if n==0` | recursive call on `n-1` |

