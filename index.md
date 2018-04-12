---
title: UCSB CS8
---

<h1>UCSB CMPSC 8: Introduction to Computer Science</h1>
<h2>(also: CMPTGCS 20: Introduction to CS for non-majors)</h2>

<div id="about" data-role="collapsible" data-collapsed="true" markdown="1">
<h2>About this course</h2>

CMPSC 8 is a course taught in the [Dept. of Computer Science](http://www.cs.ucsb.edu) at
[UC Santa Barbara](http://www.ucsb.edu).

A course covering many of the same topics, "Introduction to CS for non-majors" is occasionally taught in CCS under the number CMPTGCS 20.

This site is maintained in this github repo: <https://github.com/ucsb-cs8/ucsb-cs8.github.io>.   If you are a CS department faculty member or TA that should have access to this page, contact Phill Conrad to request permission.

# CS8 materials

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

</div><!-- about -->


<div id="textbooks" data-role="collapsible" data-collapsed="false">
  <h2>Textbooks</h2>
    <ul>
      {% assign textbooks = site.textbooks | sort: 'custom_sort_order' %}
      {% for textbook in textbooks %}
         <li {% if topic.indent %} class="indent" {% endif %}><a href="{{textbook.url}}">{{ textbook.title }}</a>&mdash;{{textbook.desc}}</li>
      {% endfor %}
    </ul>
</div>

<div id="ptopics" data-role="collapsible" data-collapsed="false">
  <h2>Python Topics</h2>
  <ul>
   {% for topic in site.ptopics %}
     <li {% if topic.indent %} class="indent" {% endif %}><a href="{{topic.url}}">{{ topic.topic }}</a>&mdash;{{topic.desc}}</li>
   {% endfor %}
  </ul>
</div>

<div id="topics" data-role="collapsible" data-collapsed="false">
  <h2>Other Topics</h2>
  <ul>
   {% for topic in site.topics %}
     <li {% if topic.indent %} class="indent" {% endif %}><a href="{{topic.url}}">{{ topic.topic }}</a>&mdash;{{topic.desc}}</li>
   {% endfor %}
  </ul>
</div>



<div id="resources" data-role="collapsible" data-collapsed="false">
  <h2>Resources</h2>
  <ul>
   {% for topic in site.resources %}
     <li {% if topic.indent %} class="indent" {% endif %}><a href="{{topic.url}}">{{ topic.topic }}</a>&mdash;{{topic.desc}}</li>
   {% endfor %}
  </ul>
</div>

<div id="tutorials" data-role="collapsible" data-collapsed="false">
  <h2>Tutorials</h2>
  <ul>
   {% for t in site.tutorials %}
     <li {% if t.indent %} class="indent" {% endif %} ><a href="{{t.url}}">{{ t.topic }}</a>&mdash;{{t.desc}}</li>
   {% endfor %}
  </ul>
</div>

