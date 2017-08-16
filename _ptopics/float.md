---
topic: "float"
desc: "the data type that represents real numbers"
---

Real numbers are numbers on the number line other than integers, such
as -2.5, square root of 2, pi, and so forth.

Python treats integers such as 2, 4, 100, and -42 differently from
real numbers.  This is even true when we write an integer with a
decimal point; that is 100 and 100.0 are treated differently in terms
of Python's "internal processing", even though they represent the same
number.

Python will be precise and exact in representing integers.  However,
when representing real numbers, even ones that correspond to integers
such as 100.0, there is always the potential for some error.  This is
a consequence of the fact that the number of bits used to represent a
number is finite, but the number of real numbers in any range is
infinite.

That is:
* If we use 32 bits, or 64 bits, or 128 bits to represent an integer, we know precisely how many integers we can represent, and we can be sure each one has a unique, exact representation.    
* Between any two real numbers, there is an uncountably infinite number of additional real numbers.  So, no matter how many bits we use, and no matter what range of numbers we choose to represent, we cannot represent them all exactly and precisely.  Therefore representations of real numbers are always an approximation, and there is always the potential for some error.  
 
This error is usually small and insignificant--but not always.  It can cause at least two kinds of problems:
* In calculations involving many steps, small errors can accmuulate into larger, more significant errors.  Knowing about this problem and designing ways to predict and control the error is part of a topic in Computer Science and Applied Math known as "numerical analysis".   
* When we test for equality, i.e. is cToF(100.0) == 212.0, there is the possibility that the calculation on the left gives us 212.0000000001  instead of 212.0000000000.  That tiny difference could cause the test case to fail, even though the calculation is as close as we can get.
