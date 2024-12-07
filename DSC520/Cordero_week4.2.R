# Assignment: ASSIGNMENT 4.2
# Name: Cordero, Joaquin
# Date: 2024-06-29

library(dplyr)

scores <- read.csv("scores.csv")

head(scores)
glimpse(scores)

scores_arrange <- scores %>% arrange(Score)

scores_duplicated <- scores_arrange[duplicated(scores_arrange), ]
print(scores_duplicated)

scores_unique <- scores_arrange[!duplicated(scores_arrange), ]
print(scores_unique)

#1.What are the observational units in this study?
#-The observational units in this study are the two sections, the total grade
#received, and the count of students that received that total grade.

#2.Identify the variables mentioned in the narrative paragraph and determine 
#which are categorical and quantitative?
#-Categorical: the two sections (Sports or Regular)
#-Quantitative: Total Grade and course grade

#3.Create one variable to hold a subset of your data set that contains only the 
#Regular Section and one variable for the Sports Section.

#4.
regular_section <- scores[scores$Section == "Regular", ]

x_regular <- regular_section$Count
y_regular <- regular_section$Score
plot(x_regular, y_regular, main = "Course - Regular")

sports_section <- scores[scores$Section == "Sports", ]

x_sports <- sports_section$Count
y_sports <- sports_section$Score
plot(x_sports, y_sports, main = "Course - Sports")

#4a.Comparing and contrasting the point distributions between the two section, 
#looking at both tendency and consistency: Can you say that one section tended 
#to score more points than the other? Justify and explain your answer.
#-Looking at the point distributions between the two sections, it looks like the 
#Regular course tended to score more points than Sports course. This is because
#more students in the 20 range per total grade earned scored higher than 320.

#4b.Did every student in one section score more points than every student in 
#the other section? If not, explain what a statistical tendency 
#means in this context.
#Yes, for the sports course students tend to score above 300. However, for the
#regular course students did not score more points than other students. In this 
#context statistical tendency is the grade most students would receive.

#4c.What could be one additional variable that was not mentioned in the 
#narrative that could be influencing the point distributions between the two 
#sections?
#-A variable that could be influencing the point distributions between the two 
#sections could be the prior knowledge student have. Some students would know
#more about sports than others and some would have no interest in sports at all.

