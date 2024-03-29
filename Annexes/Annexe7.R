library("RColorBrewer")
#Importing data
daily <- read_excel("daily.xlsx")
daily=daily[-1,]
daily<- daily[nrow(daily):1,]

col_types = c("date", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric")

#Univariate analysis
#Variable : New Cases
#the min
min.N.Cases <- min(daily$`New Cases`)
#the max
max.N.Cases <- max(daily$`New Cases`)
#The support
range(daily$`New Cases`)
#The mean
mean.N.Cases <- mean(daily$`New Cases`)
#The variance
var.N.Cases <- var(daily$`New Cases`)
#The standard deviation
sd.N.Cases <- sd(daily$`New Cases`)
#Median
median.N.Cases <- median(daily$`New Cases`)
#Quantiles
quantile(daily$`New Cases`)
#Summary
summary(daily$`New Cases`)
#Boxplot
boxplot(daily$`New Cases`, col=c("light blue"), ylab= "Nouveaux cas confirm�s")
title("La boite � moustache des nouveaux cas")
#Horizontal boxplot
boxplot(daily$`New Cases`, horizontal=TRUE, xlab="New Cases", col=c("light blue"))
title("La boite � moustache horizontale des nouveax cas")
#Histogram
hist(daily$`New Cases` , breaks = 4, prob = T, main="Histogramme de la distribution des nouveaux cas confirm�s", col=blues9, xlab = "New Cases")
#The histogram of the centered reduced quantile distribution
hist(quantile(daily$`New Cases`), col=blues9, main='Histogramme des quantiles des nouveaux cas')
#Barplot
barplot(daily$`New Cases`, col=blues9, main="Graphique � barres des nouveaux cas confirm�s",ylab="Les nouveaux cas confirm�s" )
##################################
#Variable: New Deaths
#min
min.N.Deaths <- min(daily$`New Deaths`)
#max
max.N.Deaths <- max(daily$`New Deaths`)
#support
range(daily$`New Deaths`)
#mean
mean.N.Deaths <- mean(daily$`New Deaths`)
#variance
var.N.Deaths <- var(daily$`New Deaths`)
#standard deviation
sd.N.Deaths <- sd(daily$`New Deaths`)
#median
median.N.Deaths <- median(daily$`New Deaths`)
#Quantiles
quantile(daily$`New Deaths`)
#Summary
summary(daily$`New Deaths`)
#Boxplot
boxplot(daily$`New Deaths`, col=c("red4"), ylab= "Nouveaux d�c�s")
title("La boite � moustache des nouveaux d�c�s")
#Horizontal boxplot
boxplot(daily$`New Deaths`, horizontal=TRUE, col="red4", ylab="Les nouveaux d�c�s")
title("La boite � moustache horizontale des nouveax d�c�s")
#Histogram
hist(daily$`New Deaths`, main="Histogramme des nouveaux d�c�s", prob=T,xlab="Les nouveaux d�c�s", ylab="Fr�quence", col=brewer.pal(n = 8, name = 'YlOrRd'))
#The histogram of the centered reduced quantile distribution
hist(quantile(daily$`New Deaths`), col="red4", xlab="les quantiles des nouveaux d�c�s", ylab="Fr�quence", main="Histogramme de la distribution des quantiles des nouveaux d�c�s")
#barplot
barplot(daily$`New Deaths`, col=brewer.pal(n = 8, name = 'YlOrRd'), xlab="les nouveaux d�c�s", ylab="Fr�quence", main="Histogramme de la distribution des quantiles des nouveaux d�c�s")
###################################
#variable: New Recoveries
#min
min.N.Recoveries <- min(daily$`New Recoveries`)
#max
max.N.Recoveries <- max(daily$`New Recoveries`)
#support
range(daily$`New Recoveries`)
#mean
mean.N.Recoveries <- mean(daily$`New Recoveries`)
#variance
var.N.Recoveries <- var(daily$`New Recoveries`)
#standard deviation
sd.N.Recoveries <- sd(daily$`New Recoveries`)
#median
median.N.Recoveries <- median(daily$`New Recoveries`)
#Quantiles
quantile(daily$`New Recoveries`)
#summary
summary(daily$`New Recoveries`)
#Boxplot
boxplot(daily$`New Recoveries`, col="light green", ylab= "Nouvelles gu�rissons")
title("La boite � moustache des nouvelles gu�rissons")
#La boite � moustache horizontale
boxplot(daily$`New Recoveries`, horizontal=TRUE, col="light green", ylab="Les nouvelles gu�rissons")
title("La boite � moustache horizontale des nouvelles gu�rissons")
#Histogram
hist(daily$`New Recoveries`, col="light green",prob=T, ylab="Densit�", xlab="Les nouvelles gu�rissons", main="Histogramme des nouvelles gu�risons confirm�s")
#The histogram of the centered reduced quantile distribution
hist(quantile(daily$`New Recoveries`), col="light green", ylab="Fr�quence", xlab="Les quantiles des nouvelles gu�rissons", main="Histogramme de la distribution des quantiles des nouvelles gu�rissons")
#barplot
barplot(daily$`New Recoveries`, col=brewer.pal(n = 8, name = 'YlGn'), main="Graphes � barres des nouvelles gu�rissons", ylab="Les nouvelles gu�rissons")
#################################
#variable: Active Cases
#min
min.Active <- min(daily$`Active Cases`)
#max
max.Active <- max(daily$`Active Cases`)
#support
range(daily$`Active Cases`)
#moyenne
mean.Active <- mean(daily$`Active Cases`)
#variance
var.Active <- var(daily$`Active Cases`)
#standard deviation
sd.Active <- sd(daily$`Active Cases`)
#median
median.Active <- median(daily$`Active Cases`)
#Quantiles
quantile(daily$`Active Cases`)
#Summary
summary(daily$`Active Cases`)
#Boxplot
boxplot(daily$`Active Cases`, col="purple", main="La boite � moustache des cas actifs", ylab="Les cas actifs")
title("La boite � moustache des cas actifs")
#Horizontal boxplot
boxplot(daily$`Active Cases`, horizontal=TRUE, col="purple", main="La boite � moustache horizontale des cas actifs", ylab="Les cas actifs")
title("La boite � moustache horizontale des cas actifs")
#Histogram
hist(daily$`Active Cases`, col=brewer.pal(n = 8, name = 'Purples'), main="Histogramme des cas actifs", ylab="Fr�quence", xlab="Cas actifs")
#The histogram of the centered reduced quantile distribution
hist(quantile(daily$`Active Cases`), col="purple", ylab="Fr�quence", xlab="Les quantiles des cas actifs", main="Histogramme de la distribution des quantiles des cas actifs ")
#barplot
barplot(daily$`Active Cases`, col=brewer.pal(n = 8, name = 'Purples'), ylab="Les cas actifs", main="Graphe � barres des cas actifs ")

