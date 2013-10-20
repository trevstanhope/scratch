### Vectors, vectors.R
### Trevor Stanhope

## algebra
c(10.4, 5.6, 3.1, 6.4, 21.7) -> x
a <- c(x, 0, x) 
b <- 2*a + b + 1
sort(x) -> c

## sequences
1:30 -> s1
seq(-5, 5, by=.2) -> s3

## logics
temp <- x > 13 ## makes temp of length x, where an entry is FALSE if the condition is unmet

## missing and not-a-number values
is.na(x)
d <- c(1:3,NA); ind <- is.na(d)
is.nan(x) # returns TRUE only if not-a-number

## indexing vectors
e <- d[!is.na(d)] # returns a vector removing the NA values of x
(d+1)[(!is.na(d)) & d>0] -> f # returns a vector x+1, less the NA values.

## strings
itu <- c(1:4)
names(itu) <- c("Alpha", "Bravo", "Charlie", "Delta")
matches <- itu[c("Alpha","Charlie")]







