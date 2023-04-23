################# Bivariate study ########################
##Importing necessary libraries
library(plotly)
library(readxl)
library(lubridate)
library(ggplot2)
library(car)
library(corrplot)
#Importing data
daily <- read_excel('daily.xlsx')
region<-read.csv('https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/stats/regions.csv')
daily=daily[-1,]
##reverse the order of the data 
daily<- daily[nrow(daily):1,]
##cleaning
daily[c(4,5,6,9,10,11,14,16,17,18,19,20)] <- list(NULL)
daily
##columns type
col_types = c("date", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric")
##data distribution
daily1<-daily[153:192,]
daily1$jour=1:40
##x: the date and y: new confirmed cases
x1=daily1$jour; y1=daily1$`New Cases`
#cramer
cramersV(x1,y1)
##Covariance
cov(x1,y1)
##The linear correlation coefficient
cor(x1,y1)
#Interpretation: The value of the correlation coefficient in this case is close to 1, so the linear relationship between the two variables is strong.
##Determine the coefficients of the least squares line: â and ^b
a1<-cor(x1,y1)*(sd(y1)/sd(x1))
a1

b1<-mean(y1)-a1*mean(x1)
b1
##Let's find the least squares eq by an R fct
eq1<-lm(y1 ~ x1 )
eq1
#Interpretation: The value of the slope is equal to 49.16, so for each increase of 1 in the variable x1, there is an increase of 49.16 for new confirmed cases y1.
##Let's draw the scatter plot representing the new confirmed cases according to the dates
plot(x=x1, y=y1, main="Graphe nuage de points des nouveaux cas confirmés en fonction du temps",xlab='Nombre de jours',ylab='Nouveaux cas')
##Traçons maintenant la droite des moindres carrés dans le graphe nuage des points
abline(eq1, col = "red")
#Interpretation: The points are closer together around the line, which indicates that the correlation in this case is important
#Predictions: confidence and prediction interval
#Predicted values
fitted(eq1)
#scatterplot
scatterplot(y1~x1, regLine=list(method=lm, lty=1, lwd=2, col="red"),xlab = 'Nombre de jours',ylab = 'Nouveaux cas',main='Nuage  de points des nouveaux cas')
#The number of days of pediction
x=(41:55)
y=x*21.3+902.3
y
plot(x=x, y=y, main="Nuage de points des prédictions des nouveaux cas confirmés en fonction du temps",xlab='Nombre de jours',ylab='Nouveaux cas')
#The regression line is included in the confidence interval so our model is good.
##################################################################
##x: the date and y: new deaths
y2<-daily1$`New Deaths`
#cramer coef
cramersV(x1,y2)

##Covariance
cov(x1,y2)
#Interpretation: The covariance value in this case is positive, so both variables tend to increase.
#Then x1 and y1 are positively correlated.
##The linear correlation coefficient
cor(x1,y2)
#Regression equation
eq2<-lm(y2 ~ x1 )
eq2
#Interpretation: The value of the slope is equal to 0.02794, so for each increase of 1 in the variable x1, there is an increase of 0.02794 for new deaths y2.
#Let's draw the scatter plot that represents new deaths over time.
plot(x=x1, y=y2, main="Graphe nuage de points des nouveaux décès confirmés en fonction du temps",xlab = 'Nombre de jour',ylab='Nouveaux décès')
abline(eq2, col = "red")

#Predictions: confidence and prediction interval
fitted(eq2)# Predicted values
scatterplot(y2~x1, regLine=list(method=lm, lty=1, lwd=2, col="red"),xlab='Nombre de jours',ylab = 'Nouveaux décès',main='Nuage de points des nouveaux décès')
x=(41:55)
y=x*0.5728+15.7577
y
plot(x=x, y=y, main="Nuage de points des prédictions des nouveaux décès confirmés en fonction du temps",xlab='Nombre de jours',ylab='Nouveaux décès')
#The regression line is well understood in the interval of confidence which indicates a good result
#################################################################
##x: the date and y: new deaths
y3<-daily1$`New Recoveries`
#cramer coeff
cramersV(x1,y3)

##Covariance
cov(x1,y3)
#Interpretation: The value of the covariance in this case is positive, so both variables tend to increase.
#Then x1 and y2 are positively correlated.
##The linear correlation coefficient
cor(x1,y3)
##Let's find the least squares eq by a fct R
eq3<-lm(y3 ~ x1 )
eq3
#Interpretation: The value of the slope is equal to 3.199, so for each increase of 1 in the variable x1, there is an increase of 3.199 for the new cures y3.
##Let's draw the scatterplot graph that represents the new healings as a function of time
plot(x=x1, y=y3, main="Graphe nuage de points des guérissons en fonction du temps",xlab='Nombre de jours',ylab='Nouvelles guérisons')
##Now let's draw the least squares line in the scatterplot graph
abline(eq3, col = "red")

#Predictions: confidence and prediction interval
fitted(eq3)# predicted values 

scatterplot(y3~x1, regLine=list(method=lm, lty=1, lwd=2, col="red"),xlab='Nombre de jours',ylab='Nouvelles guérisons',main='Nuage de points des nouvelles guérisons')
x=(41:55)
y=x*26.67+504.80
y
plot(x=x, y=y, main="Nuage de points des prédictions des nouvelles guérisons confirmés en fonction du temps",xlab='Nombre de jours',ylab='Nouvelles guérisons')
#The regression line is included in the confidence interval so our model is correct.
####################################################################
##x: new cases and y: new deaths
y4<-daily1$`New Deaths`
x2<-daily1$`New Cases`
#cramer coeff
cramersV(x2,y4)

##Covariance
cov(x2,y4)
##The linear correlation coefficient
cor(x2,y4)
#Interpretation: the absolute value of the correlation coefficient in this case is far from 1, then the linear relationship between the two variables is weak.

##Let's find the regression eq
eq4<-lm(y4 ~ x2)
eq4
#Interpretation:
##Let's draw the scatterplot graph that represents the new deaths according to the new confirmed cases
plot(x=x2, y=y4, main="Graphe nuage de points des nouveaux décès en fonction des nouveaux cas confirmés",xlab='Nouveaux cas',ylab='Nouveaux décès')
##Now let's draw the least squares line in the scatterplot graph
abline(eq4, col = "red")
#Interpretation:
#Predictions: confidence and prediction interval
fitted(eq4)# predicted values
scatterplot(y4~x2, regLine=list(method=lm, lty=1, lwd=2, col="red"),xlab='Nouveaux cas',ylab='Nouveaux décès',main='Nuage de points des nouveaux décès en fonction des nouveaux cas')
#The regression line is included in the confidence interval so our model is good.
#########################################################################
##x: new cases and y: new recoveries
y5<-daily1$`New Recoveries`
#cramer coeff
cramersV(x2,y5)

##Covariance
cov(x2,y5)
##The linear correlation coefficient
cor(x2,y5)
##Let's find the regression eq
eq5<-lm(y5 ~ x2)
eq5
#Interpretation: The slope equals 0.4379, this means that when x2 increases by 1, y5 increases by 0.4379.
##Let's draw the scatterplot graph which represents the new recoveries according to the new confirmed cases
plot(x=x2, y=y5, main="Graphe nuage de points des nouvelles guérissons en fonction des nouveaux cas confirmés",xlab='Nouveaux cas',ylab='Nouvelles guérisons')
##Now let's draw the least squares line in the scatterplot graph
abline(eq5, col = "red")
#Interpretation: the points are distributed around the regression line, which indicates that our model is good
#Predictions: confidence and prediction interval
fitted(eq5)# predicted values
scatterplot(y5~x2, regLine=list(method=lm, lty=1, lwd=2, col="red"),xlab = 'Nouveaux cas',ylab='Nouvelles guérisons',main='Nuage de points des nouvelles guérisons en fonction des nouveaux cas')
#####################################################################
