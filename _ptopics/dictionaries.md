---
topic: "dictionaries"
desc: "Mappings from keys to values"
---

# Python Dictionaries

In Python, we can use a *dictionary* to associate keys with values.

This code creates a simple dictionary called `en_to_es` (short for "English to Español), that
maps the words `one`, `two` and `three` (as Python strings) to their Spanish counterparts (as
Python strings):

```python
en_to_es = { 'one' : 'uno', 'two' : 'dos', 'three' : 'tres' }
```

Once you create a dictionary, you can access the values by looking up their key.
Here, we show trying some Python dictionary code at the interactive Python shell:

```python
>>> en_to_es = { 'one' : 'uno', 'two' : 'dos', 'three' : 'tres' }
>>> en_to_es['one']
'uno'
>>> en_to_es['three']
'tres'
>>> 
```

If a particular key is not in the dictionary, and you try to look it up, you get a 
`KeyError`, like this:

``` python
>>> en_to_es['ten']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'ten'
>>> 
```

# Listing the keys in a dictionary

We can look up the keys in a dictionary by typing `.keys()` after the variable that refers to the dictionary.  For example, see what `en_to_es.keys()` returns in the example below.


We can put `list (   )` around that expression to make sure the result comes back as a Python list.


```
>>> en_to_es = { 'one' : 'uno', 'two' : 'dos', 'three' : 'tres' }
>>> en_to_es.keys()
dict_keys(['three', 'two', 'one'])
>>> list(en_to_es.keys())
```

# Adding new values to a dictionary

Dictionaries are *mutable*, meaning they can be changed.  We can add new key/value pairs to an existing dictionary using assignment staements such as this one:

```
en_to_es['four'] = 'quatro'
en_to_es['five'] = 'cinco'
```

# Handling `KeyError` with `try`/`except`

You can use a so-called `try`/`except` block to write custom code that looks for the
`KeyError` and instead of printing a scary looking error message, does whatever you
would prefer:

Suppose we run this file:

```python
def translate(myDictionary,wordToLookup):
    ''' lookup word.  return NoneType value if word not found '''
    try:
        return myDictionary[wordToLookup]
    except KeyError:
        print "The word ",wordToLookup," was not in the dictionary"
        return


en_to_es = { 'one' : 'uno', 'two' : 'dos', 'three' : 'tres' }
```
    
Then, we can use the function `translate` to do translation with a "nicer" error message.

```
=============== RESTART: /Users/pconrad/Documents/translate.py ===============
>>> en_to_es
{'three': 'tres', 'two': 'dos', 'one': 'uno'}
>>> en_to_es['one']
'uno'
>>> en_to_es['ten']

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    en_to_es['ten']
KeyError: 'ten'
>>> translate(en_to_es,'one')
'uno'
>>> translate(en_to_es,'ten')
The word  ten  was not in the dictionary
>>> 
```

# Dictionaries of Dictionaries

Two letter language codes for various human spoken languages have
been standardized by the International Standards Organization, ISO, and can be looked up
[at this web page](https://www.loc.gov/standards/iso639-2/php/code_list.php))

Here are just a few.   The third column explains why, for example, 
German is `de` and Chinese is `zh`.

|code| Language (in English) | Language (in that language,<br>using latin alphabet)|
|----|-----------------------|-----------------------------------------------------|
|de  | German                | Deutsch |
|en  | English               | English |
|es  | Spanish               | Español  |
|fr  | French                | Français |
|fa  | Persian               | Farsi  |
|zh  | Chinese               | Zhongwen |

We could construct a dictionary of these codes like this:

```python
codeToLanguage = {
  'de' : 'German',
  'en' : 'English',
  'es' : 'Spanish',
  'fr' : 'French',
  'fa' : 'Persian',
  'zh' : 'Chinese',
}
```

If we wanted to translate the number 'one','two','three' into each of these languages, we
could create six different dictionaries, like this:

```python
en_to_de = { 'one' : 'eins', 'two' : 'zwei', 'three' : 'drei' }
en_to_es = { 'one' : 'uno', 'two' : 'dos', 'three' : 'tres' }
en_to_fr = { 'one' : 'un', 'two' : 'deux', 'three' : 'trois' }
# etc ...
```

But there is a better way.  It turns out that the *value* part in a *(key,value)* pair can be any type; not just
a string.   One possibility is that it can, itself, be a dictionary.  

This gives us many ways that we could construct a dictionary to translate `one`,`two`,`three` into various languages.

## Method 1: Use English number as key, then each entry is a dictionary by language:

```
numDict = { 
    'one':   {'de' : 'eins', 'es':'uno',  'fa':'yek', 'fr':'un',    'zh':'yi' },
    'two':   {'de' : 'zwei', 'es':'dos',  'fa':'do',  'fr':'deux',  'zh':'er' },
    'three': {'de' : 'drei', 'es':'tres', 'fa':'seh', 'fr':'trois', 'zh':'san' }
  }
```

In this dictionary, writing `numDict['one']` returns to us another dictionary, where the keys
are the language codes, (`'de'`, `'es'`, `'fr'`, etc.).    For example:


```
>>> numDict['one']
{'fa': 'yek', 'fr': 'un', 'de': 'eins', 'zh': 'yi', 'es': 'uno'}
>>> 
```

Note that in a Dictionary, the keys don't necessary appear in the order that we put them into the dictionary,
and they don't even necessarily appear in *any* particular order.   In technical terms, we say that:

* A python dictionary is an unordered collection of mappings from keys to values.

So, to get `'one'` in a particular language, we can index the dictionary returned by  `numDict['one']` a second
time, with the language that we want.  For example, to get `'one'` in Chinese (`'zh'`), we can use:

```
>>> numDict['one']['zh']
'yi'
>>> 
```

But that's not the only way to do it.

## Method 2: Index by language, then by word

We could also arrange our dictionary like this:

```python
numberLookup = {
    'de' : { 'one' : 'eins', 'two' : 'zwei', 'three': 'drei'  },
    'es' : { 'one' : 'uno',  'two' : 'dos',  'three': 'tres'  },
    'fa' : { 'one' : 'yek',  'two' : 'do',   'three': 'seh'   },
    'fr' : { 'one' : 'un',   'two' : 'deux', 'three': 'trois' },
    'zh' : { 'one' : 'yi',   'two' : 'er',   'three': 'san'   }
}
```    

Now, when we use `numberLookup['es']` for example, we get a dictionary indexed by
the numbers in English, `'one'`, `'two'`, `'three'`.

```python
>>> numberLookup['es']
{'three': 'tres', 'two': 'dos', 'one': 'uno'}
>>> 
```

So, to lookup a particular, number, we add a second index:

```
>>> numberLookup['es']['two']
'dos'
>>> 
```

# Why are dictionaries important?

Dictionaries are one of the most commonly used data structures in "real world" Python programming, because they
correspond very nicely to the way that real world data is often structured.  This includes data from
data bases, websites, etc.

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

That topic is explored on another page: [json](/ptopics/json/)

