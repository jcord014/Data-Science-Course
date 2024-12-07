# Assignment: ASSIGNMENT 8.2
# Name: Joaquin Cordero
# Date: 2024-07-25

library(readxl)
library(dplyr)
library(ggplot2)
library(Metrics)

housing_data <- read_xlsx("week-6-housing.xlsx") %>% 
  rename(sale_price = 'Sale Price')

my_data <- housing_data %>% 
  select(sale_price, addr_full, sq_ft_lot) %>% 
  distinct(addr_full, .keep_all = TRUE) 
  
duplicated(my_data$addr_full)

# 1. I selected only 3 columns from the original data that is currently needed.
# Created a new data set using Sale Price, addr_full, and sq_ft_lot from the original.
# To remove duplicates, I used addr_full to remove any duplicated rows because a unique entry should
# not have the same address. I used duplicated() function prior to and after using distinct() function
# to check for any duplicate entries. Lastly, renamed column 'Sale Price' to sale_price.

#2.
sq_ft_price_lm <- lm(sale_price ~ sq_ft_lot, data = my_data)
sq_ft_price_lm

#3.
summary(sq_ft_price_lm)

#For every additional square foot, price is expected to increase by 0.826.

#4.
residuals <- resid(sq_ft_price_lm)

plot(sq_ft_price_lm$fitted.values, residuals) + abline(h=0, col = "red")

# The model indicates a cluster and not evenly distributed on the horizontal line at 0.
# May not be representing the relationship properly.

#5.
qqnorm(residuals)
qqline(residuals, col = "red")

#The residuals do not meet the normality assumption since it forms an S-shaped curve.

#6.
second_model <- housing_data %>%
  select(sale_price, addr_full, square_feet_total_living, bedrooms, 
         bath_full_count, year_built) %>% 
  distinct(addr_full, .keep_all = TRUE) 

second_model_lm <- lm(sale_price ~ square_feet_total_living + bedrooms + 
                        bath_full_count + year_built, data = second_model)
second_model_lm

#Picking these variables may add explanatory value to the model because I believe
#these are variables buyers would be interested in. Having these variables might
#increase sale price.

#7.
summary(second_model_lm)
#Variables square_feet_total_living and year_built are highly significant predictors.
#While variable bath_full_count is a low significant predictor.
#For each additional square foot of living sale price is expected to increase by $167.6
#For each additional bedroom sale price is actually expected to decrease by -$16,150.
#For each additional year price is expected to increase by $3,196 meaning newer homes are 
#priced higher.

#8.
sec_mod_residuals <- resid(second_model_lm)

plot(second_model_lm$fitted.values, sec_mod_residuals) + abline(h=0, col = "red")

#The second model is clustered and not evenly distributed on the horizontal line at 0.
#Again, this may not be representing the relationship properly.

#9.
qqnorm(sec_mod_residuals)
qqline(sec_mod_residuals, col = 'red')

#My residuals do not meet the normality assumption since it forms an S-shaped curve as well.

#10.
anova(sq_ft_price_lm, second_model_lm)
#Yes, there is significant improvements between the two models. The p-value shows that 
#the additional variables are important to the model.

#11.
#The model is biased since it shows a clear pattern that does not meet normal distribution.

#12.
#12.2.1
preds_model1 <- predict(object = sq_ft_price_lm, newdata = housing_data)
#12.2.2
rmse_model1 <- rmse(housing_data$sale_price, preds_model1)

#12.3
rmse_model1

#12.4
preds_model2 <- predict(object = second_model_lm, newdata = housing_data)

rmse_model2 <- rmse(housing_data$sale_price, preds_model2)

rmse_model2

#12.5
rmse_model1 - rmse_model2
#Yes the second model's RMSE improved from the first model's RMSE. It improved by 43834.47.