---
title: "Chord progressions of 5000 songs!"
author: Amit
date: '2015-03-01'
url: /chord-progressions-of-5-000-songs/
tags:
  - Art
  - Big data
  - Data
  - R
  - Analysis
topics:
  - Music
  - Chords
  - Progressions
  - Sankey
  - Western music
---
Update: Full analysis and everything you need at my github <https://github.com/datastrategist/Musical-chord-progressions>

The <a href="http://www.hooktheory.com/trends" target="_blank">Hooktheory.com</a> database contains analyses of over 5000 songs*. These analyses are uploaded by users and allow for all these songs to be analyzed in bulk, as well as individually. One of these &#8216;all song' analyses enables users to gather chord progressions on ALL songs (see the analysis file to see how i did it, using the hooktheory API and R). This allowed us to  create a Sankey [[Visualization]] of all chord progressions in the Hooktheory database.

Check it out!

[<img class="alignnone size-medium wp-image-247" src="https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/02/chord.prog_.sankey.png?resize=288%2C300" alt="chord.prog.sankey" width="288" height="300" srcset="https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/02/chord.prog_.sankey.png?resize=288%2C300 288w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/02/chord.prog_.sankey.png?w=677 677w" sizes="(max-width: 288px) 100vw, 288px" data-recalc-dims="1" />][1]

(If you prefer the dynamic version where you can play with the data, have a look at the following link: <a title="Interactive version" href="https://amitkohli.com/wp-content/uploads/2015/02/InteractiveChordProgression.html" target="_blank">Click here!</a>).

Explaining the figure a little bit: What interests us here is the type of chords used, regardless of the song's scale, so that 1->5->6 in the figure above includes songs in key of C major that have the chord progression C->G->Am and songs in the key of A major that have A->E->F#m (if the songs have the same Roman numerals and are in the same relative major.  In reality, the API blends songs into rough categories regardless of the song's mode, so it's impossible to know for sure what we're dealing with).

The chord progressions start from the left, and continue to the right. So for example, the transition 4->1->5->6 is one of the most popular ones... and is in fact present in 327 songs! <a href="http://www.hooktheory.com/trends#node=4.1.5.6&key=rel" target="_blank">Check em out</a>!

**Methods:**

In the API, chord probabilities are stated as a percent, such that the relative importance of each chord is known at each step (the normalization technique is not known). In their API, there were 29 chords available at the start of all progressions. For every subsequent transition, the number of chord options increases (which is expected), but for the purpose of this [[Visualization]], I only keep the original 29 chords for every transition for graphical purposes (I expect these 29 to be the most common anyway, so it's not that much of a big deal). Also, since the thickness of the lines I'm plotting are in and of themselves probabilities, and the probability that you are on that chord is different, the "total thickness of each transition" isn't the same. Very lazily, I just normalized all probabilities across each transition so that each transition "mega bar" is kind-of the same height. I'm sure there's a better way to do it, the community is invited to improve!

[My analysis is here][2], collaboration and/or remixing with attribution is welcome! (and if you improve the normalization method, please let me know and I'll update this post).

**Caveats:**

  * There are several limitations to this assessment since the Hooktheory  API wasn't really intended for this type of analysis. For example, it doesn't mention whether "6" is "vi" (minor) or "VI" (major), which is kind of a big deal.
  * As mentioned, I selected only 29 chords to track... I might be missing a lot of progressions.
  * I have no idea if the normalization I applied is valid. I stopped trying when the output I got was semi-reasonable.
  * Blending everything together like this probably obscures some interesting patterns
  * I only did chord-progressions that were 4 steps long... I could have gone farther, but didn't want to slam the API too much (as you can imagine, the number of queries increases drastically for each &#8216;step'. The Start -> First step was 1 query that yielded 29 chords, the 2->3 transition was 29 results for each of the 29 chords from step1 (so 29^2 queries), the 3->4 transition was 29^3 queries and so on) .
  * The songs have been uploaded by users from around the world, but represent mostly Western music. It would be awesome to do this with music from other parts of the world.

**Possible Legend (thanks to HertzDevil):**

The numbers are as they are represented in the Trends search string, here in EBNF metasyntax:

(\* Roman numerals \*)
  
numeral = "1" | "2" | "3" | "4" | "5" | "6" | "7";
  
(\* Borrowed modes, from Dorian to Locrian \*)
  
mode = "D" | "Y" | "L" | "M" | "b" | "C";
  
(\* Figured bass for triadic and seventh chords \*)
  
inversion = "6" | "64" | "7" | "65" | "43" | "42";
  
(\* Functions available for applied chords \*)
  
function = "4" | "5" | "7";
  
(\* Basic chords or borrowed chords in the relative Major key \*)
  
simple-chord = [mode], numeral, [inversion];
  
(\* Applied chords \*)
  
applied-chord = function, [inversion], "/", numeral;
  
(\* Chord progressions for both the Trends page and the API \*)
  
chord = simple-chord | applied-chord;
  
trends-progression = chord, {".", chord};
  
api-progression = chord, {",", chord};

**Parting thoughts:**

  * Even though there is a great variety of chords and chord progressions, progressions involving 1,4,5, and 6 are favoured, probably because they &#8216;sound good' to our brain. Nowhere is this better illustrated than by [Axis of Evil's song "4 Four Chord Song"][3]. I definitely expected chord 1 to be used frequently, but I was expecting more variability.
  * Music is pretty to look at!
  * If you're a musician, try weird progressions! I know that what sounds good sounds good, but jeez... how will humanity ever learn to be creative if everyone keeps doing the same thing over and over?

&nbsp;

_(thanks to <a href="https://www.linkedin.com/profile/view?id=59744871" target="_blank">Laure Belotti</a> for editorial prowess)_

&nbsp;

EDIT: I've been getting great feedback on this post. Please check out the great conversations][4] and [here][5]. Giving credit where it's due, turns out Axis of Evil wasn't the first to talk about Chord-progression overusage, check out [this dude][6]. More credit where it's due, turns out I wasn't the first one [to come up with this idea][7] (great minds indeed...). And finally, I'm sure you nerds all checked out hooktheory, but take a look at these][8] resources [also][9]!

&nbsp;

*EDIT2: Originally I was under the impression that the hooktheory database contained over 25000 songs... but a hooktheory admin clarified that in fact there's just over 5000.

 [1]: https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/02/chord.prog_.sankey.png
 [2]: https://github.com/datastrategist/Musical-chord-progressions
 [3]: https://www.youtube.com/watch?v=5pidokakU4I
 [4]: http://www.[[Reddit]].com/r/dataisbeautiful/comments/32ol86/chord_progressions_of_25_000_songs_oc/
 [5]: https://news.[[YCombinator]].com/item?id=9394176
 [6]: https://www.youtube.com/watch?v=JdxkVQy7QLM
 [7]: http://briancort.com/songviz/
 [8]: http://labrosa.ee.columbia.edu/millionsong/
 [9]: http://yanno.eecs.qmul.ac.uk/