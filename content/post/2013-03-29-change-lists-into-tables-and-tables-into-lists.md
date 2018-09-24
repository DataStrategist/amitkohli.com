---
title: Change lists into tables and tables into lists
author: Amit
type: post
date: 2013-03-29T15:04:29+00:00
url: /change-lists-into-tables-and-tables-into-lists/
categories:
  - Excel
  - Macro
  - Tutorials
  - Userform
  - VBA

---
Designed a userform that converts dimension formats, i.e. information from tabular format to list (or flat) format, and viceversa. Some options include preserving formatting or not, as well as including blank cells or not.

>>Form is here:[Dim changer userform][1]

>>Excel file with embedded form and a macro to make the form pop up is here:[Dim_changer][2]

>>Tutorial is here: <a title="Youtube tutorial" href="http://www.youtube.com/edit?video_id=VdmV4BJT3H4" target="_blank">https://www.youtube.com/watch?v=EvaRfIZo0QY</a>

Code to inspect is here:

<pre>Option Explicit
Private Sub CommandButton1_Click()
'Dimension Fixer is by Amit Kohli (www.AmitKohli.com). You can use this macro free of charge, but please leave a comment if it's useful, and of course,
'this macro comes with no guarantees whatsoever. If you use this and something bad happens, you can't hold me liable.
'ok

'-------------DIMs
Dim rrange1, rrange2, datastarts, X, Y1 As Range
Dim i, i_ctr As Integer
Dim r, c As Variant
Dim cmt As Comment
Dim fixxed_cmt As String
Dim arr(99999, 5)

'-------------ERRORS
If Me.OB_Table_to_List.Value = False And Me.OB_List_to_table.Value = False Then
MsgBox ("Please select what I should do with your data")
Exit Sub
End If

'-------------PICK DIMENSIONS
Me.Hide
On Error Resume Next
Application.DisplayAlerts = False
If Me.OB_List_to_table Then 'Dim 1, ROW headings
Set rrange1 = Application.InputBox(Prompt:="Please select the Dimension that will become ROW HEADINGS", Title:="SPECIFY DIM 1", Type:=8)
Else
Set rrange1 = Application.InputBox(Prompt:="Please select the ROW HEADINGS", Title:="SPECIFY DIM 1", Type:=8)
End If

If rrange1 Is Nothing Then Exit Sub

If Me.OB_List_to_table Then 'Dim 2, COLUMN headings
Set rrange2 = Application.InputBox(Prompt:="Please select the Dimension that will become COLUMN HEADINGS", Title:="SPECIFY DIM 2", Type:=8)
Else
Set rrange2 = Application.InputBox(Prompt:="Please select the COLUMN HEADINGS", Title:="SPECIFY DIM 2", Type:=8)
End If

On Error GoTo 0
If rrange2 Is Nothing Then Exit Sub

Set datastarts = Application.InputBox(Prompt:="Please select first data-point.", Title:="SPECIFY DIM 2", Type:=8) 'First data point

Application.DisplayAlerts = True

If datastarts Is Nothing Then Exit Sub

If rrange1.Cells(1, 1).Column = datastarts.Column Then
Set X = rrange1
Set Y1 = rrange2
Else
Set X = rrange2
Set Y1 = rrange1
End If

If Me.CB_formatting Then
'In comments, replace line breaks with unique character ƒ, and " with '. (Just cleaning up for later)
For Each cmt In ActiveSheet.Comments
'fixxed_cmt = Replace(cmt.Text, Chr(10), "ƒ")
'fixxed_cmt = Replace(cmt.Text, Chr(13), "ƒ")
fixxed_cmt = Replace(cmt.Text, """", "'")
cmt.Delete
cmt.Parent.AddComment Text:=fixxed_cmt
Next
End If

'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=START! ARR 0=Row counter | 1=Column counter | 2=Value | 3=Cell Color | 4=Font Color | 5=Comment

i = 0

If Me.OB_Table_to_List Then '================================================================================== TABLE ------&gt; LIST HERE
datastarts.Activate

For Each r In Y1
For Each c In X
Range("A1").Offset(r.Row - 1, c.Column - 1).Activate 'debug
arr(i, 0) = r
arr(i, 1) = c
arr(i, 2) = Range("A1").Offset(r.Row - 1, c.Column - 1).Formula
If Me.CB_formatting Then
arr(i, 3) = Range("A1").Offset(r.Row - 1, c.Column - 1).Interior.Color
arr(i, 4) = Range("A1").Offset(r.Row - 1, c.Column - 1).Font.Color
On Error Resume Next
arr(i, 5) = Range("A1").Offset(r.Row - 1, c.Column - 1).Comment.Text
On Error GoTo 0
End If

i = i + 1
Next
Next

'====OK, done, now spitting out results
Workbooks.Add
Range("B2").Activate

For i_ctr = 0 To i - 1
If Len(arr(i_ctr, 2)) &lt;&gt; 0 Or Me.CB_Blanks Then 'if cell isn't empty or if u want blanks
ActiveCell.Offset(0, 0).Value = arr(i_ctr, 0)
ActiveCell.Offset(0, 1).Value = arr(i_ctr, 1)
ActiveCell.Offset(0, 2).Value = arr(i_ctr, 2)
If Me.CB_formatting Then
ActiveCell.Offset(0, 2).Interior.Color = arr(i_ctr, 3)
ActiveCell.Offset(0, 2).Font.Color = arr(i_ctr, 4)
If Len(arr(i_ctr, 5)) &lt;&gt; 0 Then
ActiveCell.Offset(0, 2).NoteText arr(i_ctr, 5)
End If
End If
ActiveCell.Offset(1, 0).Activate
End If
Next

Else '========================================================================================================== LIST ------&gt; TABLE HERE

For Each c In rrange1
datastarts.Offset(i, 0).Activate

arr(i, 0) = c.Value
arr(i, 1) = rrange2.Cells(i + 1, 1).Value
arr(i, 2) = datastarts.Offset(i, 0).Formula
If Me.CB_formatting Then
arr(i, 3) = datastarts.Offset(i, 0).Interior.Color
arr(i, 4) = datastarts.Offset(i, 0).Font.Color
On Error Resume Next
arr(i, 5) = datastarts.Offset(i, 0).Comment.Text
On Error GoTo 0
End If

i = i + 1
Next

'====OK, done, now spitting out results

Application.Workbooks.Add
For i_ctr = 0 To i - 1

If Len(arr(i_ctr, 2)) &lt;&gt; 0 Or Me.CB_Blanks Then 'if cell isn't empty or if u want blanks
Range("c1").Activate
'find correct column header
While ActiveCell.Offset(1 - ActiveCell.Row, 0).Value &lt;&gt; arr(i_ctr, 1) And ActiveCell.Offset(1 - ActiveCell.Row, 0).Value &lt;&gt; ""
ActiveCell.Offset(0, 1).Activate
Wend
'didn't find it.. labelling
If ActiveCell.Offset(1 - ActiveCell.Row, 0).Value = "" Then ActiveCell.Offset(1 - ActiveCell.Row, 0).Value = arr(i_ctr, 1)

ActiveCell.Offset(1, 0).Activate

'find correct row header
While ActiveCell.Offset(0, 1 - ActiveCell.Column).Value &lt;&gt; arr(i_ctr, 0) And ActiveCell.Offset(0, 1 - ActiveCell.Column).Value &lt;&gt; ""
ActiveCell.Offset(1, 0).Activate
Wend
'didn't find it.. labelling
If ActiveCell.Offset(0, 1 - ActiveCell.Column).Value = "" Then ActiveCell.Offset(0, 1 - ActiveCell.Column).Value = arr(i_ctr, 0)

ActiveCell.Formula = arr(i_ctr, 2) 'Found point! Putting data
If Me.CB_formatting Then
ActiveCell.Interior.Color = arr(i_ctr, 3)
ActiveCell.Font.Color = arr(i_ctr, 4)
If Len(arr(i_ctr, 5)) &lt;&gt; 0 Then
ActiveCell.NoteText arr(i_ctr, 5)
End If
End If
End If
Next

End If

End Sub

Private Sub CommandButton2_Click()
'Cancel
Unload Dim_changer
End Sub
</pre>

 [1]: http://www.amitkohli.com/uploads/Dim_changer.frm
 [2]: https://amitkohli.com/wp-content/uploads/2013/03/Dim_changer.xlsm