---
title: Heart-shaped wordcloud, celebrating Colombia peace treaty
author: Amit
type: post
date: 2016-09-27T03:53:07+00:00
url: /heart-shaped-wordcloud-celebrating-colombia-peace-treaty/
arcade_basic_custom_image:
  - https://amitkohli.com/wp-content/uploads/2016/09/colombia.png
categories:
  - Big data
  - Data
  - R
tags:
  - colombia
  - paz
  - peace
  - wordcloud
  - wordcloud2

---
This is a lightening quick post just providing the script to draw a heart-shaped wordcloud, using the awesome [This is a lightening quick post just providing the script to draw a heart-shaped wordcloud, using the awesome][1] package. See the resulting image here:

<img class="alignnone size-medium wp-image-695" src="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/09/colombia.png?resize=300%2C192" alt="colombia" width="300" height="192" srcset="https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/09/colombia.png?resize=300%2C192 300w, https://i2.wp.com/amitkohli.com/wp-content/uploads/2016/09/colombia.png?w=571 571w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" />

&nbsp;

Apparently, the original code allows you to fit a wordcloud to any shape, [even custom shapes][2], but I didn&#8217;t find that functionality pushed out into R yet (a peace sign would have been awesome in this case).

In any event, here&#8217;s the code to accomplish this chart. Sorry for the very very short post, I&#8217;m working on something big! Stay tuned!

`</p>
<pre>
########################################################################
## Title: Draw heart-shaped wordcloud
## Date: 2016-09-26
########################################################################

## Load libraries
library(twitteR)
library(dplyr)
library(httr)
library(rvest)
library(wordcloud2) # devtools::install_github("lchiffon/wordcloud2")

## SETUP (you need to authenticate on twitter... put in your secret codes here)

setup_twitter_oauth("secret1", "secret2")


## THING TO LOOK FOR

topik<-"#PazEnColombia"

S1 = searchTwitteR(topik, n = 10000)

## Convert text df

S.df = do.call("rbind", lapply(S1, as.data.frame))

## Get only text and convert to lower

b <- unlist(strsplit(S.df$text," "))

b <- tolower(b)

## Get list of spanish stopwords
sw <- read_html("http://www.ranks.nl/stopwords/spanish")

sw <- html_nodes(sw,"td")

sw <- unlist(strsplit(html_text(sw)," "))

## add a few more stopwords and "RT", and eliminate ":"

sw <- c(sw,"de","la","rt","en","las","para","por","con","que","a","y")

sw <- gsub(":","",sw)

## 'niceify'

stopWords <- data.frame(word = sw)

table(b) %>% as.data.frame -> c

names(c) <- c("word","freq")

## Remove stopwords via anti_join, and infrequent matches

d <- anti_join(x = c,y=stopWords) %>%

arrange(desc(freq)) %>% filter(freq>2)

## Plot!

wordcloud2(d, size = 2,shape = 'cardioid')
</pre>
<p>`

 [1]: https://github.com/lchiffon/wordcloud2
 [2]: https://timdream.org/wordcloud2.js/#love