---
title: Chord progressions of 5 000 songs!
author: Amit
type: post
date: 2015-03-01T19:18:54+00:00
url: /chord-progressions-of-5-000-songs/
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
  - Music
  - Chords
  - Progressions
  - Sankey
  - Western music

---
Update: Full analysis and everything you need at my github <https://github.com/mexindian/Musical-chord-progressions>

The <a href="http://www.hooktheory.com/trends" target="_blank">Hooktheory.com</a> database contains analyses of over 5000 songs*. These analyses are uploaded by users and allow for all these songs to be analyzed in bulk, as well as individually. One of these &#8216;all song&#8217; analyses enables users to gather chord progressions on ALL songs (see the analysis file to see how i did it, using the hooktheory API and R). This allowed us to  create a Sankey visualization of all chord progressions in the Hooktheory database.

Check it out!

[<img class="alignnone size-medium wp-image-247" src="https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/02/chord.prog_.sankey.png?resize=288%2C300" alt="chord.prog.sankey" width="288" height="300" srcset="https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/02/chord.prog_.sankey.png?resize=288%2C300 288w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/02/chord.prog_.sankey.png?w=677 677w" sizes="(max-width: 288px) 100vw, 288px" data-recalc-dims="1" />][1]

(If you prefer the dynamic version where you can play with the data, have a look at the following link: <a title="Interactive version" href="https://amitkohli.com/wp-content/uploads/2015/02/InteractiveChordProgression.html" target="_blank">Click here!</a>).

Explaining the figure a little bit: What interests us here is the type of chords used, regardless of the song&#8217;s scale, so that 1->5->6 in the figure above includes songs in key of C major that have the chord progression C->G->Am and songs in the key of A major that have A->E->F#m (if the songs have the same Roman numerals and are in the same relative major.  In reality, the API blends songs into rough categories regardless of the song&#8217;s mode, so it&#8217;s impossible to know for sure what we&#8217;re dealing with).

The chord progressions start from the left, and continue to the right. So for example, the transition 4->1->5->6 is one of the most popular ones&#8230; and is in fact present in 327 songs! <a href="http://www.hooktheory.com/trends#node=4.1.5.6&key=rel" target="_blank">Check em out</a>!

**Methods:**

In the API, chord probabilities are stated as a percent, such that the relative importance of each chord is known at each step (the normalization technique is not known). In their API, there were 29 chords available at the start of all progressions. For every subsequent transition, the number of chord options increases (which is expected), but for the purpose of this visualization, I only keep the original 29 chords for every transition for graphical purposes (I expect these 29 to be the most common anyway, so it&#8217;s not that much of a big deal). Also, since the thickness of the lines I&#8217;m plotting are in and of themselves probabilities, and the probability that you are on that chord is different, the &#8220;total thickness of each transition&#8221; isn&#8217;t the same. Very lazily, I just normalized all probabilities across each transition so that each transition &#8220;mega bar&#8221; is kind-of the same height. I&#8217;m sure there&#8217;s a better way to do it, the community is invited to improve!

[My analysis is here][2], collaboration and/or remixing with attribution is welcome! (and if you improve the normalization method, please let me know and I&#8217;ll update this post).

**Caveats:**

  * There are several limitations to this assessment since the Hooktheory  API wasn&#8217;t really intended for this type of analysis. For example, it doesn&#8217;t mention whether &#8220;6&#8221; is &#8220;vi&#8221; (minor) or &#8220;VI&#8221; (major), which is kind of a big deal.
  * As mentioned, I selected only 29 chords to track&#8230; I might be missing a lot of progressions.
  * I have no idea if the normalization I applied is valid. I stopped trying when the output I got was semi-reasonable.
  * Blending everything together like this probably obscures some interesting patterns
  * I only did chord-progressions that were 4 steps long&#8230; I could have gone farther, but didn&#8217;t want to slam the API too much (as you can imagine, the number of queries increases drastically for each &#8216;step&#8217;. The Start -> First step was 1 query that yielded 29 chords, the 2->3 transition was 29 results for each of the 29 chords from step1 (so 29^2 queries), the 3->4 transition was 29^3 queries and so on) .
  * The songs have been uploaded by users from around the world, but represent mostly Western music. It would be awesome to do this with music from other parts of the world.

**Possible Legend (thanks to HertzDevil):**

The numbers are as they are represented in the Trends search string, here in EBNF metasyntax:

(\* Roman numerals \*)
  
numeral = &#8220;1&#8221; | &#8220;2&#8221; | &#8220;3&#8221; | &#8220;4&#8221; | &#8220;5&#8221; | &#8220;6&#8221; | &#8220;7&#8221;;
  
(\* Borrowed modes, from Dorian to Locrian \*)
  
mode = &#8220;D&#8221; | &#8220;Y&#8221; | &#8220;L&#8221; | &#8220;M&#8221; | &#8220;b&#8221; | &#8220;C&#8221;;
  
(\* Figured bass for triadic and seventh chords \*)
  
inversion = &#8220;6&#8221; | &#8220;64&#8221; | &#8220;7&#8221; | &#8220;65&#8221; | &#8220;43&#8221; | &#8220;42&#8221;;
  
(\* Functions available for applied chords \*)
  
function = &#8220;4&#8221; | &#8220;5&#8221; | &#8220;7&#8221;;
  
(\* Basic chords or borrowed chords in the relative Major key \*)
  
simple-chord = [mode], numeral, [inversion];
  
(\* Applied chords \*)
  
applied-chord = function, [inversion], &#8220;/&#8221;, numeral;
  
(\* Chord progressions for both the Trends page and the API \*)
  
chord = simple-chord | applied-chord;
  
trends-progression = chord, {&#8220;.&#8221;, chord};
  
api-progression = chord, {&#8220;,&#8221;, chord};

**Parting thoughts:**

  * Even though there is a great variety of chords and chord progressions, progressions involving 1,4,5, and 6 are favoured, probably because they &#8216;sound good&#8217; to our brain. Nowhere is this better illustrated than by [Axis of Evil&#8217;s song &#8220;4 Four Chord Song&#8221;][3]. I definitely expected chord 1 to be used frequently, but I was expecting more variability.
  * Music is pretty to look at!
  * If you&#8217;re a musician, try weird progressions! I know that what sounds good sounds good, but jeez&#8230; how will humanity ever learn to be creative if everyone keeps doing the same thing over and over?

&nbsp;

_(thanks to <a href="https://www.linkedin.com/profile/view?id=59744871" target="_blank">Laure Belotti</a> for editorial prowess)_

&nbsp;

EDIT: I&#8217;ve been getting great feedback on this post. Please check out the great conversations][4] and [here][5]. Giving credit where it&#8217;s due, turns out Axis of Evil wasn&#8217;t the first to talk about Chord-progression overusage, check out [this dude][6]. More credit where it&#8217;s due, turns out I wasn&#8217;t the first one [to come up with this idea][7] (great minds indeed&#8230;). And finally, I&#8217;m sure you nerds all checked out hooktheory, but take a look at these][8] resources [also][9]!

&nbsp;

*EDIT2: Originally I was under the impression that the hooktheory database contained over 25000 songs&#8230; but a hooktheory admin clarified that in fact there&#8217;s just over 5000.

 [1]: https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/02/chord.prog_.sankey.png
 [2]: https://github.com/mexindian/Musical-chord-progressions
 [3]: https://www.youtube.com/watch?v=5pidokakU4I
 [4]: http://www.reddit.com/r/dataisbeautiful/comments/32ol86/chord_progressions_of_25_000_songs_oc/
 [5]: https://news.ycombinator.com/item?id=9394176
 [6]: https://www.youtube.com/watch?v=JdxkVQy7QLM
 [7]: http://briancort.com/songviz/
 [8]: http://labrosa.ee.columbia.edu/millionsong/
 [9]: http://yanno.eecs.qmul.ac.uk/