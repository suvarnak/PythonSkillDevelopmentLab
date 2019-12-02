theme_set(theme_gray(base_size=12, base_family="HiraKakuProN-W3"))
library(ggplot2)


employee <- c('John Doe','Peter Gynn','Jolie Hope')
salary <- c(21000, 23400, 26800)
startdate <- as.Date(c('2010-11-1','2008-3-25','2007-3-14'))

employ.data <- data.frame(employee, salary, startdate)
ggplot(employ.data, aes(employee, salary)) + 
  geom_line() +
  ggtitle("?????????") +
  xlab("?????????") +
  ylab("??????")
