# Assignment: Final Project
# Name: Joaquin Cordero
# Date: 2024-07-25

library(readxl)
library(tidyr)
library(dplyr)
library(stringr)
library(ggplot2)

ca_house_data <- read.csv("California_Housing_CitiesAdded.csv")
ca_crime <- read.csv("rows.csv")
ca_income <- read.csv("HDPulse_data_export.csv") %>% rename('median_household_income' = Value..Dollars.) %>% 
  slice(-c(1, 2))
ca_income2 <- read_excel("hci_living_wage_770_pl_co_re_ca_9-29-13-ada.xlsx")

my_data_house <- ca_house_data %>% 
  select(Median_House_Value, City) %>% 
  distinct(City, .keep_all = TRUE) %>% 
  arrange(City) %>% 
  rename('County' = City)

my_data_income <- ca_income %>% 
  select(County, median_household_income) %>% 
  mutate(median_household_income = median_household_income * 1000) %>% 
  arrange(County) %>% 
  mutate(County = str_remove(County, " County"))

my_data_crime <- ca_crime %>% 
  select(county_name, ratex1000) %>% 
  slice(-c(1,2,3,4,5)) %>% 
  distinct(county_name, .keep_all = TRUE) %>% 
  rename('County' = county_name) %>% 
  rename('crime_ratex1000' = ratex1000)

combined_data <- my_data_income %>% 
  inner_join(my_data_house, by = "County") %>% 
  inner_join(my_data_crime, by = "County") 

affordableHousing <- combined_data %>% 
  arrange(Median_House_Value)

head(affordableHousing, 5)
tail(affordableHousing, 5)

safest_county <- combined_data %>% 
  arrange(crime_ratex1000)

head(safest_county, 5)
tail(safest_county, 5)

highest_income <- combined_data %>% 
  arrange(median_household_income)

head(highest_income, 5)
tail(highest_income, 5)


cd_split <- sample.split(combined_data, SplitRatio = 0.8)

cd_train <- subset(combined_data, cd_split == "TRUE")
cd_test <- subset(combined_data, cd_split == "FALSE")

cd_model1 <- lm(Median_House_Value ~ median_household_income + crime_ratex1000, data = cd_train)
summary(cd_model1)

cd_resid <- residuals(cd_model1)

plot(cd_model1$fitted.values, cd_resid) + abline(h=0, col = "red")

