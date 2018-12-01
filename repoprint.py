#!/usr/bin/env python

from github3 import login
gh = login('quioguer', password='AchievementFirst')


user_repos = gh.repositories_by('quioguer')

for repo in user_repos:
    print repo

