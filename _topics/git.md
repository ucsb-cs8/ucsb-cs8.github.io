---
topic: "git/github"
desc: "An introduction. git vs. github.com vs. github.ucsb.edu, repos, etc."
---

A few basics facts about git, github.com, and github.ucsb.edu
----------------------------------------------------------------------------

In addition to learning Python, you may be offered the opportunity to learn a bit about "version control" in this course.

"Version control" refers to systems for:
* organizing and keeping track of different versions of the code for a system as it changes over time
* sharing that code with others that need access, while keeping it private from those that should not
* organizing changes when multiple people are making changes to the same piece of software.

One of the most popular systems for version control is a tool called a tool called "git".  

There are two websites that you might also use along with git:
* a website called "github.com"
* a website called "github.ucsb.edu". 

In this article, we'll try to clear up some of the confusion that may arise about:
* "git" vs. "github",
* when you would use "github.com" vs. "github.ucsb.edu",
* why you would even want to learn this in an introductory course 
* and if so, which parts of git and github you might learn in CMPSC 8 (vs. the parts that you won't need to learn until later, and even then, only if you are going on to do more with programming after this course is over.(

### What is git and what is a repo?

The software package "git" is an example of a "version control system". (Others include SVN, Mercurial, and in a previous generations, CVS, RCS, and SCCS).

A git repo (short for repository) is nothing more than a collection of files and directories (folders), along with a special subdirectory called .git (stored only once in the top level directory of the repo) that keeps track of the complete history of the files and directories contained in the repo. To some extent, the ".git" directory stays out of your way, and you use the files and directories in the repository exactly the same way you'd use files and directories in a regular directory.

On the other hand, keeping files in a git repository has many advantages:

-   making it easier to collaborate with others on a project (whether that's an open source or closed source project)
-   making it easier to recover from screwups (like deleting important files, messing up code that was previously working, complete failure of your hard drive)
-   making it easier to share "works in progress" with TAs and instructors and fellow students to get help during lab, office hours, or by email
-   making it easier to share "open source" projects with others on the internet.

### What is github.ucsb.edu and github.com, and how do they differ from git?

A git repository can be local, on your file system, or it can be
remote on a server somewhere on the Internet. (We might say, using
terminology that is trendy these days, that a repo on the internet is
"in the cloud" if we get to remain blissfully ignorant of exactly how
that service is being provided to us—i,.e. someone else is worrying
about all the system management issues like keeping that server up and
running, keeping it free of malware and defending from Denial of
Service attacks, managing backups, etc.)

The github.com company is a commercial enterprise that runs a website
called github.com. Github.com provides a service for hosting github
repositories "in the cloud". The github.com company hosts open source
projects for free (via free public repositories) and makes money by
charging uses for hosting closed source projects in private
repositories.

In addition github licenses its software to various organizations that
want to set up their own private "github" like servers within their
enterprise. UCSB licensed this software and set up a github server
called github.ucsb.edu that is based on your CSIL account.

We may use github.com for some assignments and github.ucsb.edu for others.

<div data-role="collapsible" data-collapsed="false">
  <h2>More on git/github</h2>
  <ul>
   {% for topic in site.topics %}
       {% if topic.topic contains "git: " or topic.topic contains "github: "%} 
           <li><a href="{{topic.url}}">{{ topic.topic }}</a>&mdash;{{topic.desc}}</li>
       {% endif %}
   {% endfor %}
  </ul>
</div>
