# Assignment: ASSIGNMENT 5.2
# Name: Cordero, Joaquin
# Date: 2024-07-06

library(readxl)
library(stringr)
library(purrr)
library(dplyr)

data <- read_excel("week-6-housing.xlsx")

arrange_sale_price <- data %>% arrange(desc(data$`Sale Price`))

avg_sale_price <- data %>% summarize(avg = mean(`Sale Price`))

group_by_zone <- data %>% 
  group_by(zip5) %>% 
  summarize(avg = mean(`Sale Price`))

filtered_by_bedroom <- arrange_sale_price %>% 
  filter(bedrooms <= 3)

# data %>% rename('Sale Price'=sale_price)

my_data <- arrange_sale_price %>% 
  select(`Sale Date`, `Sale Price`, addr_full, zip5, bedrooms,
         bath_full_count, sq_ft_lot)

my_data <- my_data %>% mutate(`Sale Price`/sq_ft_lot) %>% 
  rename_at(8, ~'price_per_sq_ft') %>% rename_at(1, ~'sale_date') %>% 
  rename_at(2, ~'sale_price')

short_data <- my_data %>% select(sale_date, sale_price, addr_full, zip5)

data_no_null <- keep(data, is.numeric)

sale_price_check <- every(my_data$sale_price, is_character)

addr_full_zip <- cbind(data$addr_full, data$zip5)

bedrooms_specified <- rbind(data$bedrooms, data$`Sale Price`)

string_test <- strsplit(my_data$addr_full, " ")

cleaned_string_test <- gsub("^c\\(|\\)$", "", string_test)
View(cleaned_string_test)

cleaned_string_test <- gsub('"', '', strsplit(cleaned_string_test, ",")[[1]])

concatenated_string_test <- paste(cleaned_string_test, collapse = "/")
View(concatenated_string_test)

