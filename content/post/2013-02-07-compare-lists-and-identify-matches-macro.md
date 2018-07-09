---
title: Compare lists and identify matches macro
author: Amit
type: post
date: 2013-02-07T16:24:52+00:00
url: /compare-lists-and-identify-matches-macro/
categories:
  - Excel
  - Macro
  - Tutorials
  - VBA
tags:
  - compare
  - excel
  - list
  - macro
  - matches
  - tutorial
  - vba
  - Visual Basic
  - vlookup

---
This macro provides an alternative to vlookup (which looks at two lists and provides data from one list to the second) that retains similar functionality while providing certain benefits. It accomplishes this by physically moving one list to the other. It&#8217;s impossible to get a false positive, and it doesn&#8217;t provide that annoying #N/A that messes up calculations.

Additionally, it let&#8217;s you decide whether to identify the matches and move them to the top (useful for quickly working with data), or not (useful in identifying holes in each list and working with that).

And here is the macro itself. Copy/paste the code, or <a title="Compare lists macro file" href="http://www.amitkohli.com/excel/compare_lists.bas" target="_blank">download the file here</a> (if it opens as text, right click and &#8220;Save link as&#8221;).

<pre>Sub compare_lists()
' Author: Amit Kohli
'START ON COLUMN TO TEST

If Application.ReferenceStyle = xlA1 Then
 Application.ReferenceStyle = xlR1C1
 change_back = 1
Else
 Application.ReferenceStyle = xlA1
End If

firstr = ActiveCell.Row
firstc = ActiveCell.Column

col_comp = InputBox("What column has the correct names?")
'=====================
'tt = 100 'Uncomment this if you know you will always have x columns of data following the name (where in this case x=100)
tt = InputBox("How many columns of data?")
'=====================
If change_back = 1 Then Application.ReferenceStyle = xlA1

If tt = "" Or col_comp = "" Then Exit Sub

beg:

If ActiveCell.Value &lt;&gt; ActiveCell.Offset(0, col_comp - ActiveCell.Column).Value Then

While ActiveCell.Value &lt;&gt; ActiveCell.Offset(i, col_comp - ActiveCell.Column).Value And ActiveCell.Offset(i, col_comp - ActiveCell.Column).Value &lt;&gt; ""
 i = i + 1
 Wend

 If ActiveCell.Value = ActiveCell.Offset(i, col_comp - ActiveCell.Column).Value Then
 Range(ActiveCell, ActiveCell.Offset(i - 1, tt)).Select
 Selection.Insert Shift:=xlDown
 ActiveCell.Offset(i, 0).Activate
 Else
 ActiveCell.EntireRow.Insert
 Range(ActiveCell, ActiveCell.Offset(0, tt)).Delete Shift:=xlUp
 ActiveCell.Offset(1, 0).Activate
 i = 0
 GoTo beg
 End If
 i = 0
Else
 ActiveCell.Offset(1, 0).Activate
End If

If ActiveCell.Value &lt;&gt; "" Then GoTo beg

cont = MsgBox("Move matches to top?", vbYesNo)
If cont = 6 Then
 Range(ActiveCell.Offset(0, tt), ActiveCell.Offset(firstr - ActiveCell.Row, col_comp - ActiveCell.Column)).Select
 Selection.Sort Key1:=Range(ActiveCell.Offset(0, firstc - ActiveCell.Column).Address), Order1:=xlAscending, Header:=xlNo
 ActiveCell.Offset(0, firstc - col_comp).Select
 Selection.End(xlDown).Activate
 Range(ActiveCell.Offset(0, tt), ActiveCell.Offset(firstr - ActiveCell.Row, col_comp - ActiveCell.Column)).Select
 Selection.Sort Key1:=Range(ActiveCell.Address), Order1:=xlAscending, Header:=xlNo
 Selection.End(xlDown).Activate
 ActiveCell.EntireRow.Borders(xlEdgeBottom).LineStyle = xlDouble
End If

ActiveCell.Offset(1 - ActiveCell.Row, 0).Activate
End Sub
</pre>

I uploaded a video tutorial, you can see it here (please view in fullscreen mode, or watch the video in youtube by clicking on the logo):[youtube=http://www.youtube.com/watch?v=4lcEB28JpJg]