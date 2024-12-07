# Assignment: ASSIGNMENT 7.2
# Name: Joaquin Cordero
# Date: 2024-07-17

library(readxl)
library(dplyr)
library(GGally)

my_data <- read.csv('student-survey.csv')

reading_tv <- plot(x = my_data$TimeReading, y = my_data$TimeTV)

reading_happiness <- plot(x = my_data$TimeReading, y = my_data$Happiness)

tv_happiness <- plot(x = my_data$TimeTV, y = my_data$Happiness)


#3.a. The variables TimeReading and TimeTV slope indicate a negative relationship
#3.b. The variables TimeReading and Happiness slope somewhat indicate a negative relationship
#3.c. The variables TimeTV and Happiness slop indicate a positive relationship

cov_matrix <- cov(my_data$TimeReading, my_data$TimeTV, my_data$Happiness)

reading_tv_happiness <- my_data %>% select(TimeReading, TimeTV, Happiness)

cov_matrix <- cov(reading_tv_happiness) 

ggpairs(cov_matrix[])

cor_matrix <- cor(reading_tv_happiness)

ggpairs(cor_matrix[])

cor(my_data$TimeReading, my_data$TimeTV)

install.packages("http://miktex.org")
