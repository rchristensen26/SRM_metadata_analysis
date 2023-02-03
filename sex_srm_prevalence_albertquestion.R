# Albert: It looks odd that the general SRMM prevalence is 31%, 
# but the prevalence of either males or females is only 21%. 
# Why is that? Is sex data more often available for non-infants?
library(ggplot2)
df <- hgm_subject_df

ggplot(df, aes(y = age_years)) +
  geom_histogram()