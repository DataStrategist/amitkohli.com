---
title: Human armature from d3Network!
author: Amit
type: post
date: 2014-11-11T00:17:06+00:00
url: /human-armature-from-d3network/
xyz_smap:
  - 1
categories:
  - Art
  - R
  - Tutorials
tags:
  - armature
  - d3Network
  - frame
  - human
  - R

---
So a little bit of R, a little bit of d3Network and boom! Instant interactive html human!

    <style>
    .link {
    stroke: #666;
    opacity: 0.4;
    stroke-width: 1.5px;
    }
    .node circle {
    stroke: #fff;
    opacity: 0.4;
    stroke-width: 1.5px;
    }
    .node:not(:hover) .nodetext {
    display: none;
    }
    text {
    font: 7px serif;
    opacity: 0.4;
    pointer-events: none;
    }
    </style>
    
    <script src=http://d3js.org/d3.v3.min.js></script>
    
    <script> 
     var links = [ { "source" : 0, "target" : 1, "value" : 300 }, { "source" : 1, "target" : 2, "value" : 50 }, { "source" : 1, "target" : 3, "value" : 50 }, { "source" : 2, "target" : 4, "value" : 20 }, { "source" : 3, "target" : 5, "value" : 20 }, { "source" : 4, "target" : 6, "value" : 1 }, { "source" : 5, "target" : 7, "value" : 1 }, { "source" : 8, "target" : 9, "value" : 50 }, { "source" : 9, "target" : 10, "value" : 20 }, { "source" : 9, "target" : 11, "value" : 20 }, { "source" : 10, "target" : 12, "value" : 10 }, { "source" : 11, "target" : 13, "value" : 10 }, { "source" : 12, "target" : 14, "value" : 5 }, { "source" : 13, "target" : 15, "value" : 5 }, { "source" : 2, "target" : 8, "value" : 50 }, { "source" : 3, "target" : 16, "value" : 50 }, { "source" : 1, "target" : 8, "value" : 50 }, { "source" : 1, "target" : 16, "value" : 50 }, { "source" : 8, "target" : 16, "value" : 50 }, { "source" : 16, "target" : 9, "value" : 50 } ] ; 
     var nodes = [ { "name" : "Head", "group" : 1 }, { "name" : "Sternum", "group" : 1 }, { "name" : "Shoulder.r", "group" : 1 }, { "name" : "Shoulder.l", "group" : 1 }, { "name" : "Elbow.r", "group" : 1 }, { "name" : "Elbow.l", "group" : 1 }, { "name" : "Wrist.r", "group" : 1 }, { "name" : "Wrist.l", "group" : 1 }, { "name" : "rib.r", "group" : 1 }, { "name" : "hip.c", "group" : 1 }, { "name" : "hip.r", "group" : 1 }, { "name" : "hip.l", "group" : 1 }, { "name" : "knee.r", "group" : 1 }, { "name" : "knee.l", "group" : 1 }, { "name" : "ankle.r", "group" : 1 }, { "name" : "ankle.l", "group" : 1 }, { "name" : "rib.l", "group" : 1 } ] ; 
     var width = 900
    height = 600;
    
    var color = d3.scale.category20();
    
    var force = d3.layout.force()
    .nodes(d3.values(nodes))
    .links(links)
    .size([width, height])
    .linkDistance(50)
    .charge(-120)
    .on("tick", tick)
    .start();
    
    var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);
    
    var link = svg.selectAll(".link")
    .data(force.links())
    .enter().append("line")
    .attr("class", "link")
    .style("stroke-width", function(d) { return Math.sqrt(d.value); });
    
    var node = svg.selectAll(".node")
    .data(force.nodes())
    .enter().append("g")
    .attr("class", "node")
    .style("fill", function(d) { return color(d.group); })
    .style("opacity", 0.4)
    .on("mouseover", mouseover)
    .on("mouseout", mouseout)
    .call(force.drag);
    
    node.append("circle")
    .attr("r", 6)
    
    node.append("svg:text")
    .attr("class", "nodetext")
    .attr("dx", 12)
    .attr("dy", ".35em")
    .text(function(d) { return d.name });
    
    function tick() {
    link
    .attr("x1", function(d) { return d.source.x; })
    .attr("y1", function(d) { return d.source.y; })
    .attr("x2", function(d) { return d.target.x; })
    .attr("y2", function(d) { return d.target.y; });
    
    node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
    }
    
    function mouseover() {
    d3.select(this).select("circle").transition()
    .duration(750)
    .attr("r", 16);
    d3.select(this).select("text").transition()
    .duration(750)
    .attr("x", 13)
    .style("stroke-width", ".5px")
    .style("font", "17.5px serif")
    .style("opacity", 1);
    }
    
    function mouseout() {
    d3.select(this).select("circle").transition()
    .duration(750)
    .attr("r", 8);
    }
    
    </script>
    
&nbsp;

<!-- iframe plugin v.4.3 wordpress.org/plugins/iframe/ -->

&nbsp;

Code to make your own or edit as you see fit:

<pre>library(d3Network)

Nodes &lt;- c(
"Head", "Sternum", "Shoulder.r", "Shoulder.l", # 0 1 2 3
"Elbow.r", "Elbow.l", "Wrist.r", "Wrist.l", # 4 5 6 7
"rib.r", "hip.c", "hip.r", "hip.l", # 8 9 10 11
"knee.r", "knee.l", "ankle.r", "ankle.l", # 12 13 14 15
"rib.l") # 16

Nodes.df &lt;- data.frame(name=Nodes, group=rep(1,length(Nodes)))

Con &lt;- rbind(
c(0, 1, 300),
c(1, 2, 50),
c(1, 3, 50),
c(2, 4, 20),
c(3, 5, 20),
c(4, 6, 1),
c(5, 7, 1),
c(8, 9, 50),
c(9, 10, 20),
c(9, 11, 20),
c(10, 12, 10),
c(11, 13, 10),
c(12, 14, 5),
c(13, 15, 5),
c(2, 8, 50),
c(3, 16, 50),
c(1, 8, 50),
c(1, 16, 50),
c(8, 16, 50),
c(16, 9, 50))

colnames(Con) &lt;- c("source", "target", "value")
Con &lt;- as.data.frame(Con)

d3ForceNetwork(Links = Con, Nodes = Nodes.df, Source = "source",
Target = "target", Value = "value", NodeID = "name",
Group = "group", opacity = 0.4, file="human.html")
</pre>