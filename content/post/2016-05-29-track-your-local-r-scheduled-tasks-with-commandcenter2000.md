---
title: Track your local R scheduled tasks with CommandCenter2000!!!
author: Amit
type: post
date: 2016-05-29T17:32:02+00:00
url: /track-your-local-r-scheduled-tasks-with-commandcenter2000/
categories:
  - Data
  - R
  - Tutorials
tags:
  - Command center
  - Run
  - Schedule
  - Script

---
There are many ways to automate your scripts running, for example using RScript, or [in-R itself][1] (and now even as an [add-in][2] for RStudio) ([check all here][3]). But after a while, it can get a bit overwhelming to track tasks and ensure they are firing as planned. In order to address this, I have developed some futuristic advanced tech that lets us do that. I hereby present to you: the CommandCenter2000!!! Yes, it&#8217;s Y2K compliant! This is what it looks like:

&nbsp;

[<img class="alignnone size-medium wp-image-658" src="https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/05/Capture.png?resize=300%2C166" alt="Capture" width="300" height="166" srcset="https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/05/Capture.png?resize=300%2C166 300w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/05/Capture.png?w=471 471w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" />][4]

&nbsp;

It has the following features:

  * It&#8217;ll tell you when the script ran last
  * whether it was successful or not (green/red light)
  * and will help you rerun failed scripts in 2 ways.

## How to make your own:

[<img class="alignnone size-medium wp-image-674" src="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/05/diagram-1.png?resize=300%2C230" alt="diagram" width="300" height="230" srcset="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/05/diagram-1.png?resize=300%2C230 300w, https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/05/diagram-1.png?resize=768%2C588 768w, https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/05/diagram-1.png?w=847 847w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" />][5]

(Follow the steps in the schematic above: red for setup, and yellow to run it. These are explained below)

  1. Setup the folders where there are running tasks. Concretely, inside the working folder for each script, you need a .bat file that will run that specific script. Within the bat file<span style="color: #ff0000;">*</span>, the code will look like this for example: <p style="padding-left: 90px;">
      <code>@echo off&lt;br />
"C:\Program Files\R\R-3.2.2\bin\x64\R.exe" --vanilla --slave CMD BATCH "D:\Project X\analyzer.R"&lt;br />
</code>
    </p>

  2. OK, now you need to schedule the task in Windows (I like scheduling it myself so that I can set some specific requirements&#8230; in particular, I want tasks to fire only if connected to certain wifi). Don&#8217;t know how to do this? [There are many ways to automate your scripts running, for example using RScript, or [in-R itself][1] (and now even as an [add-in][2] for RStudio) ([check all here][3]). But after a while, it can get a bit overwhelming to track tasks and ensure they are firing as planned. In order to address this, I have developed some futuristic advanced tech that lets us do that. I hereby present to you: the CommandCenter2000!!! Yes, it&#8217;s Y2K compliant! This is what it looks like:

&nbsp;

[<img class="alignnone size-medium wp-image-658" src="https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/05/Capture.png?resize=300%2C166" alt="Capture" width="300" height="166" srcset="https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/05/Capture.png?resize=300%2C166 300w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/05/Capture.png?w=471 471w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" />][4]

&nbsp;

It has the following features:

  * It&#8217;ll tell you when the script ran last
  * whether it was successful or not (green/red light)
  * and will help you rerun failed scripts in 2 ways.

## How to make your own:

[<img class="alignnone size-medium wp-image-674" src="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/05/diagram-1.png?resize=300%2C230" alt="diagram" width="300" height="230" srcset="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/05/diagram-1.png?resize=300%2C230 300w, https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/05/diagram-1.png?resize=768%2C588 768w, https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/05/diagram-1.png?w=847 847w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" />][5]

(Follow the steps in the schematic above: red for setup, and yellow to run it. These are explained below)

  1. Setup the folders where there are running tasks. Concretely, inside the working folder for each script, you need a .bat file that will run that specific script. Within the bat file<span style="color: #ff0000;">*</span>, the code will look like this for example: <p style="padding-left: 90px;">
      <code>@echo off&lt;br />
"C:\Program Files\R\R-3.2.2\bin\x64\R.exe" --vanilla --slave CMD BATCH "D:\Project X\analyzer.R"&lt;br />
</code>
    </p>

  2. OK, now you need to schedule the task in Windows (I like scheduling it myself so that I can set some specific requirements&#8230; in particular, I want tasks to fire only if connected to certain wifi). Don&#8217;t know how to do this?][6] (that&#8217;s how I learned)!
  3. OK, now tasks will be firing off! Now you need to get the command Center script from my [github account][7]. Go <!-- iframe plugin v.4.3 wordpress.org/plugins/iframe/ --> it now! 
    
      1. This contains: 
          1. the CommandCenter R script
          2. a .bat file that will run the CommandCenter2000!!! itself. I recommend creating a shortcut to this bat file on your desktop or whatever. That way you can run it whenever
          3. the html file that reports the status of each task.
          4. ignore the rest of the stuff
      2. Ok, now you have a local CommandCenter2000!!!. 
          1. Set up the WORKING DIRECTORY to wherever you installed the folder.
          2. Now, for each script you&#8217;d like to track in the CommandCenter2000!!!, add a reference to that script in the main CommandCenter2000!!! script. By &#8220;reference&#8221;, I mean: 
              1. Copy the block of code that looks like it should be copied. (hint, there&#8217;s START and END comments). Within each: 
                  1. Give that script a human name (this is what will be displayed)
                  2. Specify the path and name of the R file (remember the whole &#8220;/&#8221; vs &#8220;\&#8221; debacle for windows paths)
                  3. Specify the path and name of  the .bat file
              2. That&#8217;s it! Rinse and repeat for every script that you would like on your CommandCenter2000!!!
  4. OK, setup is done. Now, whenever you want to check the status of scripts, you can just run your command center. Of course, you _could_ run the CommandCenter2000!!! itself on a schedule&#8230; but putting something on a schedule to check whether other things are running on schedule correctly is a bit&#8230;&#8230; mind-bending. Careful you don&#8217;t [break reality.][8]
  5. Everytime you click it, you&#8217;ll get the html file coming up shown above. In detail: 
      1. &#8220;**thing**&#8220;: is just the name of the analysis
      2. &#8220;**lastRun**&#8220;: is how long ago the analysis ran (in days&#8230; although obviously this is configurable).
      3. &#8220;**status**&#8220;: (this is the last column) has a red or green light to indicate whether the script ran successfully or not. If it didn&#8217;t, the red light will have  a mouseover effect whereby you&#8217;ll be able to tell what the error was&#8230;. which looks like this: [<img class="alignnone size-medium wp-image-666" src="https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/05/dd.png?resize=300%2C29" alt="dd" width="300" height="29" srcset="https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/05/dd.png?resize=300%2C29 300w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/05/dd.png?resize=768%2C74 768w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/05/dd.png?resize=1024%2C98 1024w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/05/dd.png?w=1076 1076w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" />][9]This mouseover effect will help you debug&#8230; using the following two options
      4. &#8220;**SomethingWrong**&#8220;: provides a link to the R file, <span style="text-decoration: underline;">in case the script failed because your R script is messed up</span>. Don&#8217;t click the link, but right click and &#8220;copy link&#8221;, then open it from R (sorry for roundabout way, but unfortunately it&#8217;s very difficult to launch a local file from HTML for security)
      5. &#8220;**runLink**: provides a link to the bat file that will run the script (more on this later). Use this<span style="text-decoration: underline;"> if  the script failed but you think the R script is correct and just needs to rerun</span> (for example if the network crapped out), just click, download the bat file and run it&#8230; everything will rerun automatically.

&nbsp;

So clearly, this is a very rough first-pass attempt to keep track of scheduled tasks. If you&#8217;d like to collaborate, I&#8217;d love to evaluate some pull-requests.

&nbsp;

&nbsp;

<span style="color: #ff0000;">*WARNING: This approach uses .bat files, which could damage your computer or corrupt your data. Be VERY CAREFUL, and don&#8217;t trust anybody else&#8217;s bat files without first examining them in a text editor.</span>

 [1]: http://www.r-bloggers.com/taskscheduler-r-package-to-schedule-r-scripts-with-the-windows-task-manager/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+RBloggers+%28R+bloggers%29
 [2]: http://www.bnosac.be/index.php/blog/57-new-rstudio-add-in-to-schedule-r-scripts
 [3]: http://www.r-bloggers.com/?s=schedule
 [4]: https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/05/Capture.png
 [5]: https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/05/diagram-1.png
 [6]: https://trinkerrstuff.wordpress.com/2015/02/11/scheduling-r-tasks-via-windows-task-scheduler/
 [7]: https://github.com/datastrategist/CommandCenter
 [8]: https://xkcd.com/1638/
 [9]: https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/05/dd.png