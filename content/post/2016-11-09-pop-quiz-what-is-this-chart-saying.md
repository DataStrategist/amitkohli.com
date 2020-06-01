---
title: Pop quiz! What is this chart saying?
author: Amit
type: post
date: 2016-11-09T01:06:19+00:00
url: /pop-quiz-what-is-this-chart-saying/
categories:
  - Data
  - R
  - Visualizations
  - Analysis
tags:
  - Quiz
  - R
  - Scatter plot
  - Test

---
I have been reading more and more about how people can&#8217;t interpret charts&#8230; which kinda never occurred to me, if I&#8217;m gonna be very honest.  Anyway, it kind of made me think of actually testing people informally, to see for myself. So I&#8217;ve been doing just that: showing colleagues, friends, etc a chart that we created interactively during the [first Accra R-Users session][1] with tons of detail, and asking them to analyze it at length. The results have been staggering! I&#8217;m still trying to generalize my conclusions, but thought it would be fun to open up this test to the community, so here it goes! If you feel like sharing, post your observations in the comments section.

_&#8220;The following chart shows the ratings (imdb) for ~60k movies throughout the years. Movies are divided by their genre (in the case a movie has multiple genres it shows up in all genres), and their budgets are shown in color. All movies are shown as mostly transparent so darker patches mean more movies. Talk for 3 minutes about what this chart is showing, try to explain stuff, and think of what other analysis should follow.&#8221;_

[<img class="alignnone size-medium wp-image-718" src="https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/11/MovieRatingsYearGenreBudget.png?resize=300%2C206" alt="movieratingsyeargenrebudget" width="300" height="206" srcset="https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/11/MovieRatingsYearGenreBudget.png?resize=300%2C206 300w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/11/MovieRatingsYearGenreBudget.png?resize=768%2C528 768w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/11/MovieRatingsYearGenreBudget.png?resize=1024%2C704 1024w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/11/MovieRatingsYearGenreBudget.png?w=1195 1195w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" />][2]

_(click to magnify)_

&nbsp;

The R code to get this chart follows, or you could find the entire exploratory exercise [in the github page][3].

&nbsp;

<pre>library(ggplot2)
library(ggplot2movies)
library(tidyr)
library(dplyr)

## Gather up all ratings into one column, then use that to divide up the movies dataframe and plot
movies %&gt;% 
 select(-(r1:r10)) %&gt;%
 gather(key = genre,val , Action:Short) %&gt;%
 filter(val==1) %&gt;% 
 ggplot(aes(x=year,y=rating,color=budget,label=title))+geom_point(alpha=0.1)+facet_wrap(~genre) + 
 scale_color_gradient(low="red",high="green") +
 ggtitle("Movie ratings by year")

</pre>

 [1]: http://datascience-africa.org/2016/05/first-accra-r-user-meetup-success/
 [2]: https://i0.wp.com/amitkohli.com/wp-content/uploads/2016/11/MovieRatingsYearGenreBudget.png
 [3]: https://github.com/datascience-africa/Accra-R/blob/master/Meeting%201.R