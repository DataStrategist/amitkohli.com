---
title: The Reddit effect…
author: Amit
type: post
date: 2015-05-01T19:32:56+00:00
url: /the-reddit-effect/
categories:
  - Data
  - R
  - Visualizations
tags:
  - hug of death
  - log
  - parsing
  - reddit

---
So I had a happy little blog&#8230; no one really paid attention, but I didn&#8217;t much care because I was happy.

And then I posted [one of my visualizations][1] to reddit. This is what happened:

[<img class="alignnone size-medium wp-image-346" src="https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/05/ChordProgressionsNotes.png?resize=300%2C170" alt="ChordProgressionsNotes" width="300" height="170" srcset="https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/05/ChordProgressionsNotes.png?resize=300%2C170 300w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/05/ChordProgressionsNotes.png?resize=1024%2C581 1024w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/05/ChordProgressionsNotes.png?resize=700%2C397 700w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/05/ChordProgressionsNotes.png?w=1200 1200w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" />][2]

(None of the log analyzers I found would make a plot like this so I made it myself by parsing the log file itself, [script is on github][3]).

So obviously, Reddit made the whole thing go crazy, including bringing my site down&#8230; but there&#8217;s lots of other interesting insights here. From this graph, it&#8217;s clear to tell that the Reddit traffic came like a storm, and left like a storm&#8230; leaving in its wake a bunch of facebook and twitter hits (twitter wasn&#8217;t visible in my log btw&#8230; apparently they mask themselves, so you&#8217;ll just have to take my word for it that the traffic pattern was just like facebook&#8217;s, if a little lower). Then some days later, someone posted on YCombinator news, which had an immediate effect of having the facebook traffic jump a bit, and even someone reposting on reddit, this time in the Musicaltheory sub (although it was the weekend, so hard to establish causality).

What is interesting is how quickly reddit and ycombinator traffic falls below the facebook/twitter slow-and-steady approach, and how (at least in this case) it never really &#8220;blew up&#8221; on facebook, but did the &#8216;long-tail&#8217; did last a loooong time.

&nbsp;

Quick question for anyone that knows about logging and WordPress: These are my top 3 &#8220;referrers&#8221;:

  * http://amitkohli.com/?p=246
  * http://amitkohli.com/wp-content/themes/pinboard/style.css
  * http://amitkohli.com/wp-content/themes/pinboard/styles/colorbox.css

The first link is the article itself, and the other two are css files on the theme that I&#8217;m currently using on my blog. How are these &#8220;referrers&#8221;? And why can&#8217;t I see any of the Twitter traffic that I expect?

&nbsp;

All in all&#8230;It was a fun thing to happen to me, even though forevermore my site statistics are messed up, check out my daily hits:

[<img class="alignnone size-medium wp-image-348" src="https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/05/hits.jpg?resize=300%2C261" alt="hits" width="300" height="261" srcset="https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/05/hits.jpg?resize=300%2C261 300w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/05/hits.jpg?w=541 541w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" />][4]

&nbsp;

 [1]: http://amitkohli.com/?p=246
 [2]: https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/05/ChordProgressionsNotes.png
 [3]: https://github.com/mexindian/logReffererTS
 [4]: https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/05/hits.jpg