---
title: Clickable list of the best animations since 1900, gathered the geek way.
author: Amit
type: post
date: 2015-10-22T13:51:20+00:00
url: /list-of-the-best-animations-since-1900-gathered-the-geek-way/
categories:
  - Big data
  - Data
  - Movies
  - R
tags:
  - animation
  - cartoon
  - data analysis
  - movie
  - R
  - scraping
  - search engine
  - short film
  - string matching

---
[<img class="alignnone wp-image-420" src="https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/10/images.jpg?resize=138%2C106" alt="images" width="138" height="106" srcset="https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/10/images.jpg?zoom=2&resize=138%2C106 276w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/10/images.jpg?zoom=3&resize=138%2C106 414w" sizes="(max-width: 138px) 100vw, 138px" data-recalc-dims="1" />][1][<img class="alignnone wp-image-423" src="https://i2.wp.com/amitkohli.com/wp-content/uploads/2015/10/2.jpg?resize=137%2C105" alt="2" width="137" height="105" srcset="https://i2.wp.com/amitkohli.com/wp-content/uploads/2015/10/2.jpg?zoom=2&resize=137%2C105 274w, https://i2.wp.com/amitkohli.com/wp-content/uploads/2015/10/2.jpg?zoom=3&resize=137%2C105 411w" sizes="(max-width: 137px) 100vw, 137px" data-recalc-dims="1" /><img class="alignnone wp-image-422" src="https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/10/3.jpg?resize=139%2C104" alt="3" width="139" height="104" srcset="https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/10/3.jpg?zoom=2&resize=139%2C104 278w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/10/3.jpg?zoom=3&resize=139%2C104 417w" sizes="(max-width: 139px) 100vw, 139px" data-recalc-dims="1" /><img class="alignnone wp-image-421" src="https://i2.wp.com/amitkohli.com/wp-content/uploads/2015/10/4.jpg?resize=158%2C105" alt="4" width="158" height="105" data-recalc-dims="1" />][2]

In the midst of our random data exploration, Laure and I started playing around with Hadley&#8217;s movies dataset and noticed that there were a lot of old cartoon animations&#8230; I mean REALLY old. So we got excited and wondered if we could find Youtube links for all these old animations. Indeed we could! Here&#8217;s how we did it. As always, the full analysis <a href="https://github.com/mexindian/Search-engine-scraping-and-stringmatching" target="_blank">is on github</a>.

  1. In R, Load in ggplot2::hadley, which has something like 60 000 movies
  2. Reduce this dataset to animations of only 10 minutes or less and then arrange by year and descending rating, then select only <del>1 best animation per year</del>. Hrm&#8230; actually, select each year&#8217;s 3 best-rated cartoons. You&#8217;ll see why later. This reduced dataset has <300 rows&#8230; much more manageable. Of this, only keep the title and year, you don&#8217;t need the rest.
  3. Now let&#8217;s create a column that will give us good search results&#8230; in order to do that, prepend with cartoon and put the year between parentheses so that each row looks like this: &#8220;Cartoon \&#8221;It&#8217;s the Cat\&#8221; (2004)&#8221; (the backslashes escape the quotes inside the string&#8230; dontworriboutem).
  4. Now feed each one of these lines into bing.com (google/yahoo don&#8217;t let us!) and capture the results using httr::GET()
  5. Now we have the whole webpage with the results inside. We use XPath to try our best to grab only the parts of the webpage that we want, namely the search results. Find the first Youtube hit. It takes a LOT of cleaning to figure out what you need and what needs to be thrown out. From this, grab the title of each search result page and the link (by the way, at this point, we have a shorter list because not every movie has a Youtube link).
  6. Now we have to face the reality that the search result may have given us a Youtube link that wasn&#8217;t the film we wanted. In order to understand whether we did or not, we use a package called _stringdistance._ This measures the difference between the title we were looking for and the title of the Youtube hit we got. Sometimes you look for &#8220;Unsteady Chough, The&#8221; and get back &#8220;The unsteady chorough&#8221;. So for this analysis, I found the _qgram _method to perform best. Unfortunately, sometimes even the string distance alone isn&#8217;t a good predictor. One or two misspellings in a film with 3 letters is a bigger deal than 5 misspellings in a film with 30 letters. Therefore:
  7. Come up with a Percent parameter where you divide the stringdistance() by the number of characters in the title you were looking for. This will give you a good indication of how much error there is per string.
  8. Based on an evaluation of the string distances and percents,  we realized that very few cartoons have good correspondence between the title looked for and the title found.This is why one movie per year doesn&#8217;t work and we had to go back and select the 3 best cartoons.
  9. After analyzing the results carefully, we decided to cut the dataset to only stringdistance() <8 and Perc <100 (although results vary a lot here). This left about a hundred cartoons.
 10. So now that you have good cartoons and their Youtube links, put some html code in front and in back, and use cat() to push it all out into an html file!

### Final thoughts

  * We tried to find the images for each video entice viewers to watch the cartoon, but this was reeeeeally hard to do! All the search engines we found push the images as data or in iframes so we couldn&#8217;t capture the image with GET. We finally gave up 🙁
  * We could have probably found  more hits if we had looked at more movie sites than youtube, but we didn&#8217;t like the idea of going to whatever site&#8230; who knows what ads they might have popup or whatever.
  * It&#8217;s lots of fun to see how cartoons have changed through the ages! It&#8217;s amazing to see what they could already do in 1922 and how quickly cartoons improved over time! Click around and see for yourself!
  * Some of the early attempts were full of errors, but in a way it feels a bit psychedelic to click on these links&#8230; it&#8217;s Youtube roulette! I dare you! Click around <a href="https://htmlpreview.github.io/?https://github.com/mexindian/Search-engine-scraping-and-stringmatching/blob/master/Try%201.html" target="_blank">>>here<<</a>.

<p style="text-align: center;">
  <a href="https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/10/5.jpg"><img class="alignnone size-full wp-image-425" src="https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/10/5.jpg?resize=262%2C192" alt="5" width="262" height="192" data-recalc-dims="1" /></a>
</p>

# RESULTS HERE BELOW! Click to go to the youtube link!

&nbsp;

1906 &#8211; <a href="http://youtube.com/watch?v=bc0JTTZOk9U" target="_blank">Humorous Phases of Funny Faces</a>

1911 &#8211; <a href="http://youtube.com/watch?v=2f8tfSHIU_g" target="_blank">Little Nemo</a>

1916 &#8211; <a href="http://youtube.com/watch?v=HfQgxx3AbbE" target="_blank">R.F.D. 10,000 B.C.</a>

1916 &#8211; <a href="http://youtube.com/watch?v=7ESzUkmCiIA" target="_blank">Krazy Kat, Bugologist</a>

1919 &#8211; <a href="http://youtube.com/watch?v=fsRullIZs9M" target="_blank">Feline Follies</a>

1922 &#8211; <a href="http://youtube.com/watch?v=9DDZ1RoZphw" target="_blank">Puss in Boots</a>

1925 &#8211; <a href="http://youtube.com/watch?v=kLwPQIEdjzU" target="_blank">Alice&#8217;s Egg Plant</a>

1928 &#8211; <a href="http://youtube.com/watch?v=v9_QLy0ronc" target="_blank">Vormittagsspuk</a>

1929 &#8211; <a href="http://youtube.com/watch?v=POQKQqfC8hM" target="_blank">Springtime</a>

1931 &#8211; <a href="http://youtube.com/watch?v=RFrBG4xyaF8" target="_blank">Bimbo&#8217;s Initiation</a>

1932 &#8211; <a href="http://youtube.com/watch?v=Jkh5ojRXKYM" target="_blank">Flowers and Trees</a>

1933 &#8211; <a href="http://youtube.com/watch?v=KRhIas55fG8" target="_blank">Une nuit sur le mont chauve</a>

1933 &#8211; <a href="http://youtube.com/watch?v=leAh00n3hno" target="_blank">Three Little Pigs</a>

1934 &#8211; <a href="http://youtube.com/watch?v=tV477L8cCII" target="_blank">Tale of the Vienna Woods</a>

1934 &#8211; <a href="http://youtube.com/watch?v=cuHQMNieCMo" target="_blank">China Shop, The</a>

1935 &#8211; <a href="http://youtube.com/watch?v=Zdt0IbZBIJM" target="_blank">Three Orphan Kittens</a>

1937 &#8211; <a href="http://youtube.com/watch?v=1iaOlMcJvyU" target="_blank">Lonesome Ghosts</a>

1938 &#8211; <a href="http://youtube.com/watch?v=Nn1-_jV-UZE" target="_blank">Porky in Wackyland</a>

1939 &#8211; <a href="http://youtube.com/watch?v=d8stkqssLYc" target="_blank">Peace on Earth</a>

1939 &#8211; <a href="http://youtube.com/playlist?list=PLdKgz3pUUR5DJVIJAaIHueemHAtiNmPAk" target="_blank">Blue Danube, The</a>

1941 &#8211; <a href="http://youtube.com/watch?v=XWpYaY5N-Mk" target="_blank">Dance of the Weed</a>

1941 &#8211; <a href="http://youtube.com/watch?v=ZL9_PDfzDqg" target="_blank">Fox and the Grapes, The</a>

1942 &#8211; <a href="http://youtube.com/watch?v=RF2mTYf3BRI" target="_blank">Horton Hatches the Egg</a>

1943 &#8211; <a href="http://youtube.com/watch?v=yJutO3D_EF8" target="_blank">Fighting Tools</a>

1943 &#8211; <a href="http://youtube.com/watch?v=XrW4R8CSQMc" target="_blank">Red Hot Riding Hood</a>

1947 &#8211; <a href="http://youtube.com/watch?v=NRrrRMkcGcE" target="_blank">Tubby the Tuba</a>

1948 &#8211; <a href="http://youtube.com/watch?v=fkNkKDaizQ4" target="_blank">Cat That Hated People, The</a>

1948 &#8211; <a href="http://youtube.com/watch?v=WTPA0BSil_4" target="_blank">Mouse Wreckers</a>

1950 &#8211; <a href="http://youtube.com/watch?v=dXS_L54CFxE" target="_blank">Morris the Midget Moose</a>

1950 &#8211; <a href="http://youtube.com/watch?v=qvwzlUeJAG8" target="_blank">Ventriloquist Cat</a>

1951 &#8211; <a href="http://youtube.com/watch?v=J0jA89ro48w" target="_blank">Dude Duck</a>

1951 &#8211; <a href="http://youtube.com/watch?v=ZlE9U41gAIc" target="_blank">Symphony in Slang</a>

1952 &#8211; <a href="http://youtube.com/watch?v=1bTGIU7FT0E" target="_blank">Rock-a-Bye Bear</a>

1955 &#8211; <a href="http://youtube.com/watch?v=Kxcy6uMVH74" target="_blank">You and Your Senses of Smell and Taste</a>

1959 &#8211; <a href="http://youtube.com/watch?v=3bqzgWkEsws" target="_blank">Short and Suite</a>

1960 &#8211; <a href="http://youtube.com/watch?v=CuMI4lMk_-s" target="_blank">High Note</a>

1962 &#8211; <a href="http://youtube.com/watch?v=dmYim499bDY" target="_blank">Self Defense&#8230; for Cowards</a>

1962 &#8211; <a href="http://youtube.com/watch?v=NCh6Ssf1geo" target="_blank">Now Hear This</a>

1965 &#8211; <a href="http://youtube.com/watch?hl=en&v=xQqSpcmHkkM" target="_blank">Go Go Amigo</a>

1967 &#8211; <a href="http://youtube.com/watch?v=cq0a5JTSGvU" target="_blank">Bear That Wasn&#8217;t, The</a>

1968 &#8211; <a href="http://youtube.com/watch?v=cit6iUEEdyo" target="_blank">Windy Day</a>

1969 &#8211; <a href="http://youtube.com/watch?v=xbdYemPph_Q" target="_blank">Corbeau et le renard, Le</a>

1969 &#8211; <a href="http://youtube.com/watch?v=C1XgGb9q71E" target="_blank">Bambi Meets Godzilla</a>

1970 &#8211; <a href="http://youtube.com/watch?v=LbWCjQ5L0ZY" target="_blank">Is It Always Right to Be Right?</a>

1971 &#8211; <a href="http://youtube.com/watch?v=CebRfSFnWGM" target="_blank">Thank You Mask Man</a>

1972 &#8211; <a href="http://youtube.com/watch?v=p5bF0tKwAVU" target="_blank">Balablok</a>

1978 &#8211; <a href="http://youtube.com/watch?v=GfMt-RTLhpA" target="_blank">Afterlife</a>

1978 &#8211; <a href="http://youtube.com/watch?v=IaFi3DCHjak" target="_blank">Special Delivery</a>

1979 &#8211; <a href="http://youtube.com/watch?v=1B3VMlK7DkA" target="_blank">Harpya</a>

1979 &#8211; <a href="http://youtube.com/watch?v=upsZZ2s3xv8" target="_blank">Canada Vignettes: Log Driver&#8217;s Waltz</a>

1979 &#8211; <a href="http://youtube.com/watch?v=6bevAfTcj20" target="_blank">Every Child</a>

1985 &#8211; <a href="http://youtube.com/watch?v=ZqIwpT-kcGo" target="_blank">Broken Down Film</a>

1985 &#8211; <a href="http://youtube.com/watch?v=UtedQz5mnQM" target="_blank">Concerto Grosso Modo</a>

1986 &#8211; <a href="http://youtube.com/watch?v=gzAyrlXTfQ8" target="_blank">Luxo Jr.</a>

1988 &#8211; <a href="http://youtube.com/watch?v=bETCusT5kNM" target="_blank">Cat Came Back, The</a>

1995 &#8211; <a href="http://youtube.com/watch?v=7H1HYYKplBE" target="_blank">Life of Larry, The</a>

1995 &#8211; <a href="http://youtube.com/watch?v=vkTauJqPfJQ" target="_blank">Chicken from Outer Space, The</a>

1999 &#8211; <a href="http://youtube.com/watch?v=51_tXkwgLqs" target="_blank">Pinocchio</a>

 [1]: https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/10/images.jpg
 [2]: https://i2.wp.com/amitkohli.com/wp-content/uploads/2015/10/4.jpg