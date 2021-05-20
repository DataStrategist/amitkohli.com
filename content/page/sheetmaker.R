library(dplyr)
library(visNetwork)
library(xlsx)

##  MAKE NETWORK CHART ####
  nodes <- read.xlsx("skills.xlsx",stringsAsFactors = F,sheetIndex = 1)
  edges <- read.xlsx("skills.xlsx",stringsAsFactors = F,sheetIndex = 2)
  
  visNetwork(nodes, edges, width = "100%",height="2000px") %>% 
    visEdges(arrows = "from") %>% 
    # visHierarchicalLayout(levelSeparation = 60, nodeSpacing = 200, 
    #                       treeSpacing = 300, edgeMinimization = T) %>% 
    visEdges(shadow = F,
             arrows =list(to = list(enabled = TRUE, scaleFactor = .5)),
              color = list(color = "lightgrey", highlight = "yellow"))
  
  