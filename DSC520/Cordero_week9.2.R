# Assignment: ASSIGNMENT 9.2
# Name: Joaquin Cordero
# Date: 2024-07-25

#install.packages("foreign")
library(foreign)
library(tidyr)
library(dplyr)
#install.packages("caTools")
library(caTools)

# ts = Thoraric Surgery
ts_data <- read.arff("ThoraricSurgery.arff") 
# bc = binary classifier
bc_data <- read.csv("binary-classifier-data.csv")

ts_split <- sample.split(ts_data, SplitRatio = 0.8)
 
ts_train <- subset(ts_data, ts_split == "TRUE")
ts_test <- subset(ts_data, ts_split == "FALSE")
# 1.b.i
ts_model1 <- glm(Risk1Yr ~ AGE + PRE17 + PRE19 + PRE30, data = ts_train, family = 'binomial')
summary(ts_model1)

# 1.b.ii
#according to the summary, variables PRE17 and PRE30 had the greatest effect on survival
#rate based on their p-values

# 1.b.iii
ts_preds <- predict(ts_model1, ts_test, type = "response")
ts_preds
 
ts_preds <- predict(ts_model1, ts_train, type = "response")
ts_preds
 
ts_confmatrix <- table(Actual_Value=ts_train$Risk1Yr, Predicted_Value = ts_preds > 0.5)
ts_confmatrix
 
ts_accuracy <- ts_confmatrix[1,1] / sum(ts_confmatrix)
ts_accuracy

# 2.b. 
bc_split <- sample.split(bc_data, SplitRatio = 0.8)

bc_train <- subset(bc_data, bc_split == "TRUE")
bc_test <- subset(bc_data, bc_split == "FALSE")

bc_model1 <- glm(label ~ x + y, data = bc_train, family = 'binomial')
summary(bc_model1)

bc_preds <- predict(bc_model1, bc_test, type = "response")

bc_confmatrix <- table(Actual_Value= bc_test$label, Predicted_Value = bc_preds > 0.5)
bc_confmatrix

bc_accuracy <- (bc_confmatrix[1,1] + bc_confmatrix[2,2]) / sum(bc_confmatrix)

# 2.b.i
bc_accuracy
