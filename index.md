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
  {% include 8-or-16.md %}
</div>
</div>


{% include collapse-button.html label="Textbooks" id="textbook-list" %}
<div class="collapse" id="textbook-list">
 <div class="card card-body" markdown="1">
## Textbooks
{% include textbooks_list.html %}
</div>
</div>

{% include collapse-button.html label="Python Topics" id="python-topics" %}
<div class="collapse" id="python-topics">
 <div class="card card-body" markdown="1">
{% include ptopics_list.html %}
 </div>
</div>

{% include collapse-button.html label="Other Topics" id="other-topics" %}
<div class="collapse" id="other-topics">
 <div class="card card-body" markdown="1">
{% include topics_list.html %}
 </div>
</div>


{% include collapse-button.html label="Resources" id="resources" %}
<div class="collapse" id="resources">
<div class="card card-body" markdown="1">
{% include resources_list.html %}
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

