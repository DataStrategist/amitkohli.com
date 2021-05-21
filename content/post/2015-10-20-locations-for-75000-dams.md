---
title: Locations for 75000 dams
author: Amit
type: post
date: 2015-10-20T20:30:39+00:00
url: /locations-for-75000-dams/
switch_like_status:
  - 1
categories:
  - Big data
  - Data
  - Analysis
tags:
  - Barrage
  - csv
  - Dam
  - Database
  - Earth
  - Kml
  - Location
  - Map
  - Prensa
  - Reservoir

---
The last task I performed for <a href="http://www.fao.org/nr/aquastat" target="_blank">AQUASTAT</a> was to try to find the best way to estimate the anthropogenic evaporation from dams. The paper can be found [here]("http://www.fao.org/3/bc814e/bc814e.pdf"), but here I provide one of the fun outputs, a map of 75000 dams!

[<img class="alignnone size-medium wp-image-401" src="https://i2.wp.com/amitkohli.com/wp-content/uploads/2015/10/dams.png?resize=300%2C263" alt="dams" width="300" height="263" srcset="https://i2.wp.com/amitkohli.com/wp-content/uploads/2015/10/dams.png?resize=300%2C263 300w, https://i2.wp.com/amitkohli.com/wp-content/uploads/2015/10/dams.png?w=624 624w" sizes="(max-width: 300px) 100vw, 300px" data-recalc-dims="1" />][1]

ok okok&#8230; it&#8217;s not REALLY 75000 dams, this is an duplicate-containing amalgam of:

  * <a href="http://www.fao.org/nr/water/aquastat/dams/index.stm" target="_blank">AQUASTAT </a>dams with known location (green up arrow)
  * AQUASTAT dams with guessed location, estimated by City if known, else by State if known, else by Country (green diagonal arrow)
  * <a href="https://www.openstreetmap.org/#map=5/51.500/-0.100" target="_blank">OpenStreetMap </a>(OSM) dams using the awesome <a href="http://overpass-turbo.eu/" target="_blank">OverPass Turbo</a> API (blue left arrow)
  * Wikipedia dams&#8230; somehow inferred from <a href="http://dbpedia.org" target="_blank">dbpedia</a> (red/down arrow)

There really is a lot of redundancy, but I&#8217;m still pretty sure that this is the biggest collection of dam locations to date. Still, for those interested in the full kml, it&#8217;s available for download <a href="https://www.dropbox.com/s/1q27n6raje3gvab/all.merged.kml?dl=0" target="_blank">>>here<<</a> (CAREFUL&#8230; 200 MB), or just the minimum information in a small csv file <a href="https://www.dropbox.com/s/qpraev5pbvzk1jc/all.merged.csv?dl=0" target="_blank">>>here<<</a>. BTW, there&#8217;s a tutorial on how to create a google earth file like this one from an excel file <a href="https://amitkohli.com/kml-maker-for-excel-google-earth/" target="_blank">on this blog</a>.

 [1]: https://i2.wp.com/amitkohli.com/wp-content/uploads/2015/10/dams.png