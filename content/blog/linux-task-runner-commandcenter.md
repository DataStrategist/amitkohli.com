---
title: You Don't Need Airflow (And Your Cron Jobs Are Fine)
author: amit
date: 2026-05-24
slug: linux-task-runner-commandcenter
tags:
  - Linux
  - R
  - Data Engineering
  - Workflow
  - Infrastructure
topics:
  - Workflow
  - Data Pipelines
  - Scheduling
draft: true
type: "[[Article]]"
topic: "[[Linux Scheduling]]"
---

You were going to say Airflow, weren't you? And don't get me wrong, it's great, as are all the other tools in this space, but the space between yet another dependency and "just a little bit more than crontab" is really big, especially if you have a small team.

For example, let's say you have a Linux server, a handful of R/Python scripts, and you just need them to run on a schedule without falling over. There are a couple of gotchas, and a couple things you need to monitor in order to keep things going pretty consistently. To accomplish this, you don't need Airflow, you need cron a folder convention, and a bit of smarts!

## The Pattern

You will probably be familiar with the fact that running an R/Python file outputs the results to the console. So a simple pattern like:

```
Rscript my_file.R > my_file.log
```

will capture the outputs of running the file into a log file. 

If you put this in your cron, it'll work fine. You can then set another script that monitors all the log files and looks for the word "error"... this _would_ work a charm... but depending on your file, you might get some nonsense about working directory.

You can get around this by putting the command into a bash file like `my_script.sh`. If you do:

```
cd path/my_files_folder
Rscript my_file.R > my_file.log 2>&1
```

and then put that in the crontab, you solve that problem.  (The `2>&1` bit just stores text or errors to the log file.)

But if you have multiple scripts running on your crontab, you might end up in a place where you have long runs that run over one another. and considering you're running scripts anyway in your crontab, nothing stops the crontab from containing a bit more utility which gives you A BUNCH of more functionality:

```
START=$(date +%s)

# change path to working directory
cd path/my_files_folder

# start your script work here
Rscript my_file.R > my_file.log 2>&1

END=$(date +%s)
DIFF=$(( $END - $START ))
echo "XXX data_uploader $START $DIFF"
```

What this does is store the start and entime of the script, and output the start time and duration to a log file. Now, the simple bit:

```
10 21 * * * /srv/projects/chatbot_content/qc_maker_prod.sh >> /srv/projects/cc/qc_maker_prod.timeRun.txt 2>&1

```
