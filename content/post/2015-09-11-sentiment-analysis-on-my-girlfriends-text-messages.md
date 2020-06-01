---
title: Sentiment analysis on my girlfriend’s text messages
author: Amit
type: post
date: 2015-09-11T13:22:14+00:00
url: /sentiment-analysis-on-my-girlfriends-text-messages/
switch_like_status:
  - 1
categories:
  - Art
  - Data
  - R
  - Visualizations
  - Analysis
tags:
  - Analysis
  - Anniversary
  - Data
  - Love
  - Sentiment

---
When I told my friends that I wanted to give my girlfriend an infographic of us (centered around a sentimental analysis of our texts) as a gift for our first anniversary, most of them told me that was a terrible idea. Yeah&#8230; well&#8230; CHALLENGE ACCEPTED!! Without further ado, this is what love looks like:

[<img class="alignnone size-medium wp-image-372" src="https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/08/senAn.png?resize=300%2C100" alt="senAn" width="300" height="100" srcset="https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/08/senAn.png?resize=300%2C100 300w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/08/senAn.png?resize=700%2C234 700w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/08/senAn.png?w=932 932w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" />][1]

## What&#8230; um&#8230;. what are we looking at?

This is a plot of the aggregate sentiment per day per person of our skype and whatsapp messages. We don&#8217;t sms and email was:

<p style="padding-left: 30px;">
  a) annoying to extract [does anyone know how  an easy way to get gmail into R?], and
</p>

<p style="padding-left: 30px;">
  b) one email consists of lots of words, few times per day&#8230; as opposed to many short messages per day, therefore I didn&#8217;t think it was right to mix with text messages.
</p>

The sentiment was evaluated by comparing to positive and negative word lists. **In other words: When I say that &#8220;we are getting sweeter&#8221;, _I can actually prove it_** (within a reasonable margin of error)*.

## How come she didn&#8217;t break up with me on the spot?

OK ok ok&#8230;. I didn&#8217;t just give her this, I made this part of a whole infographic  about our year together with wordclouds and other stuff that made it lighter. I also made it personal by calling out specific individual days from that plot and displaying the text within to add context to each point. So that&#8217;s when you realize each point is actually a day from our lives, some good, some bad&#8230; it&#8217;s like a memory thing. Especially true because those few I called out were special days in which we texted especially nice things. It was sweet&#8230; I guess u had to be there. Also, the first year anniversary is paper, so it&#8217;s perfectly apropos. Also2, I spent a TON of time on this. Chicks dig it when you spend effort on them. Also3, she&#8217;s dating a geek, she expects this kinds of thing from me and loves it.

## How did I do it?

I typically post my analyses to github, but I won&#8217;t this time for obvious reasons&#8230; here&#8217;s the general flow of how I did it:

  1. Find someone to love. Write lots of text messages to each other for a year.
  2. Get the logs. I used whatsapp (email yourself the whole log, it&#8217;s in the settings) and skype (at the time I did the analysis you could get up to 6 months of history. Just copy paste it into a text file)
  3. Clean the logs. This part is super annoying. Every time we were texting and anyone pasted in something from somewhere else (like a link or copypasting from another conversation), it breaks the line-number scheme. There might be better ways to clean it, but for me it was a bit of regex, a LOT of manual cleaning and iterating. There are also a lot of encoding problems if your logs are in more than one language, and lastly, not all emoji translates to text nicely.  If they didn&#8217;t, I just deleted them&#8230; which sucks (This is kind of a big deal since there&#8217;s a lot of sentiment in emojis 🙁 :'(. Somebody should come up w/ a emoji sentiment valence table for whatsapp). What you want in the end is a text file that has 3 columns: Timestamp, name, clean text, seperated by a unique delimiter, for example &#8220;|&#8221;. Keep munging till you have that.
  4. Read Whatsapp log into R 
      1. Realize that the logs within the  current year don&#8217;t have the year in the timestamp, so add it manually.
  5. Read in Skype logs and combine w/ the Whatsapp
  6. Realize that the timestamps are different between the logs. Pull your hair out remembering how to deal w/ dates in R and munge and munge till they are the same. (no, I&#8217;m not going to learn to use lubridate, I&#8217;m not a quitter).
  7. Done! Now start analyzing!
  8. Sentiment analysis- compare each individual text message against the sentimental Lexicon from Hu and Liu. 
      1. PROTIP &#8211; for easy mode, use the [score_sentiment][2] function from Jeffrey Breen.
      2. Cap positive sentiment greater than 4 to 4&#8230; that&#8217;s good enough. I guess you could cap negative sentiment as well, but I didn&#8217;t have the need.
      3. To create the chart above, aggregate the sentiment scores PER PERSON PER DAY. Now you have two sets of dots, one for you and one for your lover. Plot those bad boys and add the smoothing!
      4. Now that you have the sentiment analysis of each text message, other fun things you can do (not shown here, but you&#8217;ll get the picture): 
          1. When and how do we communicate? and at what time of day are we sweetest and least-sweet
          2. Are we sweeter on Skype or Whatsap?
          3. Sentiment-sensitive wordclouds, etc

## *OK fine, but what does it mean?

OK fine, it don&#8217;t mean a goddam thing but it is interesting to analyze anyway! The rise in sweetness halfway through the year is due to the fact that we were apart, and were forced to be sweet by text and calls more than in person. Interesting that the texts stayed sweet after that. Also interesting that the amount of communication since then really increased.

With regards to the future&#8230;OF COURSE in a normal relationship, text messages start off like this:

<p style="padding-left: 30px;">
  <em>&#8220;I&#8217;m thinking of you, sleep with the angels sweet one&#8221;</em>
</p>

and end up like this:

<p style="padding-left: 30px;">
  <em>&#8220;Did you forget the milk?!&#8221;</em>
</p>

That&#8217;s just what happens in relationships, because we&#8217;ve all got stuff to do and when you share your life with someone, you become part of a team, and from time to time, the team needs milk and sometimes that milk is forgotten for extremely valid and completely unavoidable reasons. So eventually we will get less sweet via text message and what will that mean? Probably nothing at all. Anyway, what do I care? At least we&#8217;re getting sweeter now. 🙂 I&#8217;ll worry bout tomorrow tomorrow.

Joking aside, if nothing else, doing analyses like this force people like me to TRY EXTRA HARD to be sweet even if it&#8217;s not necessary. And intention when text-messaging is important since there&#8217;s NEVER any context to text messages and misunderstandings are common.

So keep up the sweet text-messages, geeks of the world! Don&#8217;t want the trendline to go negative, do we?

_Edited by [Laure Belotti][3]_

&nbsp;

UPDATE: For more &#8220;Love data&#8221;, check out other people that analyzed their partners&#8217; text messages ([HERE][4] and [HERE][5] and [HERE][6]), two people that hacked online dating for their own purposes ([When I told my friends that I wanted to give my girlfriend an infographic of us (centered around a sentimental analysis of our texts) as a gift for our first anniversary, most of them told me that was a terrible idea. Yeah&#8230; well&#8230; CHALLENGE ACCEPTED!! Without further ado, this is what love looks like:

[<img class="alignnone size-medium wp-image-372" src="https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/08/senAn.png?resize=300%2C100" alt="senAn" width="300" height="100" srcset="https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/08/senAn.png?resize=300%2C100 300w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/08/senAn.png?resize=700%2C234 700w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/08/senAn.png?w=932 932w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" />][1]

## What&#8230; um&#8230;. what are we looking at?

This is a plot of the aggregate sentiment per day per person of our skype and whatsapp messages. We don&#8217;t sms and email was:

<p style="padding-left: 30px;">
  a) annoying to extract [does anyone know how  an easy way to get gmail into R?], and
</p>

<p style="padding-left: 30px;">
  b) one email consists of lots of words, few times per day&#8230; as opposed to many short messages per day, therefore I didn&#8217;t think it was right to mix with text messages.
</p>

The sentiment was evaluated by comparing to positive and negative word lists. **In other words: When I say that &#8220;we are getting sweeter&#8221;, _I can actually prove it_** (within a reasonable margin of error)*.

## How come she didn&#8217;t break up with me on the spot?

OK ok ok&#8230;. I didn&#8217;t just give her this, I made this part of a whole infographic  about our year together with wordclouds and other stuff that made it lighter. I also made it personal by calling out specific individual days from that plot and displaying the text within to add context to each point. So that&#8217;s when you realize each point is actually a day from our lives, some good, some bad&#8230; it&#8217;s like a memory thing. Especially true because those few I called out were special days in which we texted especially nice things. It was sweet&#8230; I guess u had to be there. Also, the first year anniversary is paper, so it&#8217;s perfectly apropos. Also2, I spent a TON of time on this. Chicks dig it when you spend effort on them. Also3, she&#8217;s dating a geek, she expects this kinds of thing from me and loves it.

## How did I do it?

I typically post my analyses to github, but I won&#8217;t this time for obvious reasons&#8230; here&#8217;s the general flow of how I did it:

  1. Find someone to love. Write lots of text messages to each other for a year.
  2. Get the logs. I used whatsapp (email yourself the whole log, it&#8217;s in the settings) and skype (at the time I did the analysis you could get up to 6 months of history. Just copy paste it into a text file)
  3. Clean the logs. This part is super annoying. Every time we were texting and anyone pasted in something from somewhere else (like a link or copypasting from another conversation), it breaks the line-number scheme. There might be better ways to clean it, but for me it was a bit of regex, a LOT of manual cleaning and iterating. There are also a lot of encoding problems if your logs are in more than one language, and lastly, not all emoji translates to text nicely.  If they didn&#8217;t, I just deleted them&#8230; which sucks (This is kind of a big deal since there&#8217;s a lot of sentiment in emojis 🙁 :'(. Somebody should come up w/ a emoji sentiment valence table for whatsapp). What you want in the end is a text file that has 3 columns: Timestamp, name, clean text, seperated by a unique delimiter, for example &#8220;|&#8221;. Keep munging till you have that.
  4. Read Whatsapp log into R 
      1. Realize that the logs within the  current year don&#8217;t have the year in the timestamp, so add it manually.
  5. Read in Skype logs and combine w/ the Whatsapp
  6. Realize that the timestamps are different between the logs. Pull your hair out remembering how to deal w/ dates in R and munge and munge till they are the same. (no, I&#8217;m not going to learn to use lubridate, I&#8217;m not a quitter).
  7. Done! Now start analyzing!
  8. Sentiment analysis- compare each individual text message against the sentimental Lexicon from Hu and Liu. 
      1. PROTIP &#8211; for easy mode, use the [score_sentiment][2] function from Jeffrey Breen.
      2. Cap positive sentiment greater than 4 to 4&#8230; that&#8217;s good enough. I guess you could cap negative sentiment as well, but I didn&#8217;t have the need.
      3. To create the chart above, aggregate the sentiment scores PER PERSON PER DAY. Now you have two sets of dots, one for you and one for your lover. Plot those bad boys and add the smoothing!
      4. Now that you have the sentiment analysis of each text message, other fun things you can do (not shown here, but you&#8217;ll get the picture): 
          1. When and how do we communicate? and at what time of day are we sweetest and least-sweet
          2. Are we sweeter on Skype or Whatsap?
          3. Sentiment-sensitive wordclouds, etc

## *OK fine, but what does it mean?

OK fine, it don&#8217;t mean a goddam thing but it is interesting to analyze anyway! The rise in sweetness halfway through the year is due to the fact that we were apart, and were forced to be sweet by text and calls more than in person. Interesting that the texts stayed sweet after that. Also interesting that the amount of communication since then really increased.

With regards to the future&#8230;OF COURSE in a normal relationship, text messages start off like this:

<p style="padding-left: 30px;">
  <em>&#8220;I&#8217;m thinking of you, sleep with the angels sweet one&#8221;</em>
</p>

and end up like this:

<p style="padding-left: 30px;">
  <em>&#8220;Did you forget the milk?!&#8221;</em>
</p>

That&#8217;s just what happens in relationships, because we&#8217;ve all got stuff to do and when you share your life with someone, you become part of a team, and from time to time, the team needs milk and sometimes that milk is forgotten for extremely valid and completely unavoidable reasons. So eventually we will get less sweet via text message and what will that mean? Probably nothing at all. Anyway, what do I care? At least we&#8217;re getting sweeter now. 🙂 I&#8217;ll worry bout tomorrow tomorrow.

Joking aside, if nothing else, doing analyses like this force people like me to TRY EXTRA HARD to be sweet even if it&#8217;s not necessary. And intention when text-messaging is important since there&#8217;s NEVER any context to text messages and misunderstandings are common.

So keep up the sweet text-messages, geeks of the world! Don&#8217;t want the trendline to go negative, do we?

_Edited by [Laure Belotti][3]_

&nbsp;

UPDATE: For more &#8220;Love data&#8221;, check out other people that analyzed their partners&#8217; text messages ([HERE][4] and [HERE][5] and [HERE][6]), two people that hacked online dating for their own purposes (][7] and [HERE][8]), and of course, the motherload of Love-data: <http://blog.okcupid.com/>. Enjoy!

&nbsp;

<div>
</div>

<div>
</div>

<div>
</div>

<div>
</div>

 [1]: https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/08/senAn.png
 [2]: https://github.com/jeffreybreen/twitter-sentiment-analysis-tutorial-201107/blob/master/R/sentiment.R
 [3]: https://www.linkedin.com/pub/laure-belotti/18/12/6b3
 [4]: http://www.theatlantic.com/technology/archive/2015/03/re-our-relationship/389030/?utm_source=SFFB
 [5]: https://www.reddit.com/r/dataisbeautiful/comments/36d3dd/word_cloud_of_100000_messages_from_a_long/
 [6]: http://adashofdata.com/2014/10/14/how-text-messages-change-from-dating-to-marriage/
 [7]: https://www.youtube.com/watch?v=d6wG_sAdP0U
 [8]: http://www.wired.com/2014/01/how-to-hack-okcupid/