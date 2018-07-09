---
title: Announcing ShinyTester – a package that helps you build Shiny apps
author: Amit
type: post
date: 2017-02-01T17:16:57+00:00
url: /announcing-shinytester-a-package-that-helps-you-build-shiny-apps/
categories:
  - Data
  - R
  - Shiny
tags:
  - helper
  - hierarchy
  - shiny
  - syntax

---
Shiny is awesome, but can be a bit daunting and easy to make mistakes in. I recently came back to Shiny after a hiatus of a few years and it was much more challenging than I feel comfortable admitting. I was making bonehead mistakes like writing `something` instead of `output$something`, confusing where to put `Output` commands vs `Render` commands, etc. I would eventually find my mistake, curse myself and move on with a crumpled ego. Then I had the realization that maybe if I was a beginner, I wouldn&#8217;t even know what I was doing wrong. Thusly did I conclude that I was in a unique position to help out the R community: Dumb enough to make mistakes, but experienced enough to eventually remember how to resolve them. So naturally, I wrote an R package that tests the code of the Shiny app itself.

&nbsp;

To install: `install.packages("ShinyTester")` cause yes, it&#8217;s on CRAN (my first!!! Shoutout to [@jbkunst][1] for invaluable help!)

&nbsp;

**Quick caveat**: Since this package parses code and everyone writes code differently, it will necessarily be super buggy. If this package doesn&#8217;t work for your app (after reading the full list of caveats at the bottom of this post), please help by [opening an Issue on the github repo][2].

&nbsp;

The package consists of two functions that analyze the code itself:

  * `ShinyDummyCheck()` &#8211; checks how items are created in `server.R` and then how they are called in `ui.R` and runs some fairly naive checks
  * `ShinyHierarchy()` &#8211; to create an _ad hoc_ hirearchy of the structure of the Shiny Apps &#8211; ie &#8211; what inputs go to what reactives, what reactives go to other reactives, and what then gets pushed back out to the UI as an output.

It is my hope that both of these combined minimize the intrinsic boneheadedness in us all. This is really quite beta though&#8230; please do check the Caveats! In the meantime, some examples:

### Examples for `ShinyDummyCheck`:

    ShinyTester::ShinyDummyCheck("https://raw.githubusercontent.com/mexindian/ShinyServer/master/LineSelector")
    

Provides this table:

&nbsp;

[<img class="alignnone size-medium wp-image-728" src="https://i1.wp.com/amitkohli.com/wp-content/uploads/2017/02/shinyDummyCheck.png?resize=300%2C139" alt="" width="300" height="139" srcset="https://i1.wp.com/amitkohli.com/wp-content/uploads/2017/02/shinyDummyCheck.png?resize=300%2C139 300w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2017/02/shinyDummyCheck.png?w=467 467w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" />][3]

Which shows that there are no errors in the Shiny app, oh except for the fact that I defined an object twice&#8230; whoops (Yeah, see that&#8217;s exactly the boneheadedness I&#8217;m talkin bout). The structure of the table is as follows:

&nbsp;

  * Item &#8211; The name of the asset that maybe should be on both server.R and ui.R
  * SrvCall &#8211; the TYPE of object that you&#8217;re saying this specific item is (in server.R)
  * isOutput &#8211; is a binary that will specify if in server.R you wrote just `item` or `output$item`
  * VisualCall &#8211; is the TYPE of thingie you&#8217;re trying to push the item into (in ui.R).
  * Status &#8211; Compares the SrvCall to the VisualCall, also looks at isOutput and then applies some rules to figure out if it&#8217;s probably ok or not

### Examples for `ShinyHierarchy`:

A simple example:

    library(ShinyTester)
    ShinyHierarchy("https://raw.githubusercontent.com/rstudio/shiny-examples/master/003-reactivity")
    

Will yield:

<a href="https://i1.wp.com/cloud.githubusercontent.com/assets/8094091/21746544/7830f6b2-d50e-11e6-8583-c90670786adc.png?ssl=1" target="_blank"><img src="https://i1.wp.com/cloud.githubusercontent.com/assets/8094091/21746544/7830f6b2-d50e-11e6-8583-c90670786adc.png?w=750&#038;ssl=1" alt="image" data-recalc-dims="1" /></a>

&nbsp;

Which shows one of the weaknesses of the function&#8230; it assumes all Item names are unique&#8230; and will act strangely if this assumption doesn&#8217;t hold (ie &#8211; caption).

&nbsp;

A more complex example:

    ShinyTester::ShinyHierarchy("https://raw.githubusercontent.com/mexindian/ShinyServer/master/LineSelector")
    

Yields:

<a href="https://i1.wp.com/cloud.githubusercontent.com/assets/8094091/21746698/169dcdc0-d514-11e6-88ed-357d37293b65.png?ssl=1" target="_blank"><img src="https://i1.wp.com/cloud.githubusercontent.com/assets/8094091/21746698/169dcdc0-d514-11e6-88ed-357d37293b65.png?w=750&#038;ssl=1" alt="image" data-recalc-dims="1" /></a>

And here we can start to see the structure that I&#8217;m attempting to show&#8230; there are basically three ROWS of nodes. The first one is the UI Inputs, the second row are the reactives (kinda&#8230;), and the third row are the outputs being visualized. I said the reactives are &#8220;kinda&#8221; the second row because I have introduced a small shift to each node in the middle row in order to see reactive flows into each other (if they are all in the same row, you can&#8217;t really see them). The structure is made evident in a more complex case below (forgive the redacted names):

<a href="https://i0.wp.com/cloud.githubusercontent.com/assets/8094091/21746742/67a21a86-d515-11e6-96d4-5456b54a7747.png?ssl=1" target="_blank"><img src="https://i0.wp.com/cloud.githubusercontent.com/assets/8094091/21746742/67a21a86-d515-11e6-96d4-5456b54a7747.png?w=750&#038;ssl=1" alt="image" data-recalc-dims="1" /></a>

If you want to suppress the shift in reactive nodes, use `offsetReactives = F`

### Caveats:

This is a very naive app, and in early stages at that&#8230; it works best with my style of programming and will probably take significant work to universalize (since we&#8217;re talking about code&#8230; maybe it&#8217;s impossible to fully universalize).  Some other caveats:

  * For now only works with `<-` assignments, not `=` or `->` assignments
  * <del>For now calling items only works with doublequotes. (ie. <code>plotOutput("thingie")</code> works, <code>plotOutput('thingie')</code> doesn&#8217;t.</del>
  * For now, only supports seperate ui.R and server.R Shiny apps&#8230; the single `app.R` implementation is not supported.
  * `isolate` and `observe` are not supported yet
  * For now, I don&#8217;t read in data outside the shinyserver call (for example, if I want to pass data in that only needs to be calculated once. Not sure yet what&#8217;s the best way.
  * For now it only analyzes the main scripts, if you are SOURCEing files in from other places, it won&#8217;t work.

### Other tips for working in Shiny:

  * Add to your server.R and ui.R TEST items. for example, add one for a data.frame and one for a figure. You can keep these commented out or displaying random data&#8230; then, when you add a new element, just test them in the test blocks before adding them to the exact place. Saves time.
  * Likewise, during testing, if you need to run through the code to debug, you can always simulate inputs by writing this: `input <- data.frame(Parameter1="thingie1",Parameter2="thingie2")`. Keep this commented out, but when you test, you can run through the Shiny app as if it were live.
  * Check Dean Attali&#8217;s excellent tips and tricks (<http://deanattali.com/blog/advanced-shiny-tips/>).

&nbsp;

Enjoy!

(Thanks to my [rusers community][4], especially to [Joshua Kunst][1] and [Colin Phillips][5] for discussion, help and encouragement required to push this through to CRAN).

 [1]: http://jkunst.com
 [2]: https://github.com/mexindian/ShinyTester/issues
 [3]: https://i1.wp.com/amitkohli.com/wp-content/uploads/2017/02/shinyDummyCheck.png
 [4]: http://rusers.co
 [5]: http://www.pivotsciences.com