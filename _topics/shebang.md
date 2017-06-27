---
topic: "shebang"
desc: "About that first line of some python files that looks like this: #!/usr/bin/env python"
---

The first line of many Python files looks like this:

```
#!/usr/bin/env python
```

This is called a "shebang" (pronounced "shuh-bang").  The name comes from the fact that the exclamation point (`!`) is sometimes
read aloud as the word "bang", and the syntax here comes from the Unix Shell, hence "shell-bang", contracted into "shebang".

But what is it for?  What it does is allow you to run a Python Script directly in a Unix Shell environment 
(also in a MacOS terminal session, which is a Unix shell) by just typing its name.

That is, if `hello.py` looks like this:

```python
print ("Hello World")
```

then to run it, you need to do:

```
python hello.py
```

But if it has a shebang as its first line:

```
#!/usr/bin/env python

print ("Hello World")

```

and you change its permissions to executable (`chmod u+x hello.py`) then you can run it directly 
like this:

```
./hello.py
```

# More about the shebang 

* [Shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) on Wikipedia
