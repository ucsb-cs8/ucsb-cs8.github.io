#!/usr/bin/env bash


[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"
rvm use 2.5.1 --install --binary --fuzzy
bundle install --jobs=3 --retry=3
bundle exec jekyll serve $@
