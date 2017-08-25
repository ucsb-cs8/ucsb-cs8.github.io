---
topic: "Anaconda"
desc: "An alternative Python installation that incorporates many features for scientific computing"
---

The default suggested way for CMPSC 8 students to install Python on their computers is by using the Downloads at <https://python.org>

An alternative is Anaconda.

I'm not suggesting you use Anaconda.

But, if you already have on your machine, here are some things you may need to know:

# You may need to use `conda install blah` instead of `pip3 install blah`

Some labs may ask you to do something like:

```
pip3 install pytest
```

or 

```
pip3 install flask
```

If you are using the versions of `idle3` that came with Anaconda, then `pip3` might not work for you.

Try instead, for example:

```
conda install pytest
```

