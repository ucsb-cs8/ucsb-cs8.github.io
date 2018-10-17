---
topic: "Flask Webapps: 06"
desc: "Working with Sessions in Flask"
indent: true
---

{% include flask_webapps_header.html %}

---
topic: "Webapps Intro, Part 5"
desc: "Working with Sessions in Flask"
---

# Sessions in Flask

To do anything remotely interesting with a web application, you must build 
on the concept of a *session*.

A *session* is a place that we can store some information, temporarily, 
while a user navigates from one page to another within our web
application.    

Here is an example of a running application on Heroku that uses sessions:


* [https://github.com/ucsd-cse-spis-2016/spis16-webapps-flask-sessions](https://github.com/ucsd-cse-spis-2016/spis16-webapps-flask-sessions)
* In this lesson we'll go through the code that makes this example work.

## Preliminaries to using Sessions

Before you can use sessions in your flask webapp, you need to do two preliminary things:

1. Set up the right import statement

   Here's the import you need:

   ```python
   from flask import session
   ```
2. Set the value of `app.secret_key`  

   The secret key is used to encrypt our session to avoid something called "session hijacking", which
   is a way that an evildoer can hack into a running web app session and take it over (potentially stealing private data, or creating other mayhem).

   The value of the secret key can be pretty much any string of letters and digits.  More information on the secret key can be found here: [http://flask.pocoo.org/docs/0.10/quickstart/#sessions](http://flask.pocoo.org/docs/0.10/quickstart/#session)

   Set the secret key sometime after the `app = Flask(__name__)` line.

   ```python
   app = Flask(__name__)
   app.secret_key='w98fw9ef8hwe98fhwef'   # This sets the secret key for sessions
   ```

   In this example, the secret key is hard coded right in the Python code that implements
   the web app, which is fine for a simple example, but there are better ways to do it, such as reading the value
   from an environment variable.   We'll discuss how that works when we get to OAuth and databases.

## Setting up a session (or starting over)

To create a new session, we use this code:

```
   session.clear()
```

This is *also* the code we use to destroy a session, since the act of destroying a sessions also, essentially, creates a new session.     

Another way to look at it is this: once you use `from flask import session`, you *always* have a session
in any browser that opens a page on your web app.  It is just a matter of when you press the "reset" button to make a new
one.   

You can actually "just start using" the session object by storing things in it, without doing `session.clear()` first.  But its probably a better idea to be sure that you always start with a clean slate, like erasing the blackboard before you start a new lesson.

## Storing things in a session, and getting them back out

You store things in a session the same way you store them in a Python dictionary (`dict`) object, by key and value:

To store a hard coded value, you could write:

```python
    session['firstName']='Phill'
```

But it is more likely that you'd be storing some information that the user entered into a form:

```python
    session['firstName']=request.form['firstName']
```

Suppose we want to get something out of session that we have stored there.  For instance, suppose  our key is `firstName` and we want to get the value:

* We use `session['firstName']` to get the value.   
* We can also test whether a key is in the session or not with: `if 'firstName' in session:`

We are typically doing that inside the HTML inside one of our templates.  We may want to check whether that value exists or not first.  Here's some code that does that.  This code would be inside one of the `.html` files inside the `templates` folder.  

Note that in a Jinja2 template, we do *not* put a colon (`:`) after the `if 'firstName' in session` test; since this is already inside a set of Jinja2 delimiters, i.e. `{% raw %}{% %}{% endraw %}`, the colon is not needed.


```python
{% raw %}{%{% endraw %} if 'firstName' in session {% raw %}%}{% endraw %} 
   First Name: {% raw %}{{{% endraw %} session['firstName'] {% raw %}}}{% endraw %}<br>
{% raw %}{%{% endraw %} endif {% raw %}%}{% endraw %}
```


## Some things to know about sessions:

* A session is created when the user navigates to some page that has code on the backend (the Python part of our web application) that
    creates the session.
* Each page we visit can then store things into the session, or get things out of the session.
* The session is temporary: if you close the browser, restart the Python code that is running your server, 
    the session object goes away.  (For more permanent storage we typically use a database of some kind; more on that later.)
* Webapps typically offer the user some way (e.g. by clicking a button) to start a new session.   Starting a new session
    discards everything in the current session, and starts from scratch.
* It is typically not possible to have two sessions running at a time in the same browser.  If you want to test with multiple
    sessions, you can use multiple browsers, or the "incognito"/"private-browsing" feature that most browsers offer.

## The concept of a session is not specific to Flask or Python

You'll find the concept of a session in pretty much every web framework, regardless of whether you are using Python 
for your web "backend" language, or something else such as Java, PHP, Ruby on Rails, Node (server-side JavaScript), etc.

{% include flask_webapps_table_of_contents.html %}
