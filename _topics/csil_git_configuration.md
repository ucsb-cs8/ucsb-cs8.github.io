---
topic: "CSIL: git configuration"
desc: "Configuring your CSIL account to use git"
---

This page has three sections:

* *How* to configure your CSIL account for git
* *Why* you need to configure your CSIL account for git
* *What about GUI* options for git?

How
---

This section describes how to configure your CSIL account for git.

To set up your CSIL account for using command line git, type the following commands, substituting your real name (e.g. Chris Gaucho) in place of "Your Name" and your email address (e.g. cgaucho@umail.ucsb.edu) in place of "you@example.com".

```
git config --global user.name "Your Name"
git config --global user.email you@example.com
git config --global push.default simple
```

You should only have to ever do these steps once for any given computer system. The values of these global configuration options are stored in a file called .gitconfig in your home directory. Take a look by cd'ing into your home directory, and using the more command to list the contents of .gitconfig:

```
$ cd
$ more .gitconfig
[push]
    default = simple
[user]
    name = Chris Gaucho
    email = cgaucho@umail.ucsb.edu
$
```

The `~/.gitconfig` file is a plain text file, and the options in it can also be set by just editing this file. Using the git config command is an alternative to hand editing this file, and is really just a way to be sure that the syntax ends up being right.


