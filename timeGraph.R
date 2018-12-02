library(tidyverse)

size <- c(10, 50, 100, 150, 200, 250, 500, 750, 1000)
time <- c(0.02311448205728084, 0.21002487500663847, 0.741171, 1.1935353100000001, 2.1499613220000002, 3.3981936269999995, 13.271662949, 31.467654691000003
, 57.638190504)
df <- data.frame(size, time)
size_pred <- data.frame(size=c(1e3, 1e4, 1e5, 1e6, 1e7))

ggplot(df, aes(x=size, y=time)) +
  geom_point() +
  geom_smooth(method="loess", se = F)

df$logTime <- log(df$time)
df$logSize <- log(df$size)
ggplot(df, aes(x=logSize, y=logTime)) +
  geom_point()

# fit non-linear model
mod <- nls(time ~ exp(a + b * size), data = df, start = list(a = 0, b = 0))
predict(mod, newdata=size_pred)
