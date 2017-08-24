library(dplyr)
library(ggplot2)

fragrance = read.csv('fragInfoUnique.csv',header = TRUE)
summary(fragrance)
View(fragrance)

fragrance %>% 
  ggplot(aes(x=woody)) + geom_histogram()

fragrance %>% ggplot(aes(x=woody, y=like)) + geom_point() +
  scale_x_log10() + geom_smooth()

fragrance %>% ggplot(aes(x=citrus, y=love)) + geom_point() +
  scale_x_log10() + geom_smooth()

fragrance$"A Lab on Fire" %>% ggplot(aes(x=love)) + geom_point()
