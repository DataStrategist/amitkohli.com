---
title: Setting up twitter streamR Service on an Ubuntu server
author: Amit
type: post
date: 2017-11-07T15:56:06+00:00
url: /setting-up-twitter-streamr-service-on-an-ubuntu-server/
categories:
  - R
  - Tutorials
tags:
  - Linux
  - Server
  - Service
  - Twitter

---
I am working on a **super-secret** project for which I am harvesting a highly confidential source of data: twitter 🙂 The idea is to gather a small amount of twitter data, but for a long time&#8230; maybe a year. I tried to use the package [TwitteR][1], but it can only  grab up to a week of tweets&#8230; it&#8217;s not really good for a set-it-and-forget-it ongoing capture since it requires user-based authentication, which means (I guess) that a machine can’t authenticate for it. Tangibly this means a human needs to start the process every time. So I could run the script weekly, but of course there&#8217;s days you miss, or run at different times&#8230; plus it&#8217;s just plain annoying&#8230;

<blockquote class="twitter-tweet" data-lang="en">
  <p dir="ltr" lang="en">
    does no <a href="https://twitter.com/hashtag/rstats?src=hash&ref_src=twsrc%5Etfw">#rstats</a> package useTwitter oauth 2.0? I can&#8217;t believe it&#8230; this means that automated tweet-scrapers in R aren&#8217;t possible? <a href="https://t.co/eq9dnrbB6L">pic.twitter.com/eq9dnrbB6L</a>
  </p>
  
  <p>
    — amit (@VizMonkey) <a href="https://twitter.com/VizMonkey/status/895191870208434177?ref_src=twsrc%5Etfw">August 9, 2017</a>
  </p>
</blockquote>



And then I remembered about [streamR][2], which allows exactly for this ongoing scraping. This blog documents my experience this up on my server, using a linux service.

## Let&#8217;s Go!

(Small meta-note: I&#8217;m experimenting with a new blogging style: showing more of my errors and my iterative approach to solving problems in order to counter the perception of the perfect analyst&#8230; something a bunch of people have been talking about recently. I was exposed to it by <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="https://twitter.com/JennyBryan" data-user-id="2167059661"><span class="username u-dir" dir="ltr" data-aria-label-part="">@<b>JennyBryan</b></span></a>  and <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="https://twitter.com/hspter" data-user-id="24228154"><span class="username u-dir" dir="ltr" data-aria-label-part="">@<b>hspter</b></span></a> during EARL London, and it&#8217;s really got me thinking. Anyway, I do realize that it makes for a messier read full of tangents and dead ends. Love it? Hate it? Please let me know what you think in the comments!)

(metanote 2: The linux bash scripts are available in [their own github repo][3])

So if you don’t have a linux server of your own, follow [Dean Atalli’s excellent guide][4] to set one up on [Digital Ocean][5]… it’s cheap and totally worth it. Obviously, you&#8217;ll need to install `streamR`, also `ROauth`. I use other packages in the scripts here, up to you to do it exactly how I do it or not. Also&#8230; remember when you install R-Packages on Ubuntu, you have to do it as the superuser in linux, not from R (otherwise that package won&#8217;t be available for any other user (like shiny). If you don&#8217;t know what I&#8217;m talking about then you didn&#8217;t read Dean Atalli&#8217;s guide like I said above&#8230; why are you still here?). Actually, it&#8217;s so annoying to have to remember how to correctly install R packages on linux, that I created a little utility for it. save the following into a file called &#8220;Rinstaller.sh&#8221;:

&nbsp;

<pre class="EnlighterJSRAW" data-enlighter-language="shell">!/bin/bash
# Ask the user what package to install
echo what package should I grab?
read varname

echo I assume you mean CRAN, but to use github type "g"
read source

if [ "$source" = "g" ]; then
        echo --------------------------------
        echo Installing $varname from GitHub
        sudo su - -c \\"R -e \"devtools::install_github('$varname')\"\\"
else
        echo --------------------------------
        echo Grabbin $varname from CRAN
        sudo su - -c \\"R -e \"install.packages('$varname', repos='http://cran.rstudio.com/')\"\\"
fi

</pre>

this function will accept an input (the package name) and then will ask if to install from CRON or from github. From github, obviously you need to supply the user account and package name. There! Now we don&#8217;t need to remember anything anymore! 🙂 Oh, make sure you `chmod 777 Rinstaller.sh` (which lets anyone execute the file) and then to run it: `./Rinstaller.sh`

&nbsp;

Anyway, I messed around with streamR for a while and figured out how I wanted to structure the files. I think I want 3 files&#8230; one to authenticate, one to capture tweets, and the third to do the supersecret analysis. Here they are:

&nbsp;

#### Authenticator

<pre class="EnlighterJSRAW">## Auth
library(ROAuth)
requestURL &lt;- "https://api.twitter.com/oauth/request_token"
accessURL &lt;- "https://api.twitter.com/oauth/access_token"
authURL &lt;- "https://api.twitter.com/oauth/authorize"
consumerKey &lt;- "myKey"
consumerSecret &lt;- "mySecret"

my_oauth &lt;- OAuthFactory$new(consumerKey = consumerKey, consumerSecret = consumerSecret, 
                             requestURL = requestURL, accessURL = accessURL, authURL = authURL)
my_oauth$handshake(cainfo = system.file("CurlSSL", "cacert.pem", package = "RCurl"))

save(my_oauth, file = "my_oauth.Rdata")</pre>

So we use this file to connect to the Twitter service. You will need to set yourself up with an API&#8230; it&#8217;s fairly painless. [Go do that here][6] and select &#8220;Create new app&#8221;.

(small caveat: make sure the `my_oauth` file is saved in the working directory. You can make sure of it by creating a Project for these three files&#8230; actually, working w/ working directories in a scripted setting is a pain&#8230; more on this later).

#### Tweet-Getter

<pre class="EnlighterJSRAW" data-enlighter-language="null">library(streamR)
library(here)
## Get
load("/srv/shiny-server/SecretFolder/my_oauth.Rdata")
filterStream("/srv/shiny-server/SecretFolder/tweets.json", track = "SecretTopic", oauth = my_oauth)</pre>

OK, so we run the authenticator once, then we run can run this file, which just goes out and gathers all tweets related to `SecretTopic`, and saves them to `tweets.json`. This works with my stream because it&#8217;s relatively small number of tweets&#8230; but be careful, if your topic gets tons of hits, the file can grow VERY quickly. You might be interested in splitting up the output into multiple files. Check [this][7] to see how.

&nbsp;

On working directories, it&#8217;s super annoying, it&#8217;s typically bad practice to specify a direct path to files in your script, instead, it&#8217;s encouraged that you use tech to &#8220;know your path&#8221;&#8230; for example, we can use the `here` package, or use the Project folder. The problem that arises when running files from some kind of automated cron or scheduler is that it doesn&#8217;t know how to read `.Rproj` files, and therefore doesn&#8217;t know what folder to use. I asked this question in the [RStudio Community][8] site, which have sparked a large discussion&#8230; check it out! Anyway, the last script:

&nbsp;

#### Tweet-analyzer

<pre class="EnlighterJSRAW" data-enlighter-language="null">## read
library(streamR)
tweets.df &lt;- parseTweets("tweets.json", verbose = FALSE)

## Do the Secret Stuff 🙂</pre>

&nbsp;

Ok, so now we can authenticate, gather tweets, and anaylze the resulting file!

&nbsp;

OK cool! So let&#8217;s get the TweetGetter running! As long as it&#8217;s running, it will be appending tweets to the `json` file. We could run it on our laptop, but it’ll stop running when we close our laptop, so that’s a perfect candidate to run on a server. If you don&#8217;t know how to get your stuff up into a linux server, I recommend saving your work locally, setting up git, `git push`ing it up to a private github remote (CAREFUL! This will have your Private Keys so make sure you don&#8217;t use a public repo) and then `git pull`ing it into your server.

**EDIT:** As mentioned by @John in the comments, think deeply about security and see if you feel comfortable doing this. You can perfectly well skip this step and just recreate the credential file in the server, that way no private keys would live on github at all&#8230; up to you.

&nbsp;

## OK, set it up to run on the server

(CAVEAT!! I am not a linux expert&#8230; far from it! If anyone sees me doing something boneheaded (like the `chmod 777` above, please leave a comment).

The first time you run the script, it will ask you to authenticate&#8230; So I recommend running the Authenticator file from RStudio on the server, which will allow you to grab the auth code and paste it into the Rstudio session. Once you&#8217;re done, you should be good to capture tweets on that server. The problem is, if you run the TweetGetter in RStudio&#8230; when you close that session, it stops the script.

&nbsp;

**Idea 2:** Hrm&#8230; let&#8217;s try in the shell. So SSH into the server (on windows use Putty), go to the Project folder and type:

<pre class="EnlighterJSRAW" data-enlighter-language="shell">Rscript TweetGetter.R</pre>

&nbsp;

It runs, but when I close the SSH session it also stops the script :-\ . I guess that instance is tied to the SSH session? I don&#8217;t get it&#8230; but whatever, fine.

**Idea 3**: set a cronjob to run it! In case you don&#8217;t know, cron jobs are the schedulers on linux. Run `crontab -e` to edit the jobs, and `crontab -l` to view what jobs you have scheduled. To understand the syntax of the crontabs, [see this][9].

&nbsp;

So the idea would be to start the task on a schedule&#8230; that way it&#8217;s not my session that started it&#8230; although of course, if it&#8217;s set on a schedule and the schedule dictates it&#8217;s time to start up again but the file is already running, I don&#8217;t want it to run twice&#8230; hrm&#8230;

&nbsp;

Oh I know! I&#8217;ll create a small bash file (like a small executable) that CHECKS if the thingie is running, and if it isn&#8217;t then run it, if it is, then don&#8217;t do anything! This is what I came up with:

<pre class="EnlighterJSRAW" data-enlighter-language="shell">if pgrep -x "Rscript" &gt; /dev/null then
    echo "Running"
else
    echo "Stopped... restarting"
    Rscript "/srv/shiny-server/SecretFolder/newTweetGetter.R"
fi</pre>

<span style="color: #ff0000;">WARNING! THIS IS WRONG.</span>

What this is saying is &#8220;check if &#8216;Rscript&#8217; is running on the server (I assumed I didn&#8217;t have  any OTHER running R process at the time, a valid assumption in this case). If it is, then just say &#8216;Running&#8217;, if it&#8217;s not, then say &#8216;Stopped&#8230; restarting&#8217; and re-run the file, using `Rscript`. Then, we can put file on the cron job to run hourly&#8230; so hourly I will check if the job is running or not, and if it&#8217;s stopped, restart. This is what the cron job looks like:

`1 * * * * "/srv/shiny-server/SecretFolder/chek.sh"`

In other words, run the file `chek.sh` during minute 1 of every hour, every day of money, every month of the year, and every day of the week (ie, every hour :))

OK…. Cool! So I’m good right? Let me check if the json is getting tweets… hrm… no data in the past 10 minutes or so… has nobody tweeted or is it broken? Hrm2… how does one check the cronjob log file? Oh, there is none… but shouldn&#8217;t there be? ::google:: I guess there is supposed to be one&#8230; ::think:: Oh, it&#8217;s because I&#8217;m logged in with a user that doesn&#8217;t have admin rights, so when it tries to create a log file in a protected folder, it gets rejected&#8230; Well Fine! I&#8217;ll pipe the output of the run to a file in a folder I know I can write to. (Another option is to set up the cron job as the root admin&#8230;. ie instead of `crontab -e` you would say `sudo crontab -e`&#8230; but if there&#8217;s one thing I know about linux is that I don&#8217;t know linux and therefore I use admin commands as infrequently as I can get away with). So how do I pipe run contents to a location I can see? Well&#8230; google says this is one way:

&nbsp;

<pre class="EnlighterJSRAW" data-enlighter-language="shell">40 * * * * "/srv/shiny-server/SecretFolder/chek.sh" &gt;&gt; /home/amit/SecretTweets.log 2&gt;&1</pre>

So what this is doing is running the file just as before, but the `>>` pushes the results to a log file on my home directory. Just a bit of Linux for you&#8230; `>` recreates the piped output everytime (ie overwrites), whereas `>>` appends to what was already there. The `2>&1` part means &#8216;grab standard output and errors&#8217;&#8230; if you wanna read more about why, [geek out][10], but I think you&#8217;re basically saying &#8220;grab any errors and pipe them to standard output and then grab all standard output&#8221;.

OK, so after looking at the output, I saw what was happening&#8230; during every crontab run, the `chek.sh` file made it seem like the `newTweetGetter.R` wasn&#8217;t running&#8230; so it would restart it, gather 1 tweet and then time out. 🙁 What strange behaviour! Am I over some Twitter quota? No, it can&#8217;t be, it&#8217;s a streaming service, twitter will feed me whatever it wants, I&#8217;m not requesting any amount&#8230; so it can&#8217;t be that.

&nbsp;

> here is where I threw my hands up and asked [Richard][11], my local linux expert for help

Enter a very useful command: `top`. This command, and it&#8217;s slightly cooler version `htop` (which doesn&#8217;t come in Ubuntu by default but is easy to install&#8230; `sudo apt install htop`) quickly showed me that when you call an R file via `Rscript`, it doesn&#8217;t launch a service called `Rscript`, it launches a service called `/usr/lib/R/bin/exec/R --slave --no-restore --file=/srv/shiny-server/SecretFolder/newTweetGetter.R`.  Which explains why `chek.sh` didn&#8217;t think it was running (when it was)&#8230; and when the second run would try to connect to the twitter stream, it got rejected (because the first script was already connected). So this is where Richard said &#8220;BTW, you should probably set this up as a service&#8230;&#8221;. And being who I am and Richard who he is, I said: &#8220;ok&#8221;. (Although I didn&#8217;t give up on the cron&#8230; see <span style="color: #ff00ff;">ENDNOTE1</span>).

After a bit of playing around, we found that the shiny-server linux service was probably easy enough to manipulate and get functional (guidance [here][12] and [here][13]), so let&#8217;s do it!

## Setting up the service:

  1. First of all, go to the folder where all the services live.  `cd /etc/systemd/system/`
  2. Next, copy the shiny service into your new one, called SECRETtweets.service: `sudo cp shiny-server.service SECRETtweets.service`
  3. Now edit the contents! `sudo nano SECRETtweets.service` and copy paste the following code:

<pre class="EnlighterJSRAW" data-enlighter-language="shell">[Unit]
Description=SECRETTweets

[Service]
Type=simple
User=amit
ExecStart=/usr/bin/Rscript "/srv/shiny-server/SecretFolder/newTweetGetter.R"
Restart=always
WorkingDirectory= /srv/shiny-server/SecretFolder/
Environment="LANG=en_US.UTF-8"


[Install]
WantedBy=multi-user.target
</pre>

4. restart the daemon that picks up services? Don&#8217;t know why&#8230; just do it: `sudo systemctl daemon-reload`

5. Now start the service!! `sudo systemctl start SECRETtweets`

&nbsp;

Now your service is running! You can check the status of it using: `systemctl status SECRETtweets.service`

Where each part does this:

  * **Description** is what the thingie does
  * **Type** says how to run it, and &#8220;simple&#8221; is the default&#8230; but check the documentation if u wanna do something more fancy
  * **User** this defines what user is running the service. This is a bit of extra insurance, in case you installed a package as a yourself and not as a superuser (which is the correct way)
  * **ExecStart** is the command to run
  * **Restart** by specifying this to &#8220;always&#8221;, if the script ever goes down, it&#8217;ll automatically restart and start scraping again! 🙂 Super cool, no? <span style="color: #ff9900;">WARNING: Not sure about whether this can cause trouble&#8230; if twitter is for some reason pissed off and doesn&#8217;t want to serve tweets to you anymore, not sure if CONSTANTLY restarting this could get you in trouble. If I get banned, I&#8217;ll letchu know&#8230; stay tuned</span>)
  * **WorkingDirectory **This part is where the magic happens. Remember earlier on we were worried and worried about HOW to pass the working directory to the R script? This is how!! Now we don&#8217;t have to worry about paths on the server anymore!
  * **Environment **is the language
  * **WantedBy** I have no idea what this does and don&#8217;t care because it works!

So there you go! This is the way to set up a proper service that you can monitor, and treat properly like any formal linux process! Enjoy!

&nbsp;

<span style="color: #ff00ff;">ENDNOTE 1</span>

Ok, it&#8217;s true&#8230; sometimes a Service is the right thing to do, if you have a job that runs for a certain amount of time, finishes, and then you want to run it again discretely later, you should set it up as a cron job. So for those cases, here&#8217;s the correct script to check the script is running, even assigning a working directory.

<pre class="EnlighterJSRAW" data-enlighter-language="null">if ps aux | grep "R_file_you_want_to_check.R"  | grep -v grep &gt; /dev/null
then
  echo "Running, all good!"
else
  echo "Not running... will restart:"
  cd /path_to_your_working_directory
  Rscript "R_file_you_want_to_check.R" 
fi
</pre>

&nbsp;

save that as `chek.sh` and assign it to the cron with the output to your home path, like:

`40 * * * * "/srv/shiny-server/SecretFolder/chek.sh" >> /home/amit/SecretTweets.log 2>&1`

&nbsp;

 [1]: https://cran.r-project.org/web/packages/twitteR/index.html
 [2]: https://cran.r-project.org/web/packages/streamR/index.html
 [3]: https://github.com/mexindian/linuxRstuff
 [4]: deanattali.com/2015/05/09/setup-rstudio-shiny-server-digital-ocean/
 [5]: https://m.do.co/c/d925aae2d09f
 [6]: https://apps.twitter.com/
 [7]: http://enhancedatascience.com/2017/07/17/twitter-analysis-using-r/
 [8]: https://community.rstudio.com/t/best-way-to-define-paths-for-a-file-running-on-a-cron/2061
 [9]: http://www.adminschoice.com/crontab-quick-reference
 [10]: https://stackoverflow.com/questions/818255/in-the-shell-what-does-21-mean
 [11]: https://www.linkedin.com/in/richardstrand/
 [12]: https://www.freedesktop.org/software/systemd/man/systemd.service.html
 [13]: https://www.freedesktop.org/software/systemd/man/systemd.exec.html#