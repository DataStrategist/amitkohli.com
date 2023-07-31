### Cloropleth map of where I've lived

library(leaflet)
library(tidyverse)
library(htmltools)

# Download the map -------------------------------------------------------
# download.file("http://thematicmapping.org/downloads/TM_WORLD_BORDERS_SIMPL-0.3.zip" , 
#               destfile="data_mine/world_shape_file.zip")
# 
# system("unzip -o data_mine/world_shape_file.zip -d data_mine")


## base map
world_spdf <- rgdal::readOGR( 
  dsn= paste0(getwd(), "/data_mine") , 
  layer="TM_WORLD_BORDERS_SIMPL-0.3",
  verbose=FALSE
)

run <- readline("SIMPLE (s) or DETAILED (d) map? >")

## Create data
simple_countries <- function(){
  visited_countries <- c("CHL", "USA", "COL", "HND", "URY", "PRY", "MEX", 
                         "GBR", "ITA", "DEU", 
                         "GHA", "ETH", "ZMB", "KEN", "TZA",
                         "BGD", "PHL", "IND")
  
  AVp <- readr::read_csv("data_mine/ACDIVOCA projects") %>% 
    mutate(Country = ifelse(Country == "Tanzania", "United Republic of Tanzania", Country)) %>% 
    left_join(world_spdf@data, by = c("Country" = "NAME")) %>% 
    ##Meh, some I didn't really do:
    filter(!is.na(ISO3), ISO3 != "ARM", ISO3 != "GIN") %>% 
    pull(ISO3) %>% unique
  
  countries <- c(visited_countries, AVp) %>% unique
  return(countries)
}

detailed_countries <- function(){
  av_field <- tibble(cou = c("GHA", "BGD", "PHL", "KEN", "COL", "IND", "HND", "PRY"), av_field = 1)
  central <- tibble(cou = c("CHL", "GBR", "ITA", "GHA"), central = 1)
  tech <- tibble(cou = c("USA", "GBR", "URY", "MEX", "DEU"), tech = 1) 
  leadership <- tibble(cou = c("ETH", "TZA", "GBR", "USA"), leadership = 1)
  
  countries <- full_join(av_field, central, by = "cou") %>% 
    full_join(tech, by = "cou") %>% 
    full_join(leadership, by = "cou") %>% 
    mutate(various = rowSums(across(where(is.numeric)), na.rm = TRUE))
  
  simple_c <- tibble(cou = simple_countries(), simple = 1)
  
  ## all countries that I haven't explicitly named just get added to tech
  countries <- full_join(countries, simple_c, by = "cou") %>% 
    mutate(tech = ifelse(is.na(various), 1, tech)) %>% select(-simple)
  
  ## simplify to one category
  countries <- countries %>% pivot_longer(cols = -cou) %>% 
    filter(!is.na(value), !(name == "various" & value == 1)) %>% arrange(cou, desc(value)) %>% 
    group_by(cou) %>% slice(1) %>% select(-value)
  
  return(countries)
}

# MAP! --------------------------------------------------------------------

if (run == "s"){
  countries <- tibble(ISO3 = simple_countries(), color = "#FF7560")
} else {
  countries <- detailed_countries() %>% rename(group = name, ISO3 = cou)
  qpal <- colorFactor("Set3", countries$group, n = length(countries$group))
  countries$color <- qpal(countries$group)
}

## add data
world_spdf@data <- world_spdf@data %>% 
  left_join(countries, by = "ISO3") %>% 
  mutate(fillOpacity = ifelse(is.na(color), 0, 1))

m <- leaflet(world_spdf, options = leafletOptions(zoomControl = FALSE)) %>% 
  addProviderTiles("Stamen.Watercolor", group = "Toner Lite") %>%
  setView( lat=10, lng=0 , zoom=2) %>%
  addPolygons(fillOpacity = ~fillOpacity, fillColor = ~color, color = "white", weight = 1)

if (run == "d") m <- m %>% addLegend(pal = qpal, values = ~group, opacity = 1)

tag.map.title <- tags$style(HTML("
  .leaflet-control.map-title { 
    transform: translate(-50%,20%);
    position: fixed !important;
    left: 20%;
    text-align: center;
    padding-left: 10px; 
    padding-right: 10px; 
    background: rgba(0,0,0,0.25);
    font-weight: bold;
    font-size: 28px;
    font-family: Leafy;
    color: white;
  }
"))

title <- tags$div(
  tag.map.title, HTML("What kind of work have I done?")
)  

m %>%
  addControl(title, position = "topleft", className="map-title")
   
