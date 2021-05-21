
projectAdder <- function(topics, elementName, mainTitle, subTitle,
                         imageLink, linkLink, description){
  text <- readLines("C:/Users/mexin/Dropbox/My projects/amitkohli.com/public/consulting/projectTemplate.txt")
  text <- gsub("TOPICS", topics, text)
  text <- gsub("ELEMENTNAME", elementName, text)
  text <- gsub("MAINTITLE", mainTitle, text)
  text <- gsub("SUBTITLE", subTitle, text)
  text <- gsub("IMAGELINK", imageLink, text)
  text <- gsub("LINKLINK", linkLink, text)
  text <- gsub("DESCRIPTION", description, text)
  text <- gsub("$", "\n", text)
  cat(noquote(text))
}

# projectAdder(topics = "",
#              elementName = "",
#              mainTitle = "",
#              subTitle = "",
#              imageLink = "",
#              linkLink = "",
#              description = "")

projectAdder(topics = "nlp fun analysis",
             elementName = "girlfriend",
             mainTitle = "Analyzing my girlfriend's text messages",
             subTitle = "Trying to quantify 'how the relationship is going'",
             imageLink = "https://i0.wp.com/amitkohli.com/wp-content/uploads/2015/08/senAn.png",
             linkLink = "https://www.amitkohli.com/sentiment-analysis-on-my-girlfriends-text-messages/",
             description = "As I was beginning to fall in love w/ NLP, I was also falling in love with a beautiful woman, now my wife. For our one year aniverary I created a dashboard displaying several metrics of our relationship as analyzed by our text messages. Note: this is a stupid idea. Note2: but she married me anyway, so...")

