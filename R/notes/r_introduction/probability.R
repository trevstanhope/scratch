### Probability, probability.R
### Trevor Stanhope

## Probabilistic Functions
beta(shape1, shape2, ncp)
binom(size, prob)
cauchy(location, scale)
chisq(df, ncp)
exp(rate)
f(df1, df2, ncp)
gamma(shape, scale)
geom(prob)
hyper(m, n, k)
lnorm(meanlog, sdlog)
logis(location, scale)
nbinom(size, prob)
norm(mean, sd)
pois(lambda)
signrank(n)
t(df, ncp)
unif(min, max)
weibull(shape, scale)
wilcox(m, n)

## Calling the Functions
## Affix ‘d’ for density, ‘p’ for CDF, ‘q’ for the quantile function and ‘r’ for random simulation
a <- 2*pt(-2.43, df = 13) # 2-tailed p-value for t distribution
b <- qf(0.01, 2, 7, lower.tail = FALSE) # upper 1% point for an F(2, 7) distribution

## Plotting Probabilities
attach(faithful)
summary(eruptions)
fivenum(eruptions)
stem(eruptions) # stem-and-leaf plot
hist(eruptions) # histogram plot
hist(eruptions, seq(1.6, 5.2, 0.2), prob=TRUE) # make the bins smaller, make a plot of density
lines(density(eruptions, bw=0.1))
rug(eruptions) # show the actual data points
plot(ecdf(eruptions), do.points=FALSE, verticals=TRUE)
long <- eruptions[eruptions > 3] # eruptions longer than 3 minutes
plot(ecdf(long), do.points=FALSE, verticals=TRUE)
x <- seq(3, 5.4, 0.01)
lines(x, pnorm(x, mean=mean(long), sd=sqrt(var(long))), lty=3) # plotf = pnorm(sequence, mean, sd)
par(pty="s") # arrange for a square figure region
qqnorm(long); qqline(long)
x <- rt(250, df = 5)
qqnorm(x); qqline(x)
qqplot(qt(ppoints(250), df = 5), x, xlab = "Q-Q plot for t dsn")
qqline(x)
shapiro.test(long) # Shapiro normality test
ks.test(long, "pnorm", mean = mean(long), sd = sqrt(var(long))) # Kolmogorov-Smirnov test

## one and two sample tests
boxplot(A,B) # if A and B are arrays
t.test(A, B)
var.test(A, B)
wilcox.test(A, B) # The two-sample Wilcoxon (or Mann-Whitney) test only assumes a common continuous distribution under the null hypothesis.

