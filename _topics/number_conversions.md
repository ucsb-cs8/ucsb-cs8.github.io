---
topic: "Number Conversions"
desc: "Binary, Decimal, Octal and Hexadecimal"
---

# Videos

CS8 F13 Student Ahaha S. located the following list of videos to help with learning number conversions
 
* A good overview <http://www.youtube.com/watch?v=GPnLy6YO-0M>
* Just understanding Binary <http://www.youtube.com/watch?v=0qjEkh3P9RE>
* Binary to Octal <http://www.youtube.com/watch?v=9jho2TkH6AU>
* Binary to Hexadecimal <http://www.youtube.com/watch?v=jFnXpMt6H_Y>
* Binary to Decimal <http://www.youtube.com/watch?v=tfKe8PPI2zs>
* A deep look at binary, that explains WHY about binary also. <https://www.youtube.com/watch?v=vT9p2QnIycI>
   * You can skip to 6:36 if you just want the HOW:  <https://www.youtube.com/watch?v=vT9p2QnIycI#t=6m36s>
* Hexadecimal conversion:
   * <https://www.youtube.com/watch?v=6plMoviKDs0#t=8m50s>

# Practice Problems

Practice Here: <http://www.cs.ucsb.edu/~pconrad/cs8/13F/numberConversions/>

# Unix File Permissions in Octal

When we type `ls -l` at the Unix/Linux command prompt we get strings that correspond to the octal numbers used in chmod commands. 

For example:

```
$ ls -l
total 5
-rwxr-xr-x 1 pconrad 0376 3633 Feb  7 09:01 000.SampleLectureTopics.htm
drwx------ 2 pconrad 0376  512 Feb  7 10:00 02.07
$ 
```

The second line starts with 

```
drwx------
```

The `d` means that `02.07` is a directory. The `rwx` means that the owner of file, `pconrad`, has read, write, execute 
permission.

Here are some additional examples, and how they related to octal numbers in a chmod command:

| This output in `ls -l` | Could be set with this `chmod` command |
|------------------------|----------------------------------------|
| `-rw-r--r--`           | `chmod 644 filename` |
| `drwxr-xr-x`           | `chmod 755 dirname`  |
| `-rw-------`           | `chmod 600 filename` | 

As a reminder, the first `d` vs. `-` isn't part of the octal number, but is rather an indication of whether the listing is for a file or a directory.

The meanings are:

| octal <br> digit | binary <br> equivalent | rwx <br> format | meaning |
|---|-----|-------|---------------|
| 0 | 000 | `---` | no permission |
| 1 | 001 | `--x` | execute |
| 2 | 010 | `-w-` | write |
| 4 | 100 | `r--` | read |


The three digits in an octal number have different meanings depending on their positions (text borrowed from <a href="http://en.wikipedia.org/wiki/File_system_permissions#Octal_notation">Wikipedia</a>). </p>
<ul>
      <li> UGO = User, Group, Other</li>
      <li>777 = &quot;-rwxrwxrwx&quot; = rwx for all</li>
      <li>754 = &quot;-rwxr-xr--&quot; = rwx for owner of the file, r-x for group, r-- for other</li>
      <li>124 = &quot;---x-w-r--&quot; = x for owner of the file, w for group, r for other</li>
</ul>

For a DIRECTORY, execute has a particular peculiar meaning...
  It means that if you already KNOW the name of a file in that directory,
  you are allowed to access it... but you may not LIST the files in that
  directory.

If we want a directory to be available on the web, we have to open up
read and execute permission to "others".  We do that with the last three
letters in the permission string


# Quiz yourself on octal chmod values 

This web page gives you an opportunity to practice with converting between the format used in ls -l output, and the octal numbers used in chmod.

<https://www.cs.ucsb.edu/~pconrad/cs8/topics/chmodQuiz1/>

# More on octal file permissions:

* <https://www.centos.org/docs/2/rhl-gsg-en-7.2/s1-navigating-chmodnum.html>
