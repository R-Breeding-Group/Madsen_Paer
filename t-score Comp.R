#viziluisation of t-score comparison 

install.packages("naniar")
install.packages("gglpot2")
install.packages("reshape2")

library(ggthemes)
library(reshape2)
library(naniar)
library(tidyverse)
library(ggplot2)


Means_Comparison <- read_csv("Means Comparison.csv")
C92_C18_data <- read_csv("C92-C18_data.csv")

data1 <- replace_with_na_all(data = C92_C18_data, condition = ~.x == ".")
data1_melt <- melt(data1, id.vars = "VARIETY")
data1_melt$value = as.numeric(data1_melt$value)



ggplot(data = subset(data1_melt,!is.na(value)), aes(x = variable, y = value, fill = VARIETY))+
  theme_calc()+
  geom_area(aes(color = VARIETY), size = 2.5)+
  labs(title = "t-Score Comparison vs. Madsen", x = "Trait", y = "")+
  theme(axis.text.x = element_text(angle = 40, hjust = 1))+
  guides(size = "none")
  