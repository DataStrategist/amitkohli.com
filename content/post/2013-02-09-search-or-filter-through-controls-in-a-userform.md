---
title: Search or filter through controls in a userform
author: Amit
type: post
date: 2013-02-09T18:30:30+00:00
url: /search-or-filter-through-controls-in-a-userform/
categories:
  - Excel
  - Tutorials
  - Userform
  - VBA
tags:
  - filter
  - form
  - macro
  - userform

---
This bit might be useful if you have a lot of controls on a form, and need a quick way to highlight them. This post supports the video:

I uploaded a video tutorial, you can see it here (please view in fullscreen mode, or watch the video in youtube by clicking on the youtube logo):[http://www.youtube.com/watch?v=5RtV9msZ2RE].

Download the file here ([Search on vba][1]), or just copypaste the code below in a userform or your own:

<pre>Private Sub Searcher_Change()
Dim c As Control
For Each c In Me.Controls  'CHECK EACH CONTROL
    If c.Name &lt;&gt; "Searcher" Then 'IF IT'S NOT THE SEARCHING BOX
        L = Len(Me.Searcher.Value) 'DEFINE "CHUNK LENGTH"
        For i = 1 To Len(c.Name) + 1
            'COMPARE L-SIZE STRING IN NAME AGAINST SEARCHER.VALUE
            If Mid(c.Name, i, L) = Me.Searcher.Value Then EN = 1
        Next
        If EN = 1 Then c.Enabled = True Else c.Enabled = False
        EN = 0
    End If
Next
End Sub


</pre>

 [1]: http://amitkohli.com/wp-content/uploads/2013/02/Search-on-vba.xls "Download"