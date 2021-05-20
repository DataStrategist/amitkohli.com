---
title: R Tagosphere!
author: Amit
type: post
date: 2016-01-31T17:41:10+00:00
url: /r-tagosphere/
switch_like_status:
  - 1
categories:
  - Art
  - Big data
  - Data
  - R
  - Visualizations
  - Analysis
tags:
  - Chart
  - d3
  - d3Network
  - Network
  - network3d
  - StackOverflow
  - Tag
  - Visualization

---
This post explores the inter-relationships of StackOverflow Tags for R-related questions. So I grabbed all the questions tagged with &#8220;r&#8221;, took the other tags in each question and made some network charts that show how often each tag is seen with the other tags. The point is to see the empirical relationships that develop as people organically describe their problems with R. [Full analysis on GitHub][1], as always.

<newbie> For the non-techies out there: [StackOverflow.com][2] is a question and answer website which many techies LOVE because in many cases it&#8217;s the best place to get answers when you&#8217;re stuck&#8230; I&#8217;ve used it a bunch of times. When you ask a question, you can tag it with (mostly) pre-defined &#8220;Tags&#8221; that help experts find your question. For example, I might ask a question: &#8220;How can I sum three numbers in Excel?&#8221;. In this case, I&#8217;d be smart to add the tags: `Excel` and `Formula`. This will help Excel and Formula experts to find my question and answer it quickly. Anyway, StackOverflow (or SO) is this whole thing, [check it out][3]&#8230; it&#8217;s awesome.** **

What I did was harvest all the questions regarding the stats program R, and then took all the other tags in that question and showed the relationships between these tags. </newbie>

## Aaaaaaaaaaaaaaanyway:

Using the tremendously awesome [SO Data Explorer][4] which lets you query the entire SO question corpus, I found a query close enough to what I wanted and downloaded all the questions that had the tag &#8220;r&#8221;. A little manipulation and I&#8217;m ready to plot the relationships! But plot what? I can imagine that the tag `ggplot2 `would often be related to the tag  ``This post explores the inter-relationships of StackOverflow Tags for R-related questions. So I grabbed all the questions tagged with &#8220;r&#8221;, took the other tags in each question and made some network charts that show how often each tag is seen with the other tags. The point is to see the empirical relationships that develop as people organically describe their problems with R. [Full analysis on GitHub][1], as always.

<newbie> For the non-techies out there: [StackOverflow.com][2] is a question and answer website which many techies LOVE because in many cases it&#8217;s the best place to get answers when you&#8217;re stuck&#8230; I&#8217;ve used it a bunch of times. When you ask a question, you can tag it with (mostly) pre-defined &#8220;Tags&#8221; that help experts find your question. For example, I might ask a question: &#8220;How can I sum three numbers in Excel?&#8221;. In this case, I&#8217;d be smart to add the tags: `Excel` and `Formula`. This will help Excel and Formula experts to find my question and answer it quickly. Anyway, StackOverflow (or SO) is this whole thing, [check it out][3]&#8230; it&#8217;s awesome.** **

What I did was harvest all the questions regarding the stats program R, and then took all the other tags in that question and showed the relationships between these tags. </newbie>

## Aaaaaaaaaaaaaaanyway:

Using the tremendously awesome [SO Data Explorer][4] which lets you query the entire SO question corpus, I found a query close enough to what I wanted and downloaded all the questions that had the tag &#8220;r&#8221;. A little manipulation and I&#8217;m ready to plot the relationships! But plot what? I can imagine that the tag `ggplot2 `would often be related to the tag  ``  so there should be a connection there&#8230; but should that count as much as a one-off random relationship? In order to answer this, we count _how many times_ we saw the relationship, and call it the **Link Strength (LS)**. So tags that are very frequently linked together will have a very high LS, and the one-off will have a low LS.

Jumping right to it, BOOM! Here is LS=10 (this will only show tags as related if they were seen together more than 10 times) :

<a href="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/Simple10.png" rel="attachment wp-att-520"><img class="alignnone size-medium wp-image-520" src="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/Simple10.png?resize=300%2C192" alt="Simple10" width="300" height="192" srcset="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/Simple10.png?resize=300%2C192 300w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/Simple10.png?resize=768%2C492 768w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/Simple10.png?resize=1024%2C657 1024w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/Simple10.png?resize=700%2C449 700w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/Simple10.png?w=1360 1360w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" /></a>

&nbsp;

[>>Play with the interactive version though<<][5], it&#8217;s WAAAAAAAAAAAAAAY funner (by the way, Ctrl+F works on it :)). Here it is in an ugly iframe:

<!-- iframe plugin v.4.3 wordpress.org/plugins/iframe/ -->

Two problems with this one:

  1. It&#8217;s not possible to distinguish the strong links (with high LS) from the weak links
  2. Those &#8220;floaters&#8221; that you see in the peripheries might be related to the central network&#8230; the link might just be seen less than 10 times.

OK, so let&#8217;s take a step back and figure out the <a href="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/LinkStrength.png" rel="attachment wp-att-518"><img class="size-medium wp-image-518 alignright" src="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/LinkStrength.png?resize=300%2C182" alt="LinkStrength" width="300" height="182" srcset="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/LinkStrength.png?resize=300%2C182 300w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/LinkStrength.png?resize=768%2C465 768w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/LinkStrength.png?resize=268%2C164 268w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/LinkStrength.png?resize=700%2C424 700w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/LinkStrength.png?w=919 919w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" /></a>LS for all tag-pairs. Plotting that, we see that the link strength increases very slowly (see figure to the right-top, and a blowup of the &#8220;elbow&#8221; right-bottom). As can be seen, around 6000 of our 7000ish tag-pairs have a LS <10.

**CONCLUSION 1: Most tag relationships are seen less than 10 times, which shows the <a href="https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/01/LinkStrengthBlowup.png" rel="attachment wp-att-519"><img class="size-medium wp-image-519 alignright" src="https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/01/LinkStrengthBlowup.png?resize=300%2C187" alt="LinkStrengthBlowup" width="300" height="187" srcset="https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/01/LinkStrengthBlowup.png?resize=300%2C187 300w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/01/LinkStrengthBlowup.png?resize=768%2C478 768w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/01/LinkStrengthBlowup.png?resize=700%2C436 700w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/01/LinkStrengthBlowup.png?w=919 919w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" /></a>huge heterogeneity of the questions of the r user community.**

&nbsp;

To investigate further, let&#8217;s plot charts at LS= 1, 10, 100, where the LS is the thickness of each link (thicker is higher Link Strength). To accomplish this I used the ForceNetwork rather than the SimpleNetwork functions of the D3Network package (yes I know the new one is called network3d but I haven&#8217;t installed it yet, sue me). Oh, and these charts are zoom and scroll enabled, so enjoy the interactive versions here: [LS=1][6], [LS = 10][7], [LS = 100][8]. They are way better to navigate. Hover your mouse over each node to see the tag name.

<a href="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/01/Complex1.png" rel="attachment wp-att-521"><img class="alignnone wp-image-521" src="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/01/Complex1.png?resize=237%2C195" alt="Complex1" width="237" height="195" srcset="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/01/Complex1.png?zoom=2&resize=237%2C195 474w, https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/01/Complex1.png?zoom=3&resize=237%2C195 711w" sizes="(max-width: 237px) 100vw, 237px" data-recalc-dims="1" /></a> <a href="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/Complex10.png" rel="attachment wp-att-522"><img class="alignnone wp-image-522" src="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/Complex10.png?resize=205%2C195" alt="Complex10" width="205" height="195" srcset="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/Complex10.png?resize=300%2C284 300w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/01/Complex10.png?w=384 384w" sizes="(max-width: 205px) 100vw, 205px" data-recalc-dims="1" /></a> <a href="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/01/Complex100.png" rel="attachment wp-att-523"><img class="alignnone wp-image-523" src="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/01/Complex100.png?resize=138%2C143" alt="Complex100" width="138" height="143" srcset="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/01/Complex100.png?resize=290%2C300 290w, https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/01/Complex100.png?w=314 314w" sizes="(max-width: 138px) 100vw, 138px" data-recalc-dims="1" /></a>

So. considering that the LS variability is mostly very low  (which is what we saw on the LS  point charts above anyway), I&#8217;m going to go out on a limb and say that the Link Strength per se is an interesting but perhaps unnecessary visualization element&#8230; it seems like the number of links to other nodes is more important. Therefore:

**Conclusion 2: Tag popularity (as relates to R) is best predicted by how &#8220;central&#8221; a node is, not by the LS of its connections to other nodes**. Here, centrality is used as a proxy to describe how many OTHER Tags it&#8217;s connected to. I could count them, but meh&#8230; you do it.

### Conclusion

I think that Network charts are a great way of exploring the relationships between tags. These relationships, when mapped together somehow show how we all use our beloved r. For example, in the LS=10 chart I provided, you can see the following topical &#8220;arms&#8221;: machine learning, packages, knitr, xml, sql, shiny, rstudio, regex, etc, all with a bunch of tags within each arm. You&#8217;ve also got the messy internal cluster tags that are linked to by EVERYONE&#8230; these are the r staples.

Anyway, These network charts can also be used to investigate new tags that might be interesting to users that consider themselves specialists in a specific area.

It&#8217;s a bit tricky to figure out the best LS to visualize&#8230; I like 10&#8230; but feel free to play around. I also started playing around with a method of identifying specific tags to explore&#8230; it&#8217;s in the R-script&#8230; it&#8217;s not great but might be a good start&#8230; check it out if interested.

This analysis could be used for any tag. I chose &#8220;r&#8221;, but it&#8217;s easy to see how to change the query to get all the questions for any other tag too&#8230; check out the script.

### A gift for everyone!

So this is just the tip of this analysis. <del>I&#8217;ve made a csv with just the Link Strengths for each pair of tags </del>(oh, its 500 megs&#8230; extract it yourself from the R code)&#8230; it can be found in [the GitHub repo][1]. Of course while you&#8217;re there and you might find out that the initial query from SO has more than _just _the tagnames for each question&#8230; go crazy internets!

### A gift for rich people

OK fine you rich bastards&#8230; you have a computer that can handle big data and a 4k monitor? Enjoy the [full_pawwah of the complete network (LS>1), plotted using the Simple technique which will have all teh names etc, at 4k rez][9]. I hope you choke.

_(edited by [Laure Belotti][10])_

## Update:

After some discussions, I figured it would be more fun to think about what the R-Taggosphere looks like WITHOUT the top tags which muck up the picture by being too popular and having too many relationships. What&#8217;s left is an easier to read network of weaker connections, which do paint a very interesting albeit unexpected picture. <a href="https://amitkohli.com/wp-content/uploads/2016/01/LS3withoutTop35.html" rel="">Check out the interactive version</a>! Or iframed below:

<!-- iframe plugin v.4.3 wordpress.org/plugins/iframe/ -->

(Incedentally, the top tags are (from popularest to least): ggplot2|plot|data.frame|matrix|shiny|knitr|loops|function|for-loop|list|rstudio|time-series|statistics|data.table|python|subset|apply|xts|plyr|rmarkdown|regression|graph|dplyr|latex|vector|csv|merge|lapply|legend|date|dataframes|rcpp|regex|string|zoo)

 [1]: https://github.com/datastrategist/StackOverflow-tag-Network-R
 [2]: http://StackOverflow.com
 [3]: http://stackoverflow.com/
 [4]: http://data.stackexchange.com
 [5]: https://amitkohli.com/wp-content/uploads/2016/01/Simple10.html
 [6]: https://amitkohli.com/wp-content/uploads/2016/01/Complex1.html
 [7]: https://amitkohli.com/wp-content/uploads/2016/01/Complex10.html
 [8]: https://amitkohli.com/wp-content/uploads/2016/01/Complex100.html
 [9]: https://amitkohli.com/wp-content/uploads/2016/01/Simple1.4k.html
 [10]: https://www.linkedin.com/in/laure-belotti-6b301218