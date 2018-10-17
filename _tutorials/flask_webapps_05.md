---
topic: "Flask Webapps: 05"
desc: "Deploying an existing Flask App on Heroku"
indent: true
---

{% include flask_webapps_header.html %}


# Deploying an existing Flask App on Heroku

If you already have a Flask app running locally by just running it in IDLE, or at the command line (e.g. python hello.py), and you want to convert it to run on Heroku, you need to do three things.  Each is very simple.

* It needs to be in a git repository.
* You need a Procfile—this is usually just one line of code (see below.)
* You need a requirements.txt file.  This is generated automatically with one unix command (see below.)
* You use the command heroku create to set up a remote repository on heroku where you can deploy your application
* You use git push heroku master to deploy your application.
* You can see your application on the web, or use heroku logs to see the logs (if there are errors.)


Let's try this now with the webapp you already created.  For example, if you
created the webapp for the unit conversions, you might try deploying that on Heroku by
following these instructions.

To deploy on Heroku, we need to create two extra files.

First, We need a file called `Procfile` in our git repo.  This file tells Heroku what to do with our github repo when we push it to github.  It should contain the following:

```
web: gunicorn hello:app --log-file=-
```

The part of this line that reads  `hello:app` assumes that the main python code for your web app is in `hello.py`, and that the variable `app` is the one that appears in the line of code `app = Flask(__name__)`.

If that is not the case, you may need to adjust either `hello` or `app `as needed.

Now that we have that file, you will want to do these commands to commit this file to our github repo.

```
git add Procfile
git commit -m "Added Procfile needed by Heroku"
git push origin master
```

We also need a file called  `requirements.txt` which is a list of the Python modules that are needed for our Heroku flask application.   

This file will list all of the Python modules that we may have installed using 
`pip install blah`, including `flask`, and anything else that `flask` might have required.

* Note: that command might be `pip3 install blah` if you routinely use `python3` instead of
`python`. 
* On shared systems such as CSIL, it may be `pip3 install --user blah`

Note that before you do the next step, you should do the following `pip install` command if you haven't already.  While this next line isn't necessarily needed for running Flask applications locally, it is needed for Heroku.

```
pip install --user gunicorn
```

We  <span style="font-weight:bold; font-size: 110%; color:red;">can</span> create the file `requirements.txt` with this command:

```
pip freeze > requirements.txt
```

 <span style="font-weight:bold; font-size: 110%; color:red;">But we won't do that! Because</span> "pip freeze" outputs the installed packages in the requirements format; however, over the course of SPIS, we have installed **many** packages, and the list is very *very* long; also heroku does not like some of the packages.

**Instead**, go ahead and create a file called "requirements.txt" `(hint: you can do this by typing "idle requirements.txt" into the command line)`, and paste this into the file:

```
Flask==0.10.1
itsdangerous==0.24
Jinja2==2.8
MarkupSafe==0.23
Werkzeug==0.10.4
wheel==0.24.0
gunicorn==19.3.0
```

We now have a list of packages our program needs to run. 

Go ahead and save that file, and now lets push that to github as well:

```
git add requirements.txt
git commit -m "Added list of Python modules needed by Heroku"
git push origin master
```

For the next step, you'll need the Heroku Command Line Interface (CLI) installed on the
machine where you are working. 
* If you are working on CSIL, the Heroku CLI is already installed;
it's the `heroku` command.  
* If you are working on your own laptop or desktop and haven't already installed the "heroku command line" for your machine,
do that now.   Instructions are here: [Installing Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

Assuming you have the `heroku` CLI installed, at a bash shell prompt you should be able to type
`heroku login`.

Now type `heroku create` and notice the name of the application created.

* It will take the form word-word-number, e.g. flying-tomato-4321

The next step is to type:

```
git push heroku master
```

After doing `git push heroku master`, you'll probably see lots of output, showing that your webapp is now running on Heroku.

* To see your app, visit https://word-word-number.herokuapp.com, 
* e.g. https://flying-tomato-4321.herokuapp.com

If there are errors, check them by typing `heroku logs`

Try entering your unique URL for you webapp on your phone or your laptop! You should be able to convert temperatures and miles to kilometers from anywhere now!

## Brief recap on order of commands

We just added another step in our software development. Just as a reminder, this is the order you should follow as you make changes to your programs:

1. git add filename
2. git commit -m "Meaningful and informative message"
3. git push origin master
4. git push heroku master

# A side note about that "itsdangerous" thing 


When I first saw that name show up in the modules we were downloading, I was a little taken aback.
If you are worried about having something called "itsdangerous" in your account, this paragraph is to reassure you that its not dangerous. 

I read the documentation for the itsdangerous module and realized that that the only thing dangerous here was the name.   The name refers to the fact that sometimes data has to be passed from a "trusted environment" to an "untrusted environment" or vice-versa, and when that happens, you want to "sign" the data—that is, do some cryptography with it—to ensure that it isn't modified enroute.  There isn't anything "dangerous" about the software itself.  On the contrary—not using it would be dangerous.


# The next lesson

The next lesson is [Web Apps Intro (part 6)](/tutorials/flask_webapps_06/)

{% include flask_webapps_table_of_contents.html %}
