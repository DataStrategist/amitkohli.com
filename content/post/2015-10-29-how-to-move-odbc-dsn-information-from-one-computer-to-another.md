---
title: How to move ODBC DSN information from one computer to another
author: Amit
type: post
date: 2015-10-29T19:02:49+00:00
url: /how-to-move-odbc-dsn-information-from-one-computer-to-another/
switch_like_status:
  - 1
categories:
  - Databases
  - Tutorials
tags:
  - Azure
  - cloud
  - data connection
  - DNS
  - new computer
  - new laptop
  - ODBC
  - windows

---
YAAAAAAAAY!!!! I got a new computer!!![<img class="size-medium wp-image-429 alignleft" src="https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/10/Data-transfer.jpg?resize=300%2C169" alt="Data-transfer" width="300" height="169" srcset="https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/10/Data-transfer.jpg?resize=300%2C169 300w, https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/10/Data-transfer.jpg?w=640 640w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" />][1]

Oh crap how do I move the DSN connections that I made on this computer?? This is how (assuming you&#8217;re on windows)! But before, we do, we have to make sure we have the right drivers&#8230; so lemme first go over the basikses my precious:

#### **TO ADD NEW CONNECTIONS:**

  * Build a shortcut on your desktop to: C:\Windows\SysWOW64\odbcad32.exe
  * Add connections from there.

#### **IF IN THE NEW COMPUTER YOU CAN’T ADD THE NEW CONNECTIONS YOU NEED:**

  * You need to download the drivers. In my case, since I want to talk to Azure databases, I need this driver: <http://www.microsoft.com/en-us/download/confirmation.aspx?id=36434>. That worked for me, you get what you need and download it.
  * Install it. It will automatically add the connection type ODBC Driver 11 for SQL Server (or whatever) to your odbcad32.

OK, now that you&#8217;re all set and you know your new pc can do the connections, without further ado:

### **TRANSFER DNS FILES FROM COMPUTER A TO COMPUTER B:**

  1. On Computer A, open the Registry Editor by typing &#8220;regedit&#8221; in the Windows search box under the Start menu and selecting regedit.exe
  2. Navigate to the following registry key : **HKEY\_CURRENT\_USER > Software > ODBC**
  3. Right-click on the ODBC.INI folder, choose Export, and save the .reg file to the location of your choice
  
    4. Copy the .reg file (or files if you have both User and System DSN data sources) to any location Computer B
  
    5. On Computer B, double click the .reg file(s) to import the DSN data sources to the registry (select &#8220;Yes&#8221; and &#8220;OK&#8221; when prompted)

&nbsp;

done!

&nbsp;

### **EDIT: What if we are going from a Computer to a Server?**

One of the steps of operationalizing scripts is to move them from a computer to a server. When that happens now we have to sync data connections too&#8230; in addition, it&#8217;s possible there&#8217;s a different driver and syntax (if we&#8217;re going from Windows to Linux). Therefore, we propose a workthrough to keep ODBC sources synced.

  1. From the server, create a git repo in the folder that contains the `ODBC.ini` file (in my version of Ubuntu 16.04, it&#8217;s `/etc`. You DONT need to add all files to the repo&#8230; only `ODBC.ini`. Back that up to a private repo on github, and clone it to your windows machine.
  2. Write a `cmd` script that will automatically export the ODBC keys, [from here][2]. Make sure you are in the cloned folder, then startup a Command promt (type Windows Key and then `cmd` ). Inside there, type: `reg export HKEY_CURRENT_USER\Software\ODBC export.reg` This has exported the ODBC sources to a file called `export.reg`. Which is cool! We just need to do some gentle manipulations to get it to work on the server. [<img class="alignnone size-medium wp-image-797" src="https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/10/serv.png?resize=300%2C267" alt="" width="300" height="267" srcset="https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/10/serv.png?resize=300%2C267 300w, https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/10/serv.png?w=513 513w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" />][3]
  3. In order to get this to work on the server, we need to do a few things (this is for me, in Ubuntu 16.04): 
      1. Delete the top stuff (you don&#8217;t see it in the above, but we need to export only the sources)
      2. Remove quotation marks
      3. Change the Driver
      4. Delete the extra stuff before the DNS stuff.

&nbsp;

Let&#8217;s write a R script to accomplish this:

<pre class="EnlighterJSRAW" data-enlighter-language="null">## Get latest stuff
#system("reg export HKEY_CURRENT_USER\Software\ODBC export.reg",intern = F) 
## ^ Hrm... this part is a bit finecky... just do it manually through cmd for now.

## Read in
file &lt;- file("export.reg")
a &lt;- readLines(file,skipNul = T)
close(file)

## Lose head
a &lt;- a[-1:-12]

## Remove quotes
a &lt;- gsub('"','',a)

## Remove path to DNS name
a &lt;- gsub('.+ODBC.INI\\\\','[',a)

## Replace Driver
a &lt;- gsub('C.+?msodbcsql11.dll','ODBC Driver 13 for SQL Server',a)

## Delete blank lines
a &lt;- a[a !=""]

## Write
file &lt;- file("odbc.ini")
writeLines(a,file)
close(file)
</pre>

Done! Now you have a way of keeping the server data sources synced with your laptop!

 [1]: https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/10/Data-transfer.jpg
 [2]: https://superuser.com/questions/595551/how-to-export-a-specific-registry-key-to-a-text-file-using-command-line#
 [3]: https://i1.wp.com/amitkohli.com/wp-content/uploads/2015/10/serv.png