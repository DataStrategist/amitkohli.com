---
title: KPI dashboard in R with animated icons
author: Amit
type: post
date: 2016-02-12T10:08:04+00:00
url: /kpi-dashboard-in-r-with-animated-icons/
categories:
  - Data
  - R
  - Tutorials
tags:
  - Animated
  - Animated gif
  - Dashboard
  - GoogleVis
  - KPI
  - Measure
  - Table
  - Target

---
So Key Performance Indicators (KPIs) are all the rage in the dashboarding community&#8230; well [So Key Performance Indicators (KPIs) are all the rage in the dashboarding community&#8230; well][1] really. The premise is simple&#8230; check a list of measurements against targets and show how they compare using some kind of visualization. I haven&#8217;t yet seen, however, a version that can utilize animated icons to display indicators that REALLY need attention. So here you go, a tutorial on how to make your very own animated icon KPI, using the googleVis library.

Suppose we have a dataset that looks like this (make sure to set your working directory):

`library(googleVis)<br />
## Set wd<br />
setwd("your folder")<br />
df <- data.frame(thing=paste("Item",1:15),<br />
measure=round(runif(15,max=10),2),<br />
target=round(runif(15,max=10),2))<br />
## unimpresive dashboard<br />
plot(gvisTable(df))`

<a href="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png" rel="attachment wp-att-555"><img class="alignnone size-medium wp-image-555" src="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png?resize=165%2C300" alt="data" width="165" height="300" srcset="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png?resize=165%2C300 165w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png?w=303 303w" sizes="(max-width: 165px) 100vw, 165px" data-recalc-dims="1" /></a>

A normal KPI would then compare the measure to the target and apply some rationale. Suppose in our case that green indicates that for that indicator you are within 80% of your target. Yellow means up to 50% of target, and red is below that.

Now, we need some icons. We can download them, or make them ourselves (protip: MS Powerpoint has some interesting possibilities with their glow/highlight/dropshadow options so this might be a good place to start if you&#8217;re not a graphic designer). Now that we have icons, we can split up the dataset into good, bad and medium categories and assign icons to each:

&nbsp;

``So Key Performance Indicators (KPIs) are all the rage in the dashboarding community&#8230; well [So Key Performance Indicators (KPIs) are all the rage in the dashboarding community&#8230; well][1] really. The premise is simple&#8230; check a list of measurements against targets and show how they compare using some kind of visualization. I haven&#8217;t yet seen, however, a version that can utilize animated icons to display indicators that REALLY need attention. So here you go, a tutorial on how to make your very own animated icon KPI, using the googleVis library.

Suppose we have a dataset that looks like this (make sure to set your working directory):

`library(googleVis)<br />
## Set wd<br />
setwd("your folder")<br />
df <- data.frame(thing=paste("Item",1:15),<br />
measure=round(runif(15,max=10),2),<br />
target=round(runif(15,max=10),2))<br />
## unimpresive dashboard<br />
plot(gvisTable(df))`

<a href="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png" rel="attachment wp-att-555"><img class="alignnone size-medium wp-image-555" src="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png?resize=165%2C300" alt="data" width="165" height="300" srcset="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png?resize=165%2C300 165w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png?w=303 303w" sizes="(max-width: 165px) 100vw, 165px" data-recalc-dims="1" /></a>

A normal KPI would then compare the measure to the target and apply some rationale. Suppose in our case that green indicates that for that indicator you are within 80% of your target. Yellow means up to 50% of target, and red is below that.

Now, we need some icons. We can download them, or make them ourselves (protip: MS Powerpoint has some interesting possibilities with their glow/highlight/dropshadow options so this might be a good place to start if you&#8217;re not a graphic designer). Now that we have icons, we can split up the dataset into good, bad and medium categories and assign icons to each:

&nbsp;

`` 

<a href="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/02/ohnoes.png" rel="attachment wp-att-559"><img class="alignnone size-medium wp-image-559" src="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/02/ohnoes.png?resize=151%2C300" alt="ohnoes" width="151" height="300" srcset="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/02/ohnoes.png?resize=151%2C300 151w, https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/02/ohnoes.png?w=226 226w" sizes="(max-width: 151px) 100vw, 151px" data-recalc-dims="1" /></a>

Oh no! Why won&#8217;t it work? Relax, it&#8217;s because we are in the localhost. See how the address is http://127.0.0.1/&#8230; ? This isn&#8217;t a real webpage, it&#8217;s launching from your computer. We need to port out the right elements into a handy-dandy webpage <span style="color: #999999;">(the code is very ugly, but SUPER flexible&#8230; you can pass css elements, titles, javascript&#8230; hell you can even create a fully functional webpage like this! I love this method, don&#8217;t bash it!)</span>:

```So Key Performance Indicators (KPIs) are all the rage in the dashboarding community&#8230; well [So Key Performance Indicators (KPIs) are all the rage in the dashboarding community&#8230; well][1] really. The premise is simple&#8230; check a list of measurements against targets and show how they compare using some kind of visualization. I haven&#8217;t yet seen, however, a version that can utilize animated icons to display indicators that REALLY need attention. So here you go, a tutorial on how to make your very own animated icon KPI, using the googleVis library.

Suppose we have a dataset that looks like this (make sure to set your working directory):

`library(googleVis)<br />
## Set wd<br />
setwd("your folder")<br />
df <- data.frame(thing=paste("Item",1:15),<br />
measure=round(runif(15,max=10),2),<br />
target=round(runif(15,max=10),2))<br />
## unimpresive dashboard<br />
plot(gvisTable(df))`

<a href="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png" rel="attachment wp-att-555"><img class="alignnone size-medium wp-image-555" src="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png?resize=165%2C300" alt="data" width="165" height="300" srcset="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png?resize=165%2C300 165w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png?w=303 303w" sizes="(max-width: 165px) 100vw, 165px" data-recalc-dims="1" /></a>

A normal KPI would then compare the measure to the target and apply some rationale. Suppose in our case that green indicates that for that indicator you are within 80% of your target. Yellow means up to 50% of target, and red is below that.

Now, we need some icons. We can download them, or make them ourselves (protip: MS Powerpoint has some interesting possibilities with their glow/highlight/dropshadow options so this might be a good place to start if you&#8217;re not a graphic designer). Now that we have icons, we can split up the dataset into good, bad and medium categories and assign icons to each:

&nbsp;

``So Key Performance Indicators (KPIs) are all the rage in the dashboarding community&#8230; well [So Key Performance Indicators (KPIs) are all the rage in the dashboarding community&#8230; well][1] really. The premise is simple&#8230; check a list of measurements against targets and show how they compare using some kind of visualization. I haven&#8217;t yet seen, however, a version that can utilize animated icons to display indicators that REALLY need attention. So here you go, a tutorial on how to make your very own animated icon KPI, using the googleVis library.

Suppose we have a dataset that looks like this (make sure to set your working directory):

`library(googleVis)<br />
## Set wd<br />
setwd("your folder")<br />
df <- data.frame(thing=paste("Item",1:15),<br />
measure=round(runif(15,max=10),2),<br />
target=round(runif(15,max=10),2))<br />
## unimpresive dashboard<br />
plot(gvisTable(df))`

<a href="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png" rel="attachment wp-att-555"><img class="alignnone size-medium wp-image-555" src="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png?resize=165%2C300" alt="data" width="165" height="300" srcset="https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png?resize=165%2C300 165w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2016/02/data.png?w=303 303w" sizes="(max-width: 165px) 100vw, 165px" data-recalc-dims="1" /></a>

A normal KPI would then compare the measure to the target and apply some rationale. Suppose in our case that green indicates that for that indicator you are within 80% of your target. Yellow means up to 50% of target, and red is below that.

Now, we need some icons. We can download them, or make them ourselves (protip: MS Powerpoint has some interesting possibilities with their glow/highlight/dropshadow options so this might be a good place to start if you&#8217;re not a graphic designer). Now that we have icons, we can split up the dataset into good, bad and medium categories and assign icons to each:

&nbsp;

`` 

<a href="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/02/ohnoes.png" rel="attachment wp-att-559"><img class="alignnone size-medium wp-image-559" src="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/02/ohnoes.png?resize=151%2C300" alt="ohnoes" width="151" height="300" srcset="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/02/ohnoes.png?resize=151%2C300 151w, https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/02/ohnoes.png?w=226 226w" sizes="(max-width: 151px) 100vw, 151px" data-recalc-dims="1" /></a>

Oh no! Why won&#8217;t it work? Relax, it&#8217;s because we are in the localhost. See how the address is http://127.0.0.1/&#8230; ? This isn&#8217;t a real webpage, it&#8217;s launching from your computer. We need to port out the right elements into a handy-dandy webpage <span style="color: #999999;">(the code is very ugly, but SUPER flexible&#8230; you can pass css elements, titles, javascript&#8230; hell you can even create a fully functional webpage like this! I love this method, don&#8217;t bash it!)</span>:

``` 

and now check it out:

<a href="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/02/better.png" rel="attachment wp-att-560"><img class="alignnone size-medium wp-image-560" src="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/02/better.png?resize=150%2C300" alt="better" width="150" height="300" srcset="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/02/better.png?resize=150%2C300 150w, https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/02/better.png?w=242 242w" sizes="(max-width: 150px) 100vw, 150px" data-recalc-dims="1" /></a>

&nbsp;

Not bad&#8230; this is what most KPI indicator lights look like&#8230; But what if we REALLY want to call the attention to some items, say where the measure is less than 20% of the target, let&#8217;s bring out the big guns and assign a red flashing light to the terriblest:

`Threshold3 <- 0.2<br />
## lowlowlowlowlow trigger<br />
df$graphic[df$measure/df$target < Threshold3] <-<br />
'<img src="redFlashing.gif">'<br />
##--- Make html again ----<br />
ObsRep <- gvisTable(df)<br />
# plot(ObsRep)<br />
cat(paste("<html><head></head><body>",<br />
"<h1>Best Dashborde!!!1!</h1>",sep=""),<br />
ObsRep$html$header,<br />
ObsRep$html$chart,<br />
"</body></html>",<br />
file="AnimatedKPIdashboard.html")<br />
browseURL("AnimatedKPIdashboard.html")`

And voilà! Here&#8217;s our KPI with a flashing red light for the real underperformers:

<!-- iframe plugin v.4.3 wordpress.org/plugins/iframe/ -->

(The link also here: >><a href="https://amitkohli.com/wp-content/uploads/2016/02/AnimatedKPIdashboard-1.html" rel="">AnimatedKPIdashboard</a><<)

And from here the sky is the limit! Enjoy re-discovering animated gifs! There&#8217;s a few gems out there.

As always, full code is in my [github account][2].

&nbsp;

(Editing by <a href="http://Www.linkedin.com/laure.belotti" target="_blank">Laure Belotti</a>)

 [1]: https://www.google.com.gh/search?q=KPI+dashboard&prmd=ivns&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwiR_aygzOvKAhWCcRQKHdNjB-MQsAQICg&biw=1278&bih=683&dpr=1&gws_rd=ssl
 [2]: https://github.com/mexindian/KPI