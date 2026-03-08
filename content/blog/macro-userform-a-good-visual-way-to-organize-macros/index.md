---
title: Macro userform ΓÇô a good visual way to organize macros
author: Amit
type: post
date: 2013-02-07T16:22:10+00:00
url: /macro-userform-a-good-visual-way-to-organize-macros/
categories:
  - Excel/VBA
  - Tutorials
tags:
  - Excel
  - Macro
  - Organization
  - Tutorial
  - Userform
  - VBA
  - Visual Basic

---
At a certain point it can become challenging to quickly find and run the macro we need. Below are some options to organize our macros. I will focus on using a┬á**pop-up form**┬ábecause it&#8217;s the method I prefer, but at the bottom of the article, you can see other options.

A pop-up menu looks like this:

[<img title="pop-up example" src="https://macrosforexcel.files.wordpress.com/2012/08/pop-up-example.jpg?resize=497%2C503" alt="" width="497" height="503" data-recalc-dims="1" />][1]

**How to make your own Macro menu form:**

Please see this video tutorial (full-screen or go to youtube):

[youtube=https://www.youtube.com/watch?v=sgMEMNJjrKY]

&#8230;or follow these instructions:

  1. Open Visual Basic Editor
  2. In the Project explorer,┬á**Right click**┬áon the workbook in which you would like to create the macro menu form (not the current workbook, but personal.xls, or wherever else you store your macros), and select┬á**Insert**, and then**┬áUserForm.**
  3. This should create an empty template. Let&#8217;s fill the template! From the Toolbox, select a┬á**CommandButton**
  4. On the Userform template,┬á**drag the shape of a box**, and this will create a button called CommandButton1.
  5. Obviously, we want to rename this, so┬á**right click**┬áon CommandButton1, and select┬á**Properties**.
  6. Change the┬á**Caption**┬áto the name you would like to see, in this case &#8220;Test button&#8221;, and press┬á**Enter**
  7. Let&#8217;s write some code inside this button.┬á**Double click**┬áon┬á**CommandButton1.┬á**This should create a macro for the Click event (what will happen when we click this button which is what we want).
  8. Make sure to add &#8220;userform1.hide&#8221; within the code in order to hide the form again&#8230; you may not need this, but I recommend it.
  9. Add some code! You can add code directly to the click event, or if you already have your macros written you can &#8220;RUN&#8221; the macro from wherever it is without having to move it. For now let&#8217;s keep it simple, and just add a message box&#8230; modify the text so it looks like this: 
    <pre>Private Sub CommandButton1_Click()
    MsgBox ("Hello world")
End Sub
</pre>

 10. **That&#8217;s it!**┬áRinse and repeat steps 3-6 as many times as you want! Now all we need is to way to show and hide the menu.
 11. In┬á**VBA Editor**, right click on your file, and select Insert->Module. This should bring up a white sheet. Copy paste the following: 
    <pre>Sub Show_menu()
 UserForm1.Show
End Sub
</pre>

 12. Lastly, create a button in the quicklaunch bar or custom menu to run this macro. In┬á**Excel 2007**,┬á**right click**┬áon the quicklaunch bar, and in the┬á**Choose commands from:**┬álist, select:┬á**Macros.**
 13. Select the macro┬á**Show_menu**┬áfrom the list, then click the button┬á**ADD > >**┬áand then click┬á**OK**┬á(you can change the image of the button by clicking┬á**Modify**┬áand selecting what you want from there.
 14. If you prefer a keyboard shortcut, you can also click on┬á**Macros**┬áfrom the┬á**Developer**┬átab in Excel, find the macro Show_menu, and then click┬á**Options**┬áon the right. This will bring up a shortcut screen, where you can for example, press Shift+T (or whatever you like). Click OK, and then cancel on the macro menu.
 15. You&#8217;re done! ┬áYou can access your menu by either pressing Ctrl+Shift+T, or by clicking the button on the quicklaunch bar.

**Other options:**

  * **Buttons**: Use buttons on the quicklaunch bar or a custom toolbar. ┬áThis is cool for a few macros, but after 10 or so macros, it gets a bit heavy. The buttons look like this:[<img title="custom_buttons" src="https://macrosforexcel.files.wordpress.com/2012/08/custom_buttons.png?resize=497%2C97" alt="" width="497" height="97" data-recalc-dims="1" />][2]

  * **Drop-down menu**: Ron DeBruin created a "Menu for favorite macros in Excel 2007-2010 (for one workbook)" but it seems to not be operational anymore)┬áthrough which you can create a drop-down list with the macros you so desire, in any┬áhierarchy┬áthat you specify. It&#8217;s pretty great, if it works for you.

 [1]: https://macrosforexcel.files.wordpress.com/2012/08/pop-up-example.jpg?resize=497%2C503
 [2]: https://macrosforexcel.files.wordpress.com/2012/08/custom_buttons.png?resize=497%2C97
