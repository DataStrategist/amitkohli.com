---
title: Best way to set up an R task in linux
author: Amit
date: '2019-01-23'
slug: best-way-to-set-up-an-r-task-in-linux
categories:
  - Data
tags:
  - linux
  - task
description: ''
---

Steps:

 1. Make the file locally. Make sure it does what you want
 2. commit it and push it up to github
 3. clone the repo into the server

``` {bash}
git clone YOURREPONAME
```
 4. Test that the code works on the server! You might need to install new packages, so do that
 5. Create a .sh file that contains the working directory and aims at a log file
 6. chmod the entire folder
 7. Commit it and push it back up to the github
 8. Insert the .sh in the crontab
 9. Insert a check in the Command Center that checks the log
 10. Done!