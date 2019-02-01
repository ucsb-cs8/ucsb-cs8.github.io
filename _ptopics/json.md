---
topic: "json"
desc: "Access JSON data in Python"
---

# Quick overview (more detail later in file)

## Read json  from file into Python object (dict or list)

Source: <https://stackoverflow.com/questions/20199126/reading-json-from-a-file>

```python
import json

with open('strings.json') as json_data:
    d = json.load(json_data)

print(d)
```

The `print(d)` is just a way to show that we have the data.

## Read json data from url into Python object (dict or list)

```
import requests
import json

def getJsonFromURL(url):

    # requests.get(url) goes and fetches a web page (like a browser does)                                                   
    # httpReponse is an object representing the response from the web                                                

    httpResponse = requests.get(url)

    # httpResponse.text is the text from the webpage                                                                        
    # jsonData is a Python dictionary or list converted from the JSON                                                       
    jsonData = json.loads(httpResponse.text)
    return jsonData
```

## Write json from dict to file

Source: <https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file>

```
import json
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
``` 

# Python: More detail about accessing JSON Data 

There is a notation called *JSON*, which stands for *JavaScript Object Notation*.  Although this notation
comes from the language *JavaScript*, it is used across many languages other than JavaScript, including Python.

Many websites and other data services provide access to data in JSON format.  

One easy example to see is the social media site [reddit.com](https://reddit.com).  

* Side note: Before going further, let us
    acknowledge that there are some controversies about the [reddit.com](https://reddit.com) site, some of which
    provoke passionate opinions.  If there were a better example website, I would use it.   The reason I use
    reddit.com is not because I necessarily endorse the site, but because it is one of the easiest sites for
    beginners to get access to JSON data easily and quickly.

The site reddit.com has various online communities called *subreddits*.  Most college/universities have one;
for example, here are the ones for the various UC Campuses with undergraduate programs:

| School	| Subreddit link	| School web page   |
|---------|-----------------|-------------------|
| UC Berkeley	| http://www.reddit.com/r/berkeley/	| http://www.berkeley.edu |
| UC Davis	| 	http://www.reddit.com/r/ucdavis	| 	http://www.ucdavis.edu	| 
| UC Irvine		| http://www.reddit.com/r/uci		| 	| http://www.uci.edu	| 
| UCLA	| 	http://www.reddit.com/r/ucla/		| http://www.ucla.edu	| 
| UC Merced		| http://www.reddit.com/r/ucmerced	| 	http://www.ucmerced.edu/	| 
| UC Riverside	| 	http://www.reddit.com/r/ucr/	| 	www.ucr.edu	| 
| UC San Diego	| 	http://www.reddit.com/r/ucsd	| 	http://www.ucsd.edu	| 
| UC Santa Barbara	| 	http://www.reddit.com/r/ucsantabarbara	| 	http://www.ucsb.edu	| 
| UC Santa Cruz	| 	http://www.reddit.com/r/ucsc	| 	http://www.ucsc.edu	| 

Suppose you visit the page for the UCSD subreddit.  If you simply add the following characters: `.json` to the URL,
you'll get a representation of the content of the page in JSON format:


* UCSD Subreddit: http://www.reddit.com/r/ucsd
* UCSD Subreddit in JSON format: http://www.reddit.com/r/ucsd.json

Here is a snapshot of what some of that JSON looks like.  Because it goes on for pages and pages,
I'm showing only the first few lines, and this excerpt will likely *not* be valid since its clipped off in the middle.

```json
{"kind": "Listing", "data": {"modhash": "", "children": [{"kind": "t3", "data": 
{"domain": "self.UCSD", "banned_by": null, "media_embed": {}, "subreddit": "UCSD",
"selftext_html": "&lt;!-- SC_OFF --&gt;&lt;div class=\"md\"&gt;&lt;p&gt;I&amp;#39;m 
basically just copying this directly from last year&amp;#39;s Q&amp;amp;A, but
I don&amp;#39;t think many things have changed. (so thank &lt;a 
href=\"/u/inconditus\"&gt;/u/inconditus&lt;/a&gt; for this, because they wrote most
of it)&lt;/p&gt;\n\n&lt;p&gt;So, you got into UCSD, congratulations! It&amp;#39;s a
great school! But you have questions, most of which the administration can&amp;#39;t 
help you with. Come ask us! I&amp;#39;m rolling over a lot of info from the &lt;a 
```
etc...

The point is that data in JSON format can be easily converted into a Python dictionary.

Here's how.

First, here is some code that we can type in at the Python prompt just to experiment a bit.

There is a Python module called `requests` that we can use to get data from a website.

We simply type `import requests`, then assign a variable to the result of `requests.get(url)`,
where `url` is a Python string with a web address.  For example:

```
import requests
result = requests.get("https://www.reddit.com/r/ucsd.json")
```

Note: If you get an error "too many requests", you may need to set a custom "user-agent".  Here is an article that
explains the process: [Python: Requests: User-Agent](/topics/python-requests-user-agent.md)

The short version is that you should write your request like this, except put your name where it says your-name-here.   If that doesn't fix the problem, see the   [Python: Requests: User-Agent](/topics/python-requests-user-agent.md) article for more detail.

```python
import requests
result = requests.get("http://www.reddit.com/r/ucsd.json", headers = {'User-agent': 'spis16 your-name-here'})
```

Now, if we type `result.text`, we get the entire contents of that web page (in this case, all the JSON that
was returned.   I'm not showing the whole thing, because it is enormous.  Here are just the first 100 characters:



```
>>> result.text[:400]
u'{"kind": "Listing", "data": {"modhash": "", "children": [{"kind": "t3", "data": {"domain": 
"self.UCSD", "banned_by": null, "media_embed": {}, "subreddit": "UCSD", "selftext_html":
"&lt;!-- SC_OFF --&gt;&lt;div class=\\"md\\"&gt;&lt;p&gt;I&amp;#39;m basically just copying
this directly from last year&amp;#39;s Q&amp;amp;A, but I don&amp;#39;t think many things
have changed. (so thank &lt;a href=\\"/u/'
>>> 
```

We can see how big it is by using `len`.  The `type` comes back as `unicode` rather than `str`;
that just means that it is a special type of string, one that may have various kinds of international
characters in it. (That's an oversimplification of what unicode is, but if you are curious, you can 
look up the details yourself.)

```
>>> len(result.text)
67435
>>> type(result.text)
<type 'unicode'>
>>>
```

We can convert the `result.text` into a Python dictionary using the following Python code:

```python
>>> import json
>>> rdata = json.loads(result.text)
>>> type(rdata)
<type 'dict'>
>>> 
```

Now, `rdata` is a Python dictionary that contains the data from the UCSD subreddit that we retrieved.

This opens up many possibilities for processing the data using Python code.

But what?

One of the problems with this `rdata` dictionary is that it is so big.   If we try to see all of it, it goes
on for pages and page:

```python
>>> rdata
{u'kind': u'Listing', u'data': {u'modhash': u'', u'children': [{u'kind': u't3', u'data': {u'domain': u'self.UCSD', u'banned_by': None, u'media_embed': {}, u'subreddit': u'UCSD', u'selftext_html': u'&
```
<em>... dozens of lines omitted ... </em>
```
se, u'created': 1471193347.0, u'url': u'https://www.reddit.com/r/UCSD/comments/4xnf96/fraternities_or_dance_groups/', u'author_flair_text': None, u'quarantine': False, u'title': u'Fraternities or dance groups?', u'created_utc': 1471164547.0, u'ups': 3, u'num_comments': 4, u'visited': False, u'num_reports': None, u'distinguished': None}}], u'after': u't3_4xnf96', u'before': None}}
>>>
```

So, what can we do?   One possibility is to just find out: what keys are at the top level of this dictionary?

We can do that by typing `rdata.keys()`.   (Note that the `u` in front of `kind` and `data` just indicates
that it is a unicode string instead of a regular string.)

```python
>>> rdata.keys()
[u'kind', u'data']
>>> 
```

So, we know that, at the top level, the dictionary `rdict` contains two key value pairs.  That is, 
it is of the form `rdata = { u'kind': `<em>something</em>`, u'data': `<em>something-else</em>` }`

So, we can try to next figure out, what is the <em>something</em> and the <em>something-else</em>.

The first <em>something</em> is going to accessed by `rdata[u'kind']`:

```python
>>> rdata[u'kind']
u'Listing'
>>> 
```

We see that it is a `Listing'.   So, let's figure out what the <em>something-else</em> is.  We type
`rdata[u'data']` and we get another super long listing:

```python
>>> rdata[u'data']
```
<em>way too much output here...</em>
```
>>> 
```

So, instead of listing the whole thing, we
can try to ask another question: what <em>type</em> thing is it?

```python
>>> type(rdata[u'data'])
<type 'dict'>
>>> 
```

Ah, that is better.  We see that it is a dictionary object. So we can repeat the process we used before with
a "too big" dictionary, that is, asking what its keys are:

```python
>>> rdata[u'data'].keys()
[u'modhash', u'children', u'after', u'before']
>>>
```

What we get back is a python list of the keys for `rdata[u'data']`.    We see that there are four of them:

1. `u'modhash'`
1. `u'children'` 
1. `u'after'` 
1. `u'before'`

We can represent what we've learned about `rdata` so far by drawing a diagram.  It looks like this:

<img src="https://docs.google.com/drawings/d/1zRIQIeaTI3-AZskqwvYvtwv_3Q_EPQnGtZqi-HdTtBE/pub?w=966&amp;h=422">

The four question marks represent: what is under each of those four keys ( `u'modhash'`,`u'children'`,`u'after'`, and `u'before'`)?

How can we tell?

The first thing we might want to do is examine each of their types.    From this we see that two of them
are unicode strings, one is a list, and one has `NoneType`, meaning that is is a missing value.

```python
>>> type(rdata[u'data'][u'modhash'])
<type 'unicode'>
>>> type(rdata[u'data'][u'children'])
<type 'list'>
>>> type(rdata[u'data'][u'after'])
<type 'unicode'>
>>> type(rdata[u'data'][u'before'])
<type 'NoneType'>
>>> 
```

We can quickly check the values of the two unicode strings:

```python
>>> rdata[u'data'][u'modhash']
u''
>>> rdata[u'data'][u'after']
u't3_4xnf96'
>>> 
```

The interesting part is under the `u'children'` key.   That turns out to be a list.  Let's find out how long
the list is:

```python
>>> len(rdata[u'data'][u'children'])
27
>>>
```

Ah, so let's just look at the first element of that list.    We might assume that each of the others probably
has a similar structure.  Unfortunately, we are right back at the stage where the thing we get is "too big":

```python
>>> rdata[u'data'][u'children'][0]
{u'kind': u't3', u'data': {u'domain': u'self.UCSD', u'banned_by': None, u'media_embed': {}, u'subreddit': u'UCSD', u'selftext_html': u'&lt;!-- SC_OFF --&gt;&lt;div class="md"&gt;&lt;p&gt;I&amp;#39;m basically just copying this directly from last year&amp;#39;s Q&amp;amp;A, but I don&amp;#39;t think m
```
<em>much too many lines of output here...</em>
```
r/UCSD/comments/4cgr1w/new_student_qa_2016/', u'author_flair_text': u'History (B.A.)', u'quarantine': False, u'title': u'New Student Q&amp;A 2016', u'created_utc': 1459275768.0, u'ups': 51, u'num_comments': 277, u'visited': False, u'num_reports': None, u'distinguished': None}}
>>>
```

So, the solution is NOT to give up!  But rather, to keep going in the direction we are going, documenting our progress
with a diagram.  Eventually, we *will* get to a structure that makes sense, that we can do some computation over, that, is some thing that represents a single reddit post, or a single comment on a single reddit post, etc.

Let's update our diagram with what we know about the next level:

<img src="https://docs.google.com/drawings/d/1UffljEjItYnKseSb3UE_SVZyFalcrid1-AxjqsrEPmg/pub?w=961&amp;h=441">

Now, let's dive into the list of 27 things that is under `rdata[u'data'][u'children']`

```python
>>> type(rdata[u'data'][u'children'])
<type 'list'>
>>> len(rdata[u'data'][u'children'])
27
>>> 
```

We apply our technique, recursively, to the first element of this list.  That is, we first examine what the keys are,
and what the types of each of the values are.   

```
>>> rdata[u'data'][u'children'][0].keys()
[u'kind', u'data']
>>> 
```

And, when we say "recursively", we truly aren't kidding!  It appears that the first element of this list has the same keys
as the entire result we got back for this page.    Let's check the types&mdash;it won't be surprising if they are the same as what we saw before for these keys:

```python
>>> type(rdata[u'data'][u'children'][0][u'kind'])
<type 'unicode'>
>>> type(rdata[u'data'][u'children'][0][u'data'])
<type 'dict'>
>>> 
```

So, since the first one is of type `unicode`, let's just see what it is:

```python
>>> rdata[u'data'][u'children'][0][u'kind']
u't3'
>>> 
```

It is at this point that I will come clean, and tell you that I could have saved you a lot of time by just pointing you to the documentation for the Reddit API, where all of this is explained, including what the value u`t3` in this case represents.  But what fun would that have been?  You've learned an awful lot about how to investigate an API by simply looking directly at the data you are getting and trying to make sense of it.  And that is a useful skill!

* The Reddit API documentation: [https://www.reddit.com/dev/api/](https://www.reddit.com/dev/api/)

On that page, among other things, we learn that `t3` is the type for links.   Let's take a look at the u'data' part of this
`[0]` element of our children here:

```python
>>> rdata[u'data'][u'children'][0][u'data'].keys()
[u'domain', u'banned_by', u'media_embed', u'subreddit', u'selftext_html', u'selftext', u'likes', 
 u'suggested_sort', u'user_reports', u'secure_media', u'link_flair_text', u'id', u'from_kind', 
 u'gilded', u'archived', u'clicked', u'report_reasons', u'author', u'media', u'name', u'score',
 u'approved_by', u'over_18', u'hidden', u'thumbnail', u'subreddit_id', u'edited', u'link_flair_css_class', u'author_flair_css_class', u'downs', u'mod_reports', u'secure_media_embed', u'saved', 
 u'removal_reason', u'stickied', u'from', u'is_self', u'from_id', u'permalink', u'locked', 
 u'hide_score', u'created', u'url', u'author_flair_text', u'quarantine', u'title', u'created_utc', 
 u'ups', u'num_comments', u'visited', u'num_reports', u'distinguished']
>>> 
```

This finally looks like something that might be useful.  In fact, this represents a single Reddit Post.   A few of the things we might be interested in right away are the values with these keys:

* `u'title'`
* `u'url'`

Let's see what we get for those:

```python
>>> rdata[u'data'][u'children'][0][u'data']['title']
u'New Student Q&amp;A 2016'
>>> rdata[u'data'][u'children'][0][u'data']['url']
u'https://www.reddit.com/r/UCSD/comments/4cgr1w/new_student_qa_2016/'
>>>
```

The `&amp;` is HTML for the `&` symbol.  So when this appears on a web page, it will simply appear as `New Student Q&A 2016`.    
# Another useful tool for working with JSON data: `pprint.pprint`

The `pprint` module (pretty print) provides a super handy tool for looking at large complex dictionary objects in Python.

Let's go back to the original example.   We now know that these four lines of code will grab some data from the UCSD subreddit and put it into a Python dictionary:

```python
>>> import requests
>>> result = requests.get("http://www.reddit.com/r/ucsd.json", headers = {'User-agent': 'spis16 your-name-here'})
>>> import json
>>> rdata = json.loads(result.text)
>>> 
```

We also know that if we type `rdata` at the Python prompt, the output will be long and dense:

```python
>>> rdata
{u'kind': u'Listing', u'data': {u'modhash': u'', u'children': [{u'kind': u't3', u'data': {u'domain': u'self.UCSD',
u'banned_by': None, u'media_embed': {}, u'subreddit': u'UCSD', u'selftext_html': u'&lt;!-- SC_OFF --&gt;&lt;div
class="md"&gt;&lt;p&gt;I&amp;#39;m basically just copying this directly from last year&amp;#39;s Q&amp;amp;A, but
I don&amp;#39;t think many things have changed. (so thank &lt;a href="/u/inconditus"&gt;/u/inconditus&lt;/a&g
```
<em>many lines omitted</em>
```python
ainst Students Due Process', u'created_utc': 1472075072.0, u'ups': 30, u'num_comments': 2, u'visited': False, u'num_reports': None, u'distinguished': None}}], u'after': u't3_4zf0b0', u'before': None}}
>>>
```
So there are two issues here: the *long* part, and the *dense* part.

The *long* part has to be tackled with the tools we've already discussed: going top down by keys to find a way to select out, for example, the dictionary for single post, like this:

```
>>> rdata[u'data'][u'children'][0][u'data']
{u'domain': u'self.UCSD', u'banned_by': None, u'media_embed': {}, u'subreddit': u'UCSD', u'selftext_html': u'&lt;!-- 
SC_OFF --&gt;&lt;div class="md"&gt;&lt;p&gt;I&amp;#39;m basically just copying this directly from last year&amp;#39;s
Q&amp;amp;A, but I don&amp;#39;t think many things have changed. (so thank &lt;ahref="/u/inconditus"&gt;/u/inconditus&lt;/a&gt; for this, because they wrote most of it)&lt;/p&gt;\n\n&lt;p&gt;So,
you got into UCSD, congratulations! It&amp;#39;s a great school! But you have questions, most of which the administration
```
<em>many lines of output omitted</em>
```python
u'removal_reason': None, u'stickied': True, u'from': None, u'is_self': True, u'from_id': None, u'permalink':
u'/r/UCSD/comments/4cgr1w/new_student_qa_2016/', u'locked': False, u'hide_score': False, u'created': 1459304568.0,
u'url': u'https://www.reddit.com/r/UCSD/comments/4cgr1w/new_student_qa_2016/', u'author_flair_text': u'History (B.A.)',
u'quarantine': False, u'title': u'New Student Q&amp;A 2016', u'created_utc': 1459275768.0, u'ups': 49, u'num_comments': 305,
u'visited': False, u'num_reports': None, u'distinguished': None}
>>> 
```

This is still a bit long, but at least now it is small enough that we can scroll back through it.   Can we do something about the "dense" part?  We can, using `pprint`.  Observe.   This time I *am* going to leave the entire output here, even though 
one part of it will scroll "way" off the screen.

From the output below, we can see all of the keys for elements of a single post quite clearly.   We can also see that 
the only two values  in this dictionary representing a single Reddit post that are "huge" are the values for the keys `selftext` and `selftext_html`.    Those are the values that contain the actual text of the post&mdash;the `selftext` version is plain text, while the `selftext_html` contains the HTML markup, with various symbols "escaped" using symbols such as `&lt;` for `<`.    

```python
>>> from pprint import pprint
>>> thisPost = rdata[u'data'][u'children'][0][u'data']
>>> pprint(thisPost)
>>> pprint(thisPost)
{u'approved_by': None,
 u'archived': False,
 u'author': u'ThumbtacksArePointy',
 u'author_flair_css_class': u'',
 u'author_flair_text': u'History (B.A.)',
 u'banned_by': None,
 u'clicked': False,
 u'created': 1459304568.0,
 u'created_utc': 1459275768.0,
 u'distinguished': None,
 u'domain': u'self.UCSD',
 u'downs': 0,
 u'edited': False,
 u'from': None,
 u'from_id': None,
 u'from_kind': None,
 u'gilded': 0,
 u'hidden': False,
 u'hide_score': False,
 u'id': u'4cgr1w',
 u'is_self': True,
 u'likes': None,
 u'link_flair_css_class': None,
 u'link_flair_text': None,
 u'locked': False,
 u'media': None,
 u'media_embed': {},
 u'mod_reports': [],
 u'name': u't3_4cgr1w',
 u'num_comments': 305,
 u'num_reports': None,
 u'over_18': False,
 u'permalink': u'/r/UCSD/comments/4cgr1w/new_student_qa_2016/',
 u'quarantine': False,
 u'removal_reason': None,
 u'report_reasons': None,
 u'saved': False,
 u'score': 49,
 u'secure_media': None,
 u'secure_media_embed': {},
 u'selftext': u'I\'m basically just copying this directly from last year\'s Q&amp;A, but I don\'t think many things have changed. (so thank /u/inconditus for this, because they wrote most of it)\n\nSo, you got into UCSD, congratulations! It\'s a great school! But you have questions, most of which the administration can\'t help you with. Come ask us! I\'m rolling over a lot of info from the [2014 edition](http://www.reddit.com/r/UCSD/comments/21uxq7/new_student_qa_2014_edition/) and [2013 edition](http://www.reddit.com/r/UCSD/comments/1c187y/official_new_student_qa_2013/) and [2015 edition](http://www.reddit.com/r/UCSD/comments/32p9ng/new_student_qa_2015/). Thanks to /u/nervette and everyone else for compiling this information.\n\nFirst up: "What are the housing deadlines?" Check out the [housing deadlines here!](http://housing.ucsd.edu/deadlines.asp)\n\nWanna know what all the acronyms and abbreviations we\'re throwing around mean? [There\'s a list for that](http://blink.ucsd.edu/sponsor/blink/AA.html)\n\n"What are the major differences between the colleges?/I got into Miur, what does that even mean?" There are 2 things: The housing units for each college are separate. [Here\'s a map](http://maps.ucsd.edu/mapping/viewer/default.htm) and they all have separate general ed requirements. check it out:  \n[ERC gen eds.](http://roosevelt.ucsd.edu/academics/gen-ed/index.html)- [Marshall gen eds.](https://marshall.ucsd.edu/academics/general-education-requirements.html)- [Muir gen eds.](http://muir.ucsd.edu/academics/degree_reqs.html)- [Revelle gen eds.](http://revelle.ucsd.edu/academics/general-education/index.html)- [Warren gen eds.](http://warren.ucsd.edu/academics/advising/acad-req.html)- [6th gen eds.](http://www.sixth.ucsd.edu/advising/requirements/index.html)\n\n"Which of my AP\'s will give me credit towards what?" I have no idea, look it up on this handy [AP credit chart](http://www.ucsd.edu/catalog/pdf/APC-chart.pdf). Also, check out the [International Baccalaureate (IB) chart]( http://www.ucsd.edu/catalog/pdf/IBC-chart.pdf).\n\nTake a look at the list of UCSD\'s [Student Organizations](http://tonga.ucsd.edu/studentorgregistration/RdOnlyList.aspx) if you\'re interested in getting involved. Here\'s the [Greek website](http://www.tritongreeks.org/) if you\'re into that, too.\n\nWanna know how many units you can transfer? According to the UCSD catalog: "The university will award graduation credit for up to seventy semester (105 quarter) units of transferable course work from a community college. Courses in excess of seventy semester units will receive subject credit and may be used to satisfy university subject requirements."\n\nThe MARSHALL list of approved classes for the Significant Writing Course requirement is [here](http://marshall.ucsd.edu/pdfs/Sig_Writing.pdf)\n\n/u/iGiveProTips takes you on an [epic tour](http://www.reddit.com/r/UCSD/comments/1c187y/official_new_student_qa_2013/c9gn7ih) of campus, complete with bathroom ratings.\n\n /u/delicious_truffles kindly made a thread for entering CS:BioInfo in 2012/2011. If that is your intended major, [check it out.](http://www.reddit.com/r/UCSD/comments/jra8a/incoming_freshman_with_questions/)\n\nOn a waitlist? Remember the Adam Powers Rule of Waitists, for any given class, around 10% of those enrolled with drop it. So you\'re #20 on the waitlist for 500 person class? You\'ll probably get in. The cravats being: if the class is super easy and popular (or Magagna), or it is a class required for an impacted major, then the drop rate goes down. Otherwise, be patient, have a back up, but have faith.\n\nIf you want fancy flair, on the sidebar under the subscribe button, check the show my flair, then hit edit and select your intended major! There is even an undeclared, for those who don\'t know yet.\n\nI\'ll be keeping an eye on this until the start of Fall Quarter, as will several others. \n\n**ALSO, GUYS, READ THIS THING:** [**SCHEDULES PSA**](http://www.reddit.com/r/UCSD/comments/1jh8hz/psa_for_freshmen_and_new_transfers_regarding)  I am serious. I know it\'s a wall of text, and I know you are in college now and know everything, but remember this is the quarter system. You only get 10 weeks before finals. Don\'t burn out. Seriously, this is super important.\n\n# Ask questions below!',
 u'selftext_html': u'&lt;!-- SC_OFF --&gt;&lt;div class="md"&gt;&lt;p&gt;I&amp;#39;m basically just copying this directly from last year&amp;#39;s Q&amp;amp;A, but I don&amp;#39;t think many things have changed. (so thank &lt;a href="/u/inconditus"&gt;/u/inconditus&lt;/a&gt; for this, because they wrote most of it)&lt;/p&gt;\n\n&lt;p&gt;So, you got into UCSD, congratulations! It&amp;#39;s a great school! But you have questions, most of which the administration can&amp;#39;t help you with. Come ask us! I&amp;#39;m rolling over a lot of info from the &lt;a href="http://www.reddit.com/r/UCSD/comments/21uxq7/new_student_qa_2014_edition/"&gt;2014 edition&lt;/a&gt; and &lt;a href="http://www.reddit.com/r/UCSD/comments/1c187y/official_new_student_qa_2013/"&gt;2013 edition&lt;/a&gt; and &lt;a href="http://www.reddit.com/r/UCSD/comments/32p9ng/new_student_qa_2015/"&gt;2015 edition&lt;/a&gt;. Thanks to &lt;a href="/u/nervette"&gt;/u/nervette&lt;/a&gt; and everyone else for compiling this information.&lt;/p&gt;\n\n&lt;p&gt;First up: &amp;quot;What are the housing deadlines?&amp;quot; Check out the &lt;a href="http://housing.ucsd.edu/deadlines.asp"&gt;housing deadlines here!&lt;/a&gt;&lt;/p&gt;\n\n&lt;p&gt;Wanna know what all the acronyms and abbreviations we&amp;#39;re throwing around mean? &lt;a href="http://blink.ucsd.edu/sponsor/blink/AA.html"&gt;There&amp;#39;s a list for that&lt;/a&gt;&lt;/p&gt;\n\n&lt;p&gt;&amp;quot;What are the major differences between the colleges?/I got into Miur, what does that even mean?&amp;quot; There are 2 things: The housing units for each college are separate. &lt;a href="http://maps.ucsd.edu/mapping/viewer/default.htm"&gt;Here&amp;#39;s a map&lt;/a&gt; and they all have separate general ed requirements. check it out:&lt;br/&gt;\n&lt;a href="http://roosevelt.ucsd.edu/academics/gen-ed/index.html"&gt;ERC gen eds.&lt;/a&gt;- &lt;a href="https://marshall.ucsd.edu/academics/general-education-requirements.html"&gt;Marshall gen eds.&lt;/a&gt;- &lt;a href="http://muir.ucsd.edu/academics/degree_reqs.html"&gt;Muir gen eds.&lt;/a&gt;- &lt;a href="http://revelle.ucsd.edu/academics/general-education/index.html"&gt;Revelle gen eds.&lt;/a&gt;- &lt;a href="http://warren.ucsd.edu/academics/advising/acad-req.html"&gt;Warren gen eds.&lt;/a&gt;- &lt;a href="http://www.sixth.ucsd.edu/advising/requirements/index.html"&gt;6th gen eds.&lt;/a&gt;&lt;/p&gt;\n\n&lt;p&gt;&amp;quot;Which of my AP&amp;#39;s will give me credit towards what?&amp;quot; I have no idea, look it up on this handy &lt;a href="http://www.ucsd.edu/catalog/pdf/APC-chart.pdf"&gt;AP credit chart&lt;/a&gt;. Also, check out the &lt;a href="http://www.ucsd.edu/catalog/pdf/IBC-chart.pdf"&gt;International Baccalaureate (IB) chart&lt;/a&gt;.&lt;/p&gt;\n\n&lt;p&gt;Take a look at the list of UCSD&amp;#39;s &lt;a href="http://tonga.ucsd.edu/studentorgregistration/RdOnlyList.aspx"&gt;Student Organizations&lt;/a&gt; if you&amp;#39;re interested in getting involved. Here&amp;#39;s the &lt;a href="http://www.tritongreeks.org/"&gt;Greek website&lt;/a&gt; if you&amp;#39;re into that, too.&lt;/p&gt;\n\n&lt;p&gt;Wanna know how many units you can transfer? According to the UCSD catalog: &amp;quot;The university will award graduation credit for up to seventy semester (105 quarter) units of transferable course work from a community college. Courses in excess of seventy semester units will receive subject credit and may be used to satisfy university subject requirements.&amp;quot;&lt;/p&gt;\n\n&lt;p&gt;The MARSHALL list of approved classes for the Significant Writing Course requirement is &lt;a href="http://marshall.ucsd.edu/pdfs/Sig_Writing.pdf"&gt;here&lt;/a&gt;&lt;/p&gt;\n\n&lt;p&gt;&lt;a href="/u/iGiveProTips"&gt;/u/iGiveProTips&lt;/a&gt; takes you on an &lt;a href="http://www.reddit.com/r/UCSD/comments/1c187y/official_new_student_qa_2013/c9gn7ih"&gt;epic tour&lt;/a&gt; of campus, complete with bathroom ratings.&lt;/p&gt;\n\n&lt;p&gt;&lt;a href="/u/delicious_truffles"&gt;/u/delicious_truffles&lt;/a&gt; kindly made a thread for entering CS:BioInfo in 2012/2011. If that is your intended major, &lt;a href="http://www.reddit.com/r/UCSD/comments/jra8a/incoming_freshman_with_questions/"&gt;check it out.&lt;/a&gt;&lt;/p&gt;\n\n&lt;p&gt;On a waitlist? Remember the Adam Powers Rule of Waitists, for any given class, around 10% of those enrolled with drop it. So you&amp;#39;re #20 on the waitlist for 500 person class? You&amp;#39;ll probably get in. The cravats being: if the class is super easy and popular (or Magagna), or it is a class required for an impacted major, then the drop rate goes down. Otherwise, be patient, have a back up, but have faith.&lt;/p&gt;\n\n&lt;p&gt;If you want fancy flair, on the sidebar under the subscribe button, check the show my flair, then hit edit and select your intended major! There is even an undeclared, for those who don&amp;#39;t know yet.&lt;/p&gt;\n\n&lt;p&gt;I&amp;#39;ll be keeping an eye on this until the start of Fall Quarter, as will several others. &lt;/p&gt;\n\n&lt;p&gt;&lt;strong&gt;ALSO, GUYS, READ THIS THING:&lt;/strong&gt; &lt;a href="http://www.reddit.com/r/UCSD/comments/1jh8hz/psa_for_freshmen_and_new_transfers_regarding"&gt;&lt;strong&gt;SCHEDULES PSA&lt;/strong&gt;&lt;/a&gt;  I am serious. I know it&amp;#39;s a wall of text, and I know you are in college now and know everything, but remember this is the quarter system. You only get 10 weeks before finals. Don&amp;#39;t burn out. Seriously, this is super important.&lt;/p&gt;\n\n&lt;h1&gt;Ask questions below!&lt;/h1&gt;\n&lt;/div&gt;&lt;!-- SC_ON --&gt;',
 u'stickied': True,
 u'subreddit': u'UCSD',
 u'subreddit_id': u't5_2r6sq',
 u'suggested_sort': u'new',
 u'thumbnail': u'self',
 u'title': u'New Student Q&amp;A 2016',
 u'ups': 49,
 u'url': u'https://www.reddit.com/r/UCSD/comments/4cgr1w/new_student_qa_2016/',
 u'user_reports': [],
 u'visited': False}
>>> 
```

# pprint with a depth parameter

If this pprint thing is so good, why not apply it to the entire `rdata` variable?

If we try that, unfortunately, we still get the problem of the output being `too long`.

But, there is a workaround for that.   We don't have to print "all the way down the tree".

Consider, again the "tree" representation of the dictionary `rdata`.  Here, again, is a diagram that shows just the top few levels.

<img src="https://docs.google.com/drawings/d/1UffljEjItYnKseSb3UE_SVZyFalcrid1-AxjqsrEPmg/pub?w=961&amp;h=441">

We can tell `pprint` to only print a certain number of levels of a dictionary.  That allows us to do the exploration with did above using `.keys()` and `.values()` much more efficiently.  Here's what that looks like.   We add a parameter `levels=1`, `levels=2`, etc. to restrict how far down the tree to go:

```python
>>> pprint(rdata,depth=1)
{u'data': {...}, u'kind': u'Listing'}
>>> pprint(rdata,depth=2)
{u'data': {u'after': u't3_4zf0b0',
           u'before': None,
           u'children': [...],
           u'modhash': u''},
 u'kind': u'Listing'}
>>> pprint(rdata,depth=3)
{u'data': {u'after': u't3_4zf0b0',
           u'before': None,
           u'children': [{...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...},
                         {...}],
           u'modhash': u''},
 u'kind': u'Listing'}
>>> pprint(rdata,depth=4)
{u'data': {u'after': u't3_4zf0b0',
           u'before': None,
           u'children': [{u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'},
                         {u'data': {...}, u'kind': u't3'}],
           u'modhash': u''},
 u'kind': u'Listing'}
>>> 

```

If we go as far as `levels=5`, that's when the output becomes too long to reasonably display.  But by then, we already have enough information to write the expression:

```
pprint(rdata['data']['children'][0]['data']
```

which gives us the data for one post.   By iterating over a slice of the children, we could get, say, the first five posts from that list.

```python
for post in rdata['data']['children'][0:5]:
  pprint(post['data'])
```

As it turns out, even the first five is too long to effectively use copy/paste to get the output into this article, but here is the first "two" posts:

```python
>>> for post in rdata['data']['children'][0:2]:
...    pprint(post['data'])
... 
{u'approved_by': None,
 u'archived': False,
 u'author': u'ThumbtacksArePointy',
 u'author_flair_css_class': u'',
 u'author_flair_text': u'History (B.A.)',
 u'banned_by': None,
 u'clicked': False,
 u'created': 1459304568.0,
 u'created_utc': 1459275768.0,
 u'distinguished': None,
 u'domain': u'self.UCSD',
 u'downs': 0,
 u'edited': False,
 u'from': None,
 u'from_id': None,
 u'from_kind': None,
 u'gilded': 0,
 u'hidden': False,
 u'hide_score': False,
 u'id': u'4cgr1w',
 u'is_self': True,
 u'likes': None,
 u'link_flair_css_class': None,
 u'link_flair_text': None,
 u'locked': False,
 u'media': None,
 u'media_embed': {},
 u'mod_reports': [],
 u'name': u't3_4cgr1w',
 u'num_comments': 305,
 u'num_reports': None,
 u'over_18': False,
 u'permalink': u'/r/UCSD/comments/4cgr1w/new_student_qa_2016/',
 u'quarantine': False,
 u'removal_reason': None,
 u'report_reasons': None,
 u'saved': False,
 u'score': 49,
 u'secure_media': None,
 u'secure_media_embed': {},
 u'selftext': u'I\'m basically just copying this directly from last year\'s Q&amp;A, but I don\'t think many things have changed. (so thank /u/inconditus for this, because they wrote most of it)\n\nSo, you got into UCSD, congratulations! It\'s a great school! But you have questions, most of which the administration can\'t help you with. Come ask us! I\'m rolling over a lot of info from the [2014 edition](http://www.reddit.com/r/UCSD/comments/21uxq7/new_student_qa_2014_edition/) and [2013 edition](http://www.reddit.com/r/UCSD/comments/1c187y/official_new_student_qa_2013/) and [2015 edition](http://www.reddit.com/r/UCSD/comments/32p9ng/new_student_qa_2015/). Thanks to /u/nervette and everyone else for compiling this information.\n\nFirst up: "What are the housing deadlines?" Check out the [housing deadlines here!](http://housing.ucsd.edu/deadlines.asp)\n\nWanna know what all the acronyms and abbreviations we\'re throwing around mean? [There\'s a list for that](http://blink.ucsd.edu/sponsor/blink/AA.html)\n\n"What are the major differences between the colleges?/I got into Miur, what does that even mean?" There are 2 things: The housing units for each college are separate. [Here\'s a map](http://maps.ucsd.edu/mapping/viewer/default.htm) and they all have separate general ed requirements. check it out:  \n[ERC gen eds.](http://roosevelt.ucsd.edu/academics/gen-ed/index.html)- [Marshall gen eds.](https://marshall.ucsd.edu/academics/general-education-requirements.html)- [Muir gen eds.](http://muir.ucsd.edu/academics/degree_reqs.html)- [Revelle gen eds.](http://revelle.ucsd.edu/academics/general-education/index.html)- [Warren gen eds.](http://warren.ucsd.edu/academics/advising/acad-req.html)- [6th gen eds.](http://www.sixth.ucsd.edu/advising/requirements/index.html)\n\n"Which of my AP\'s will give me credit towards what?" I have no idea, look it up on this handy [AP credit chart](http://www.ucsd.edu/catalog/pdf/APC-chart.pdf). Also, check out the [International Baccalaureate (IB) chart]( http://www.ucsd.edu/catalog/pdf/IBC-chart.pdf).\n\nTake a look at the list of UCSD\'s [Student Organizations](http://tonga.ucsd.edu/studentorgregistration/RdOnlyList.aspx) if you\'re interested in getting involved. Here\'s the [Greek website](http://www.tritongreeks.org/) if you\'re into that, too.\n\nWanna know how many units you can transfer? According to the UCSD catalog: "The university will award graduation credit for up to seventy semester (105 quarter) units of transferable course work from a community college. Courses in excess of seventy semester units will receive subject credit and may be used to satisfy university subject requirements."\n\nThe MARSHALL list of approved classes for the Significant Writing Course requirement is [here](http://marshall.ucsd.edu/pdfs/Sig_Writing.pdf)\n\n/u/iGiveProTips takes you on an [epic tour](http://www.reddit.com/r/UCSD/comments/1c187y/official_new_student_qa_2013/c9gn7ih) of campus, complete with bathroom ratings.\n\n /u/delicious_truffles kindly made a thread for entering CS:BioInfo in 2012/2011. If that is your intended major, [check it out.](http://www.reddit.com/r/UCSD/comments/jra8a/incoming_freshman_with_questions/)\n\nOn a waitlist? Remember the Adam Powers Rule of Waitists, for any given class, around 10% of those enrolled with drop it. So you\'re #20 on the waitlist for 500 person class? You\'ll probably get in. The cravats being: if the class is super easy and popular (or Magagna), or it is a class required for an impacted major, then the drop rate goes down. Otherwise, be patient, have a back up, but have faith.\n\nIf you want fancy flair, on the sidebar under the subscribe button, check the show my flair, then hit edit and select your intended major! There is even an undeclared, for those who don\'t know yet.\n\nI\'ll be keeping an eye on this until the start of Fall Quarter, as will several others. \n\n**ALSO, GUYS, READ THIS THING:** [**SCHEDULES PSA**](http://www.reddit.com/r/UCSD/comments/1jh8hz/psa_for_freshmen_and_new_transfers_regarding)  I am serious. I know it\'s a wall of text, and I know you are in college now and know everything, but remember this is the quarter system. You only get 10 weeks before finals. Don\'t burn out. Seriously, this is super important.\n\n# Ask questions below!',
 u'selftext_html': u'&lt;!-- SC_OFF --&gt;&lt;div class="md"&gt;&lt;p&gt;I&amp;#39;m basically just copying this directly from last year&amp;#39;s Q&amp;amp;A, but I don&amp;#39;t think many things have changed. (so thank &lt;a href="/u/inconditus"&gt;/u/inconditus&lt;/a&gt; for this, because they wrote most of it)&lt;/p&gt;\n\n&lt;p&gt;So, you got into UCSD, congratulations! It&amp;#39;s a great school! But you have questions, most of which the administration can&amp;#39;t help you with. Come ask us! I&amp;#39;m rolling over a lot of info from the &lt;a href="http://www.reddit.com/r/UCSD/comments/21uxq7/new_student_qa_2014_edition/"&gt;2014 edition&lt;/a&gt; and &lt;a href="http://www.reddit.com/r/UCSD/comments/1c187y/official_new_student_qa_2013/"&gt;2013 edition&lt;/a&gt; and &lt;a href="http://www.reddit.com/r/UCSD/comments/32p9ng/new_student_qa_2015/"&gt;2015 edition&lt;/a&gt;. Thanks to &lt;a href="/u/nervette"&gt;/u/nervette&lt;/a&gt; and everyone else for compiling this information.&lt;/p&gt;\n\n&lt;p&gt;First up: &amp;quot;What are the housing deadlines?&amp;quot; Check out the &lt;a href="http://housing.ucsd.edu/deadlines.asp"&gt;housing deadlines here!&lt;/a&gt;&lt;/p&gt;\n\n&lt;p&gt;Wanna know what all the acronyms and abbreviations we&amp;#39;re throwing around mean? &lt;a href="http://blink.ucsd.edu/sponsor/blink/AA.html"&gt;There&amp;#39;s a list for that&lt;/a&gt;&lt;/p&gt;\n\n&lt;p&gt;&amp;quot;What are the major differences between the colleges?/I got into Miur, what does that even mean?&amp;quot; There are 2 things: The housing units for each college are separate. &lt;a href="http://maps.ucsd.edu/mapping/viewer/default.htm"&gt;Here&amp;#39;s a map&lt;/a&gt; and they all have separate general ed requirements. check it out:&lt;br/&gt;\n&lt;a href="http://roosevelt.ucsd.edu/academics/gen-ed/index.html"&gt;ERC gen eds.&lt;/a&gt;- &lt;a href="https://marshall.ucsd.edu/academics/general-education-requirements.html"&gt;Marshall gen eds.&lt;/a&gt;- &lt;a href="http://muir.ucsd.edu/academics/degree_reqs.html"&gt;Muir gen eds.&lt;/a&gt;- &lt;a href="http://revelle.ucsd.edu/academics/general-education/index.html"&gt;Revelle gen eds.&lt;/a&gt;- &lt;a href="http://warren.ucsd.edu/academics/advising/acad-req.html"&gt;Warren gen eds.&lt;/a&gt;- &lt;a href="http://www.sixth.ucsd.edu/advising/requirements/index.html"&gt;6th gen eds.&lt;/a&gt;&lt;/p&gt;\n\n&lt;p&gt;&amp;quot;Which of my AP&amp;#39;s will give me credit towards what?&amp;quot; I have no idea, look it up on this handy &lt;a href="http://www.ucsd.edu/catalog/pdf/APC-chart.pdf"&gt;AP credit chart&lt;/a&gt;. Also, check out the &lt;a href="http://www.ucsd.edu/catalog/pdf/IBC-chart.pdf"&gt;International Baccalaureate (IB) chart&lt;/a&gt;.&lt;/p&gt;\n\n&lt;p&gt;Take a look at the list of UCSD&amp;#39;s &lt;a href="http://tonga.ucsd.edu/studentorgregistration/RdOnlyList.aspx"&gt;Student Organizations&lt;/a&gt; if you&amp;#39;re interested in getting involved. Here&amp;#39;s the &lt;a href="http://www.tritongreeks.org/"&gt;Greek website&lt;/a&gt; if you&amp;#39;re into that, too.&lt;/p&gt;\n\n&lt;p&gt;Wanna know how many units you can transfer? According to the UCSD catalog: &amp;quot;The university will award graduation credit for up to seventy semester (105 quarter) units of transferable course work from a community college. Courses in excess of seventy semester units will receive subject credit and may be used to satisfy university subject requirements.&amp;quot;&lt;/p&gt;\n\n&lt;p&gt;The MARSHALL list of approved classes for the Significant Writing Course requirement is &lt;a href="http://marshall.ucsd.edu/pdfs/Sig_Writing.pdf"&gt;here&lt;/a&gt;&lt;/p&gt;\n\n&lt;p&gt;&lt;a href="/u/iGiveProTips"&gt;/u/iGiveProTips&lt;/a&gt; takes you on an &lt;a href="http://www.reddit.com/r/UCSD/comments/1c187y/official_new_student_qa_2013/c9gn7ih"&gt;epic tour&lt;/a&gt; of campus, complete with bathroom ratings.&lt;/p&gt;\n\n&lt;p&gt;&lt;a href="/u/delicious_truffles"&gt;/u/delicious_truffles&lt;/a&gt; kindly made a thread for entering CS:BioInfo in 2012/2011. If that is your intended major, &lt;a href="http://www.reddit.com/r/UCSD/comments/jra8a/incoming_freshman_with_questions/"&gt;check it out.&lt;/a&gt;&lt;/p&gt;\n\n&lt;p&gt;On a waitlist? Remember the Adam Powers Rule of Waitists, for any given class, around 10% of those enrolled with drop it. So you&amp;#39;re #20 on the waitlist for 500 person class? You&amp;#39;ll probably get in. The cravats being: if the class is super easy and popular (or Magagna), or it is a class required for an impacted major, then the drop rate goes down. Otherwise, be patient, have a back up, but have faith.&lt;/p&gt;\n\n&lt;p&gt;If you want fancy flair, on the sidebar under the subscribe button, check the show my flair, then hit edit and select your intended major! There is even an undeclared, for those who don&amp;#39;t know yet.&lt;/p&gt;\n\n&lt;p&gt;I&amp;#39;ll be keeping an eye on this until the start of Fall Quarter, as will several others. &lt;/p&gt;\n\n&lt;p&gt;&lt;strong&gt;ALSO, GUYS, READ THIS THING:&lt;/strong&gt; &lt;a href="http://www.reddit.com/r/UCSD/comments/1jh8hz/psa_for_freshmen_and_new_transfers_regarding"&gt;&lt;strong&gt;SCHEDULES PSA&lt;/strong&gt;&lt;/a&gt;  I am serious. I know it&amp;#39;s a wall of text, and I know you are in college now and know everything, but remember this is the quarter system. You only get 10 weeks before finals. Don&amp;#39;t burn out. Seriously, this is super important.&lt;/p&gt;\n\n&lt;h1&gt;Ask questions below!&lt;/h1&gt;\n&lt;/div&gt;&lt;!-- SC_ON --&gt;',
 u'stickied': True,
 u'subreddit': u'UCSD',
 u'subreddit_id': u't5_2r6sq',
 u'suggested_sort': u'new',
 u'thumbnail': u'self',
 u'title': u'New Student Q&amp;A 2016',
 u'ups': 49,
 u'url': u'https://www.reddit.com/r/UCSD/comments/4cgr1w/new_student_qa_2016/',
 u'user_reports': [],
 u'visited': False}
{u'approved_by': None,
 u'archived': False,
 u'author': u'brianbsantacruz',
 u'author_flair_css_class': u'',
 u'author_flair_text': u"Physics, B.S., Class of '09",
 u'banned_by': None,
 u'clicked': False,
 u'created': 1470800155.0,
 u'created_utc': 1470771355.0,
 u'distinguished': None,
 u'domain': u'self.UCSD',
 u'downs': 0,
 u'edited': False,
 u'from': None,
 u'from_id': None,
 u'from_kind': None,
 u'gilded': 0,
 u'hidden': False,
 u'hide_score': False,
 u'id': u'4wy1h0',
 u'is_self': True,
 u'likes': None,
 u'link_flair_css_class': None,
 u'link_flair_text': None,
 u'locked': False,
 u'media': None,
 u'media_embed': {},
 u'mod_reports': [],
 u'name': u't3_4wy1h0',
 u'num_comments': 0,
 u'num_reports': None,
 u'over_18': False,
 u'permalink': u'/r/UCSD/comments/4wy1h0/new_student_summer_send_offs_2016/',
 u'post_hint': u'self',
 u'preview': {u'images': [{u'id': u'96Il-V7y39f3oeycSCxbORTao68fW7iO2bdqfw1hf9U',
                           u'resolutions': [{u'height': 67,
                                             u'url': u'https://i.redditmedia.com/Dx_WGSEo-KhUdL_fUn8AVrOYVScm-RWM3JE-zvuCCCU.jpg?fit=crop&amp;crop=faces%2Centropy&amp;arh=2&amp;w=108&amp;s=6e9ca0065f2a5fa438fa65c73b120579',
                                             u'width': 108},
                                            {u'height': 135,
                                             u'url': u'https://i.redditmedia.com/Dx_WGSEo-KhUdL_fUn8AVrOYVScm-RWM3JE-zvuCCCU.jpg?fit=crop&amp;crop=faces%2Centropy&amp;arh=2&amp;w=216&amp;s=eec349ec9d9cfb06228f19b31038d50e',
                                             u'width': 216},
                                            {u'height': 200,
                                             u'url': u'https://i.redditmedia.com/Dx_WGSEo-KhUdL_fUn8AVrOYVScm-RWM3JE-zvuCCCU.jpg?fit=crop&amp;crop=faces%2Centropy&amp;arh=2&amp;w=320&amp;s=315423e7c4d94e736e291292d4acbbad',
                                             u'width': 320}],
                           u'source': {u'height': 250,
                                       u'url': u'https://i.redditmedia.com/Dx_WGSEo-KhUdL_fUn8AVrOYVScm-RWM3JE-zvuCCCU.jpg?s=a625be5db09930ec008b5682c34c8660',
                                       u'width': 400},
                           u'variants': {}}]},
 u'quarantine': False,
 u'removal_reason': None,
 u'report_reasons': None,
 u'saved': False,
 u'score': 11,
 u'secure_media': None,
 u'secure_media_embed': {},
 u'selftext': u'For those incoming students in California, UCSD Alumni hosts a "Summer Send Off" in several regions every year for incoming students (Freshmen and Transfers). Check out one of the events happening near you. They\'re a great way to meet alumni, make connections for internships and jobs down the road, get advice and all your burning questions answered, and more. The best part is, it\'s totally free!\n\nTo make this event a success, alumni volunteers are needed.  You can sign up to volunteer on the UCSD Alumni website.  Check out the pages below for more information and a location near you: \n\n* Incoming students (and their families), sign up here: http://www.alumni.ucsd.edu/s/1170/landing/index_rot.aspx?sid=1170&amp;gid=1&amp;pgid=7150\n\n* Alumni volunteers, sign up here: http://www.alumni.ucsd.edu/s/1170/landing/index_rot.aspx?sid=1170&amp;gid=1&amp;pgid=7187',
 u'selftext_html': u'&lt;!-- SC_OFF --&gt;&lt;div class="md"&gt;&lt;p&gt;For those incoming students in California, UCSD Alumni hosts a &amp;quot;Summer Send Off&amp;quot; in several regions every year for incoming students (Freshmen and Transfers). Check out one of the events happening near you. They&amp;#39;re a great way to meet alumni, make connections for internships and jobs down the road, get advice and all your burning questions answered, and more. The best part is, it&amp;#39;s totally free!&lt;/p&gt;\n\n&lt;p&gt;To make this event a success, alumni volunteers are needed.  You can sign up to volunteer on the UCSD Alumni website.  Check out the pages below for more information and a location near you: &lt;/p&gt;\n\n&lt;ul&gt;\n&lt;li&gt;&lt;p&gt;Incoming students (and their families), sign up here: &lt;a href="http://www.alumni.ucsd.edu/s/1170/landing/index_rot.aspx?sid=1170&amp;amp;gid=1&amp;amp;pgid=7150"&gt;http://www.alumni.ucsd.edu/s/1170/landing/index_rot.aspx?sid=1170&amp;amp;gid=1&amp;amp;pgid=7150&lt;/a&gt;&lt;/p&gt;&lt;/li&gt;\n&lt;li&gt;&lt;p&gt;Alumni volunteers, sign up here: &lt;a href="http://www.alumni.ucsd.edu/s/1170/landing/index_rot.aspx?sid=1170&amp;amp;gid=1&amp;amp;pgid=7187"&gt;http://www.alumni.ucsd.edu/s/1170/landing/index_rot.aspx?sid=1170&amp;amp;gid=1&amp;amp;pgid=7187&lt;/a&gt;&lt;/p&gt;&lt;/li&gt;\n&lt;/ul&gt;\n&lt;/div&gt;&lt;!-- SC_ON --&gt;',
 u'stickied': True,
 u'subreddit': u'UCSD',
 u'subreddit_id': u't5_2r6sq',
 u'suggested_sort': None,
 u'thumbnail': u'self',
 u'title': u'New Student Summer Send Offs 2016',
 u'ups': 11,
 u'url': u'https://www.reddit.com/r/UCSD/comments/4wy1h0/new_student_summer_send_offs_2016/',
 u'user_reports': [],
 u'visited': False}
>>> 
```

# For further study

A more sophisticated way of accessing JSON data with Python is to use the Pandas data science library.

There is a tutorial here: <https://www.dataquest.io/blog/python-json-tutorial>
