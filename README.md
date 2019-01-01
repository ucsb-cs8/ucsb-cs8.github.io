# ucsb-cs8.github.io


Jekyll-based website for course materials for CS8 shared across instructors.

Website: <https://ucsb-cs8.github.io>

The theme currently being used can be find in the jekyll-theme value
in `_config.yml`

The navigation is set by the values in `_data/navigation.yml`

Jekyll status on Travis-CI: [![Build Status](https://travis-ci.org/ucsb-cs8/ucsb-cs8.github.io.svg?branch=master)](https://travis-ci.org/ucsb-cs8/ucsb-cs8.github.io)

* Travis-ci: https://travis-ci.org/ucsb-cs8/ucsb-cs8.github.io
* To add a status image like this in your README.md, see [these instructions](https://docs.travis-ci.com/user/status-images/)


To test locally:
* One time setup:
    * `git clone` the repo
    * Install rvm (the Ruby version manager)
    * Run `./setup.sh` to install correct ruby version, bundler version, and bundle the gems
* From then on, to test the site locally:
    * Run `./jekyll.sh
    * Point browser to localhost:4000


