library(tidyverse)

size <- c(10, 50, 100, 150, 200, 250, 500, 750, 1000)
time <- c(0.02311448205728084, 0.21002487500663847, 0.741171, 1.1935353100000001, 2.1499613220000002, 3.3981936269999995, 13.271662949, 31.467654691000003
, 57.638190504)
df <- data.frame(size, time)
size_pred <- data.frame(size=c(1e3, 5e3, 1e4))
size_test <- data.frame(size=1100, time=62.191481747)

g <- ggplot(df, aes(x=size, y=time)) +
  geom_point() +
  geom_smooth(method="loess", se = F) +
  geom_point(data= size_test, mapping = aes(x=size, y=time), col = "green") + 
  ylim(c(0, 100))
g

# fit non-linear model
mod <- nls(time ~ exp(a + b * size), data = df, start = list(a = 0, b = 0))
size_pred$time <- predict(mod, newdata=size_pred)

g + 
  geom_point(data= size_pred, mapping = aes(x=size, y=time), col = "red") + 
  geom_line(data= size_pred, col = 'red') +
  scale_y_log10()

