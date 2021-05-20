---
title: Make dashboard Tiles/Notecards in R
author: Amit
type: post
date: 2016-02-25T19:47:39+00:00
url: /make-dashboard-tilesnotecards-in-r/
switch_like_status:
  - 1
categories:
  - Data
  - R
  - Tutorials
  - Visualizations
tags:
  - Bootstrap
  - Dashboard
  - html
  - Tile

---
# Update!!

_Due to the popularity of this script, I released it as a package. To install it, use:_ 

<pre>devtools::install_github("datastrategist/TileMaker")
</pre>

&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;
  


Dashboard Tiles/Notecards are a great way to visualize just one number, and make it big and pretty. They can emphasize results in an easily digestible and colourful format. I was surprised that there was no way to create tiles offline (there is however a very good online version in [shinydashboards][1]), so i made one.

I wanted something that would look pretty, but also be flexible. Hrm&#8230; if only there was a flexible tool that made pretty webpages&#8230; Of course I&#8217;m talking about the ever-awesome [Bootstrap!][2]  In case you&#8217;ve been living under a rock and don&#8217;t know what that is, it&#8217;s the most popular framework for developing AWESOME mobile-friendly webpages around. Think of it as &#8220;webpage lego&#8221;, only when you&#8217;re done, things actually _look good_.

All I needed to do was figure out how to get data from R, select what features to include (ranging from a base template to link-enabled multi-sized buttons that change color based on values) and stuff all of it into a webpage enriched by Bootstrap&#8217;s CSS tags, and boom! This is what I got (full code to produce this example below):

<!-- iframe plugin v.4.3 wordpress.org/plugins/iframe/ -->

&#8230;which is suitable for any dashboard you choose!

Also, because it&#8217;s a webpage, it&#8217;s got that nice mouse-over highlighting effect (yes, it&#8217;ll do tooltips too). All you have to do is source the R file [from the github repo][3], or   <!-- iframe plugin v.4.3 wordpress.org/plugins/iframe/ --> your own version.

I allowed for many settings to be passed from R, check the Repo readme for an explanation&#8230; but in the meantime, let&#8217;s see how we did that example above:

Let&#8217;s say that I want to create a dashboard that showcases five buttons: one row of three buttons, and a second row with two buttons. I want to give them some icons and I want the top 3 to change color depending on the value that&#8217;s being passed to them. To accomplish this, we could do:

<pre>## your very important calcs will end up with the following data, for example
Value1 = 88
Value2 = 1985
Value3 = 1.22
Value4 = 30
Value5 = 42
## Install the package, and call the library
devtools::install_github("datastrategist/TileMaker")
library(TileMaker)
## Make the buttons how you like
Button1 &lt;- ButtonMaker(Value = Value1,
 Subtitle = "Speed",
 Units="mph",
 Target=88,
 ThresholdHigh=80,
 ThresholdLow=70, 
 Icon="glyphicon glyphicon-road")
Button2 &lt;- ButtonMaker(Color = 4,Value = Value2,
 Subtitle = "Origin", 
 Target=2015,
 ThresholdHigh=99,
 ThresholdLow=40, 
 Icon="glyphicon glyphicon-share-alt")
Button3 &lt;- ButtonMaker(Value = Value3, 
 Subtitle = "Powah",
 Units="GW", 
 Target=5,
 ThresholdHigh=4,
 ThresholdLow=3, 
 Hover="Great Scott!",
 Icon="glyphicon glyphicon-signal")
Button4 &lt;- ButtonMaker(Color = 4,
 Value = Value4,
 Subtitle = "Heads turned",
 Units="K", 
 Icon="glyphicon glyphicon-user")
Button5 &lt;- ButtonMaker(Color = 5,
 Value = Value5,
 Subtitle = "Answer",
 Hover="Whales rule. Petunias suck",
 Link="https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy",
 Icon="glyphicon glyphicon-thumbs-up")
## Combine in 2 rows:
Div1 &lt;- DivMaker(Title = "Doing Homework",Buttons = paste(Button1,Button2,Button3))
Div2 &lt;- DivMaker(Title = "Effect",Buttons = paste(Button4,Button5))
## Now put them all together:
TileMaker(Divs = paste(Div1,Div2),FileName = "buttons.html")
## and win!
browseURL("buttons.html")</pre>



This is just the beginning. This method can be pretty powerful... for example, doing the same thing with [Bootcards][4], or with Bootstap v.4 coming up... the [Statcards][5] look AWESOME (I would use that, but **a)** I don't want to use code that's still in alpha, and **b)** I'm not sure if it's cool to take code from a paid template... could someone tell me please?).

For anyone out there willing to add functionality, I'm welcoming pull-requests from one and all!

&nbsp;

_Edited by: [# Update!!

_Due to the popularity of this script, I released it as a package. To install it, use:_ 

<pre>devtools::install_github("datastrategist/TileMaker")
</pre>

&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;
  


Dashboard Tiles/Notecards are a great way to visualize just one number, and make it big and pretty. They can emphasize results in an easily digestible and colourful format. I was surprised that there was no way to create tiles offline (there is however a very good online version in [shinydashboards][1]), so i made one.

I wanted something that would look pretty, but also be flexible. Hrm&#8230; if only there was a flexible tool that made pretty webpages&#8230; Of course I&#8217;m talking about the ever-awesome [Bootstrap!][2]  In case you&#8217;ve been living under a rock and don&#8217;t know what that is, it&#8217;s the most popular framework for developing AWESOME mobile-friendly webpages around. Think of it as &#8220;webpage lego&#8221;, only when you&#8217;re done, things actually _look good_.

All I needed to do was figure out how to get data from R, select what features to include (ranging from a base template to link-enabled multi-sized buttons that change color based on values) and stuff all of it into a webpage enriched by Bootstrap&#8217;s CSS tags, and boom! This is what I got (full code to produce this example below):

<!-- iframe plugin v.4.3 wordpress.org/plugins/iframe/ -->

&#8230;which is suitable for any dashboard you choose!

Also, because it&#8217;s a webpage, it&#8217;s got that nice mouse-over highlighting effect (yes, it&#8217;ll do tooltips too). All you have to do is source the R file [from the github repo][3], or   <!-- iframe plugin v.4.3 wordpress.org/plugins/iframe/ --> your own version.

I allowed for many settings to be passed from R, check the Repo readme for an explanation&#8230; but in the meantime, let&#8217;s see how we did that example above:

Let&#8217;s say that I want to create a dashboard that showcases five buttons: one row of three buttons, and a second row with two buttons. I want to give them some icons and I want the top 3 to change color depending on the value that&#8217;s being passed to them. To accomplish this, we could do:

<pre>## your very important calcs will end up with the following data, for example
Value1 = 88
Value2 = 1985
Value3 = 1.22
Value4 = 30
Value5 = 42
## Install the package, and call the library
devtools::install_github("datastrategist/TileMaker")
library(TileMaker)
## Make the buttons how you like
Button1 &lt;- ButtonMaker(Value = Value1,
 Subtitle = "Speed",
 Units="mph",
 Target=88,
 ThresholdHigh=80,
 ThresholdLow=70, 
 Icon="glyphicon glyphicon-road")
Button2 &lt;- ButtonMaker(Color = 4,Value = Value2,
 Subtitle = "Origin", 
 Target=2015,
 ThresholdHigh=99,
 ThresholdLow=40, 
 Icon="glyphicon glyphicon-share-alt")
Button3 &lt;- ButtonMaker(Value = Value3, 
 Subtitle = "Powah",
 Units="GW", 
 Target=5,
 ThresholdHigh=4,
 ThresholdLow=3, 
 Hover="Great Scott!",
 Icon="glyphicon glyphicon-signal")
Button4 &lt;- ButtonMaker(Color = 4,
 Value = Value4,
 Subtitle = "Heads turned",
 Units="K", 
 Icon="glyphicon glyphicon-user")
Button5 &lt;- ButtonMaker(Color = 5,
 Value = Value5,
 Subtitle = "Answer",
 Hover="Whales rule. Petunias suck",
 Link="https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy",
 Icon="glyphicon glyphicon-thumbs-up")
## Combine in 2 rows:
Div1 &lt;- DivMaker(Title = "Doing Homework",Buttons = paste(Button1,Button2,Button3))
Div2 &lt;- DivMaker(Title = "Effect",Buttons = paste(Button4,Button5))
## Now put them all together:
TileMaker(Divs = paste(Div1,Div2),FileName = "buttons.html")
## and win!
browseURL("buttons.html")</pre>



This is just the beginning. This method can be pretty powerful... for example, doing the same thing with [Bootcards][4], or with Bootstap v.4 coming up... the [Statcards][5] look AWESOME (I would use that, but **a)** I don't want to use code that's still in alpha, and **b)** I'm not sure if it's cool to take code from a paid template... could someone tell me please?).

For anyone out there willing to add functionality, I'm welcoming pull-requests from one and all!

&nbsp;

_Edited by:][6] . Just a quick note, she has been editing my blog forever, and has finally set up shop in Upwork. Go hire her!_

 [1]: https://rstudio.github.io/shinydashboard/
 [2]: http://getbootstrap.com/
 [3]: https://github.com/datastrategist/TileMaker
 [4]: http://demo.bootcards.org/dashboard
 [5]: http://themes.getbootstrap.com/products/dashboard
 [6]: https://www.upwork.com/freelancers/~0110aec48fff897b57