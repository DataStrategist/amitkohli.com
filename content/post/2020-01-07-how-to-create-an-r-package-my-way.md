---
title: How to create an R package, my way
author: amit
date: '2020-01-07'
slug: how-to-create-an-r-package-my-way
categories:
  - Data
  - Tutorials
tags:
  - package
  - library
  - R
description: ''

draft: yes
---

creates packages their own way... but here's a conclusive guide of the steps I follow. I'll be coming back to this frequently, so watch this space.


## Do once stuff: 
   - Download R and Rstudio, but you should alreay know that :)
   - Download git and set it up w/ your name and email:
     - `git config --global user.email "you@example.com"`
     - `git config --global user.name "Your Name"` 
   - Download Rtools by going here: `https://cran.rstudio.com/bin/windows/Rtools/Rtools35.exe`

OK, now you're ready for the rest:

## OK, let's create a new package!:

   - Create new project, new R package, and make sure to enable git!
  [](/post/2020-01-07-how-to-create-an-r-package-my-way_files/package1.png)
  [](/post/2020-01-07-how-to-create-an-r-package-my-way_files/package2.png)
  [](/post/2020-01-07-how-to-create-an-r-package-my-way_files/package3.png)
  
   - delete hello.R from the /R folder
   - delete hello.Rd from the /man folder (the documentation)
   - Modify the DESCRIPTION file to say what this package is and how to use it. Add in all the details you want (for author use this format: `person("First", "Last", email = "first.last@example.com",role = c("aut", "cre")))`. "aut" means "author", and "cre" means "creator".
   - next, we'll be engaging easymode using usethis. So first call `library(usethis)`
   - `use_testthat()` I like using test-fist, so let's set that up. I'll add in more stuff about testing later.
   - `use_readme_rmd()` to make it easy to make an easy frontpage for your package's website AND a front-page to the github repo. Saving time for the win!
   - `usethis::use_lifecycle_badge(stage = "Experimental")` to show that this is a brand new package. Eventually you'll be moving to "Maturing" or "Stable". Copy the markdown into your README.Rmd
   - `use_cran_badge()` to show how if you're on CRAN or not. Like above, Copy the markdown into your README.Rmd.
   - OK, you're finally ready to start working on your package! Create a new file in the `/R` folder and write or copypaste your functions in.
   - (in case you are starting from a tangled mess of functions + function_running_code, maybe `sinew::untangle` and `sinew::pretty_namespace` can be really useful. See below for sinew link).
   - Now documentation. Make sure you've installed [sinew](https://github.com/metrumresearchgroup/sinew). To do it, run entire function, then doubleclick your title and run `sinew`'s `createOxygen` addin. It will automatically add all the guts required for documentation. In order to save time, it's better to use explicit package::function notation at least once per function, as this will be picked up by sinew and will automatically add in `@importFrom` blocks.
   - Ok, presumably, you've added some dependencies to other packages as mentioned above. Next step is to make sure that the `DESCRIPTION` file knows about this. So go to that file and put the package name under a new `Imports:` section. The function `sinew::makeImport` does this, but it's a bit buggy, so just keep an eye out.
   - Under the build menu, go to `more` and `Configure Build tools` to build documentation each time every time you Install and Restart. This way you don't have to ever think of it again. Eventually if you have tons of documentation you might want to remove that.
   - Add a license. Depending on your needs, `usethis` has a variety of functions to help you with that.
   - You're done! Keep adding tests, code, and to verify all is good, run `devtools::check()`. Rinse and repeat till you're done! (or more than likely, check below to see what to do when all fails).


https://github.com/mikldk/roxytest


## Quality Control:
   - When trying to CHECK your package: 
     - Make sure to delete "the crap"" every time! When you build, it'll create a .Rcheck folder as well as the `.tar` file. Make sure to delete these everytime you try to `check` your package, as they don't always rebuild, so you might be checking an old version
     - You might see a ton of errors like below, which might be one of two things:
     
     > no visible binding for global variable blah
       
       - you have maybe forgotten to `@importFrom` some functions. Make sure all of these are perfectly done or your package will probably be buggy.
       - you have used tidyverse (to be precise, the NSE portion of it), and it doesn't know that "Species" is `iris$Species`. In order to eliminate this error, evertime you've used `Species` alone, you are going to have to replace it with `.data$Species` AND make sure that you add `@importFrom rlang .data` to the documentation of each function where this is an issue (but this is kinda a major pain and might introduce several bugs, so it might not be worth fixing).
       
## When you're kinda finished:
   - `use_pkgdown()` to have a nice website for your package. Ignore the yml file for now
   - `pkgdown::build_site()` will build the documentation site. Remember to redo this everytime you want to do add text!
   - If you've done everything above, you'll have 3 places to make write stuff: In the documentation for each function's **Roxygen** text, in **`README.Rmd`**, and in the **DESCRIPTION**. Make sure you update these whenever you make changes to the code. 
   - give everything a final check!
   - git commit all. I use "Initial Commit" as a commit message, but it doesn't really matter
   - `use_github(protocol = "https")` to set yourself up in github (CAREFUL, this will make your work public... you might want to consider `private = TRUE` if you want it to be kept private. If it protests about no github auth_token, you'll have to set one up, but the usethis instructions are kinda clear, follow them.
   - OK, you're on github! Last step, make the package website visible. Go into the **repo**'s Settings page (careful to not enter github settings), and under Github Pages, mark the docs folder as the source. This will pop up a URL. Copy it.
   
  [](/post/2020-01-07-how-to-create-an-r-package-my-way_files/package3.png)
  
  - Now go back and click on the Edit butotn on the top right hand side of your your Repo's title, and paste that URL into the Website textbox.

 
## Extra stuff to consider 
 - `use_vignette` if you're building something cool that other people are supposed to use, then you should probably show them HOW to use it. That's what a vignette is for.
 - Travis-CI & Codecov It's super useful but can be tough to set up.  
 

