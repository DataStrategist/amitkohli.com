---
title: Macro userform – a good visual way to organize macros
author: Amit
type: post
date: 2013-02-07T16:22:10+00:00
url: /macro-userform-a-good-visual-way-to-organize-macros/
categories:
  - Excel
  - Tutorials
  - Userform
  - VBA
tags:
  - excel
  - macro
  - organization
  - tutorial
  - userform
  - vba
  - Visual Basic

---
At a certain point it can become challenging to quickly find and run the macro we need. Below are some options to organize our macros. I will focus on using a **pop-up form** because it&#8217;s the method I prefer, but at the bottom of the article, you can see other options.

A pop-up menu looks like this:

[<img title="pop-up example" src="http://macrosforexcel.files.wordpress.com/2012/08/pop-up-example.jpg?resize=497%2C503" alt="" width="497" height="503" data-recalc-dims="1" />][1]

**How to make your own Macro menu form:**

Please see this video tutorial (full-screen or go to youtube):

[youtube=http://www.youtube.com/watch?v=NHxGqt3Dr4k]

&#8230;or follow these instructions:

  1. Open Visual Basic Editor
  2. In the Project explorer, **Right click** on the workbook in which you would like to create the macro menu form (not the current workbook, but personal.xls, or wherever else you store your macros), and select **Insert**, and then** UserForm.**
  3. This should create an empty template. Let&#8217;s fill the template! From the Toolbox, select a **CommandButton**
  4. On the Userform template, **drag the shape of a box**, and this will create a button called CommandButton1.
  5. Obviously, we want to rename this, so **right click** on CommandButton1, and select **Properties**.
  6. Change the **Caption** to the name you would like to see, in this case &#8220;Test button&#8221;, and press **Enter**
  7. Let&#8217;s write some code inside this button. **Double click** on **CommandButton1. **This should create a macro for the Click event (what will happen when we click this button which is what we want).
  8. Make sure to add &#8220;userform1.hide&#8221; within the code in order to hide the form again&#8230; you may not need this, but I recommend it.
  9. Add some code! You can add code directly to the click event, or if you already have your macros written you can &#8220;RUN&#8221; the macro from wherever it is without having to move it. For now let&#8217;s keep it simple, and just add a message box&#8230; modify the text so it looks like this: 
    <pre>Private Sub CommandButton1_Click()
    MsgBox ("Hello world")
End Sub
</pre>

 10. **That&#8217;s it!** Rinse and repeat steps 3-6 as many times as you want! Now all we need is to way to show and hide the menu.
 11. In **VBA Editor**, right click on your file, and select Insert->Module. This should bring up a white sheet. Copy paste the following: 
    <pre>Sub Show_menu()
 UserForm1.Show
End Sub
</pre>

 12. Lastly, create a button in the quicklaunch bar or custom menu to run this macro. In **Excel 2007**, **right click** on the quicklaunch bar, and in the **Choose commands from:** list, select: **Macros.**
 13. Select the macro **Show_menu** from the list, then click the button **ADD > >** and then click **OK** (you can change the image of the button by clicking **Modify** and selecting what you want from there.
 14. If you prefer a keyboard shortcut, you can also click on **Macros** from the **Developer** tab in Excel, find the macro Show_menu, and then click **Options** on the right. This will bring up a shortcut screen, where you can for example, press Shift+T (or whatever you like). Click OK, and then cancel on the macro menu.
 15. You&#8217;re done!  You can access your menu by either pressing Ctrl+Shift+T, or by clicking the button on the quicklaunch bar.

**Other options:**

  * **Buttons**: Use buttons on the quicklaunch bar or a custom toolbar.  This is cool for a few macros, but after 10 or so macros, it gets a bit heavy. The buttons look like this:[<img title="custom_buttons" src="http://macrosforexcel.files.wordpress.com/2012/08/custom_buttons.png?resize=497%2C97" alt="" width="497" height="97" data-recalc-dims="1" />][2]

  * **Drop-down menu**: Ron DeBruin created an<a title="Menu for favorite macros in Excel 2007-2010 (for one workbook)" href="http://www.rondebruin.nl/qat2.htm" target="_blank"> excellent method</a> through which you can create a drop-down list with the macros you so desire, in any hierarchy that you specify. It&#8217;s pretty great, if it works for you.

 [1]: http://macrosforexcel.files.wordpress.com/2012/08/pop-up-example.jpg?resize=497%2C503
 [2]: http://macrosforexcel.files.wordpress.com/2012/08/custom_buttons.png?resize=497%2C97