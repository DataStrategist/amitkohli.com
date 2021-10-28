### Cloropleth map of where I've lived

library(leaflet)
library(dplyr)
library(htmltools)

# Download the map -------------------------------------------------------
# download.file("http://thematicmapping.org/downloads/TM_WORLD_BORDERS_SIMPL-0.3.zip" , 
#               destfile="data_mine/world_shape_file.zip")
# 
# system("unzip -o data_mine/world_shape_file.zip -d data_mine")

world_spdf <- rgdal::readOGR( 
  dsn= paste0(getwd(), "/data_mine") , 
  layer="TM_WORLD_BORDERS_SIMPL-0.3",
  verbose=FALSE
)


## Create data
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


# MAP! --------------------------------------------------------------------

world_spdf@data <- world_spdf@data %>% 
  left_join(tibble(ISO3 = countries, color = "#FF7560"), by = "ISO3") %>% 
  mutate(fillOpacity = ifelse(is.na(color), 0, 1))

m <- leaflet(world_spdf, options = leafletOptions(zoomControl = FALSE)) %>% 
  addProviderTiles("Stamen.Watercolor", group = "Toner Lite") %>%
  setView( lat=10, lng=0 , zoom=2) %>%
  addPolygons(fillOpacity = ~fillOpacity, fillColor = ~color, color = "white", weight = 1)

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
  tag.map.title, HTML("I have worked around the world")
)  

m %>%
  addControl(title, position = "topleft", className="map-title")
   
