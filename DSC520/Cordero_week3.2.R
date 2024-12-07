# Assignment: ASSIGNMENT 3.2
# Name: Cordero, Joaquin
# Date: 2024-06-22

library(ggplot2)
library(dplyr)
library(stats)
library(pastecs)

acs_dataset <- read.csv("acs-14-1yr-s0201.csv")
getwd()

#Id - Data Type: integer , Intent: unique identifier for each row
#Id2 - Data Type: integer , Intent: last 4-5 digits of 'Id' and unique identifier for each row 
#Geography - Data Type: text , Intent: unique identifier for each location 
#PopGroupID - Data Type: integer , Intent: unique identifier for 'Total population'
#POPGROUP.display.label - Data Type: text , Intent: unique identifier for 'PopGroupID' 
#RacesReported - Data Type: integer , Intent: represents the population in each geography 
#HSDegree - Data Type: integer , Intent: percent of the population that has HS degree
#BachDegree - Data Type: integer , Intent: percent of the population that has bachelor degree

str(acs_dataset)
nrow(acs_dataset)
ncol(acs_dataset)

mean_HSDegree <- mean(acs_dataset$HSDegree)
sd_HSDegree <- sd(acs_dataset$HSDegree)

hsd_plot <- ggplot(acs_dataset, aes(x = HSDegree,)) + geom_histogram(binwidth = 2) 
hsd_plot <- hsd_plot + labs(x = "Percent of HSDegree", y = "count", title = "HSDegree Histogram Plot" )
print(hsd_plot)

#1.Based on what you see in this histogram, is the data distribution unimodal?
#-Yes, based on the histogram the data distribution is unimodal.

#2.Is it approximately symmetrical?
#-No, it is not symmetrical?

#3.Is it approximately bell-shaped?
#-Yes, it is approximately bell-shaped

#4.Is it approximately normal?
#-No, it is not normal shaped

#5.If not normal, is the distribution skewed? If so, in which direction?
#-The distribution is skewed left

#6.Include a normal curve to the Histogram that you plotted.
hsd_plot <- hsd_plot + stat_function(fun = dnorm, args = list(mean = mean_HSDegree, sd = sd_HSDegree), 
                          color = "red", size = 2) 
print(hsd_plot)

#7.Explain whether a normal distribution can accurately be used as a model for this data.
#-No, I do not believe a normal distribution can accurately be used as a model for this data

hsd_prob_plot <- ggplot(acs_dataset, aes(sample = HSDegree)) + stat_qq(distribution = qnorm, dparams = list(mean = mean(acs_dataset$HSDegree), sd = sd(acs_dataset$HSDegree)))
print(hsd_prob_plot)

#1.Based on what you see in this probability plot, is the distribution approximately normal? Explain how you know.
#-No, because the plotted points bends down

#2.If not normal, is the distribution skewed? If so, in which direction? Explain how you know.
#-The distribution is skewed left becuase the plotted points curve down 

stat.desc(acs_dataset$HSDegree)

#Skew measures the dataset's asymmetry and the probability distribution. Kurtosis measures the outliers in the dataset. Z-score can measure how many standard deviation away from the dataset's mean a data point is. A change in sample size can change how accurate these are because smaller sample sizes will tend to show less of the overall picture.