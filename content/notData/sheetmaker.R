library(dplyr)
library(visNetwork)


##  MAKE NETWORK CHART ####
nodes <- readxl::read_excel("skills.xlsx", sheet = 2) %>% 
  mutate(shape = "box") %>% 
  mutate(label = stringr::str_wrap(label, width = 20)) %>% 
  mutate(font.color = "white")
edges <- readxl::read_excel("skills.xlsx", sheet = 1)

# nodes <- data.frame(id = c(skills$from,skills$to) %>% unique,
#                     label = c(skills$from,skills$to) %>% unique,
#                     level=c(1,1,2,3,3,4,5,6,6,6,7,8,7,2,3,9,9,7,7,10),
#                     stringsAsFactors = F)
# 
# edges <- data.frame(from= skills$from,
#                     to= skills$to)

a <- visNetwork(nodes, edges, width = "100%",height="800px") %>% 
  visEdges(arrows = "from") %>% 
  visHierarchicalLayout(levelSeparation = 80) %>% 
  visEdges(
           arrows =list(to = list(enabled = TRUE, scaleFactor = 1)),
           color = list(color = "lightblue", highlight = "red")) %>% 
  visOptions(collapse = list(enabled=T,fit=F))
a %>% htmltools::save_html("path.html")
