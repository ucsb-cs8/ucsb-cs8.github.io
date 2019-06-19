---
topic: "command line arguments"
desc: "passing command line arguments to a Python Script"
---

When running a Python script at the command line (instead of inside IDLE, for example), you can 
pass it command line arguments.  

As an example, this script takes a starting date and a number of weeks as arguments, and
then produces a calendar.  The strings `2019-06-17` and `4` are passed to the script 
as *command line arguments*.
```
python3 calmaker.py 2019-06-17 4
```

If you've set up your script with a  [shebang](/topics/shebang), you can just run it this way:

```
./calmaker.py 2019-06-17 4
```

Before reading the discussion below, you should already be familiar with:

* The "shebang" found at [shebang](/topics/shebang)
* The `if __name__=="__main__" block`, explained here: [main blocks](https://ucsb-cs8.github.io/ptopics/main_blocks/)

# Basic use of `argv`

If you put this at the top of your Python file:

```
import sys
```

then anywhere in your Python file, you can access the list variable argv to get a list of the command
line arguments to your script.  

In the example 

```
python3 calmaker.py 2019-06-17 4
```

The values of sys.argv woudl be:

```
sys.argv[0] == "calmaker.py"
sys.argv[1] == "2019-06-07"
sys.argv[2] == "4"
```

The number of arguments is available in `len(sys.argv)` which in this case would be `3`.  The name of the program is always
stored in `sys.argv[0]` and counts as one of the arguments.

# Advanced use of command line arguments with argparse

In real world python coding, it is more common to use a library function called `argparse` to work with command line arguments.

The Offical Python website has [documentation for argparse](https://docs.python.org/3.7/library/argparse.html) which can use accessed to learn more.

