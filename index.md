---
title: UCSB CS8
---

# UCSB CMPSC 8: Introduction to Computer Science

also: CMPTGCS 20: Introduction to CS for non-majors

{% include collapse-button.html label="About this course" id="about" %}
<div class="collapse" id="about">
 <div class="card card-body" markdown="1">

CMPSC 8 is a course taught in the [Dept. of Computer Science](http://www.cs.ucsb.edu) at
[UC Santa Barbara](http://www.ucsb.edu).

A course covering many of the same topics, "Introduction to CS for non-majors" is occasionally taught in CCS under the number CMPTGCS 20.

This site is maintained in this github repo:
<https://github.com/ucsb-cs8/ucsb-cs8.github.io>.  If you are a
faculty member or TA that should have access to this page, contact
Phill Conrad or Diba Mirza to request permission.

 </div>
</div>

{% include collapse-button.html label="CS 8 Materials" id="materials" %}
<div class="collapse" id="materials">
 <div class="card card-body" markdown="1">

* [Catalog Description](https://www.cs.ucsb.edu/education/courses/cmpsc-8) including pre-requisites
* [Older materials from Conrad's 8wiki](https://foo.cs.ucsb.edu/8wiki) site.
* [Older materials from Conrad's personal website](https://www.cs.ucsb.edu/~pconrad/cs8)

Past offerings of CS8:

* [Winter 2018, Ziad Matni](https://ucsb-cs8-w18-matni.github.io)
* [Winter 2018, Richert Wang](https://ucsb-cs8-w18-wang.github.io)
* [Fall 2017, Diba Mirza](https://ucsb-cs8-f17.github.io)
* [Summer 2017, Phill Conrad](https://ucsb-cs8-m17.github.io)
* [Spring 2017, Ziad Matni](https://ucsb-cs8-s17.github.io)
* [Spring 2017, Mike Costanzo](https://www.cs.ucsb.edu/~mikec/cs8/)
* [Winter 2016, Omer Egecioglu] Available to CS Faculty on the ECI systems in  `/cs/archive/class/cs8/2017/winter/cs8/public_html`
* [Fall 2016, Matt Buoni](https://www.cs.ucsb.edu/~buoni/cs8/)
* [Summer 2016, Çetin Kaya Koç](http://koclab.cs.ucsb.edu/teaching/cs8/)
* [Summer 2015, Veronika Strnadova](https://www.cs.ucsb.edu/~veronika/cs8/)
* [Fall 2015, Çetin Kaya Koç and Emilie Barnard](http://emiliebarnard.com/teaching/cs8fall14/)
* [Summer 2009, Summer 2010, Fall 2010, Fall 2013](https://www.cs.ucsb.edu/~pconrad/cs8/)


 </div>
</div>



{% include collapse-button.html label="Should I take CS8 or CS16?" id="8-or-16" %}

<div class="collapse" id="8-or-16">
 <div class="card card-body" markdown="1">


## Which course should I start with? CS8 or CS16?

If you are taking your first course in Computer Science at UCSB, you may be wondering whether you should start in:

* CS8, which is intended as a first course in Programming
   * CS8 targets folks that have never programmed before, and it is taught in Python
* CS16, which is intended as a second programming course.
   * CS16 is taught in C++
   * CS16 does not assume prior background in C++
   * BUT, CS16 DOES assume prior background in programming (e.g. AP CS taught in Java)

So, there are some easy cases:

* If you have <em>never</em> programmed before, you should start with CS8.
* If you are <em>proficient</em> in Python or Java and confident of your programming abilities, but have not programmed in C++ before, you should start in CS16.

More nuanced cases are these:

* If you already do have some programming background, but you are not particularly confident of those abilities, or it's been a while and you need a refresher, you should likely start with CS8.
* If you are proficient in C++ itself as a result of taking community college courses, check <https://assist.org> to see if those courses articulate to CS 16 (officially known as CMPSC&nbsp;16) at UCSB.  If so, you may be able to start directly in a later course such as CMPSC 24.

If you are still not sure, you may need to talk with an adviser.  Brand new students can do this during summer orientation sessions when they register for courses.  Continuing students may visit the CS adviser in the main CS office on the 2nd floor of Harold Frank Hall.

</div>
</div>


{% include collapse-button.html label="Textbooks" id="textbook-list" %}
<div class="collapse" id="textbook-list">
 <div class="card card-body" markdown="1">

## Textbooks
    <ul>
      {% assign textbooks = site.textbooks | sort: 'custom_sort_order' %}
      {% for textbook in textbooks %}
         <li {% if topic.indent %} class="indent" {% endif %}><a href="{{textbook.url}}">{{ textbook.title }}</a>&mdash;{{textbook.desc}}</li>
      {% endfor %}
    </ul>

 </div>
</div>

{% include collapse-button.html label="Python Topics" id="python-topics" %}
<div class="collapse" id="python-topics">
 <div class="card card-body" markdown="1">


## Python Topics
  <ul>
   {% for topic in site.ptopics %}
     <li {% if topic.indent %} class="indent" {% endif %}><a href="{{topic.url}}">{{ topic.topic }}</a>&mdash;{{topic.desc}}</li>
   {% endfor %}
  </ul>

 </div>
</div>

{% include collapse-button.html label="Other Topics" id="other-topics" %}
<div class="collapse" id="other-topics">
 <div class="card card-body" markdown="1">

## Other Topics

  <ul>
   {% for topic in site.topics %}
     <li {% if topic.indent %} class="indent" {% endif %}><a href="{{topic.url}}">{{ topic.topic }}</a>&mdash;{{topic.desc}}</li>
   {% endfor %}
  </ul>

 </div>
</div>


{% include collapse-button.html label="Resources" id="resources" %}
<div class="collapse" id="resources">
 <div class="card card-body" markdown="1">

## Resources

  <ul>
   {% for topic in site.resources %}
     <li {% if topic.indent %} class="indent" {% endif %}><a href="{{topic.url}}">{{ topic.topic }}</a>&mdash;{{topic.desc}}</li>
   {% endfor %}
  </ul>

 </div>
</div>



{% include collapse-button.html label="Tutorials" id="tutorials" %}
<div class="collapse" id="tutorials">
 <div class="card card-body" markdown="1">

## Tutorials

  <ul>
   {% for t in site.tutorials %}
     <li {% if t.indent %} class="indent" {% endif %} ><a href="{{t.url}}">{{ t.topic }}</a>&mdash;{{t.desc}}</li>
   {% endfor %}
  </ul>

 </div>
</div>

