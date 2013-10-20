### Objects, objects.R
### Trevor Stanhope

## fundamental qualities mode/length of a vector
x <- c(1:4) # e.g. a numerical vector
y <- as.character(x) # e.g. a character vector
z <- as.integer(y) # now x returns to a numeric vector
mode(x) # it's numeric
mode(y) # it's character
length(x) # it's 4 atoms long

## vector lengths
e <- numeric() # empty numeric vector
length(e) # is zero
e[3] <- 17 # is now 3 long
alpha <- 1:10
beta <- alpha[2 * 1:5] # only keeps the even indicies
length(alpha) <- 3 # sets the length of alpha to the first 3 indicies, truncating the vector

## attributes
a <- 1:10
attr(a, "dim") <- c(10,10)

## classes
unclass()

## factor() and tapply()
state <- c("tas","qld","sa","sa","sa","vic","nt","act","qld","nsw","wa","nsw","nsw","vic","vic","vic","nsw","qld","qld","vic","nt", "wa", "wa","qld", "sa", "tas","nsw", "nsw", "wa","act")
incomes <- c(60, 49, 40, 61, 64, 60, 59, 54, 62, 69, 70, 42, 56,61, 61, 61, 58, 51, 48, 65, 49, 49, 41, 48, 52, 46,59, 46, 58, 43)
statef <- factor(state); statef # makes state from character vector into a factor
levels(statef) # shows how many classes (states) there were in statef
incmeans <- tapply(incomes, statef, mean) # creates a means vector, with the component labeled by the levels in statef
# NOTE: tapply takes the values of incomes, and then groups them by the factors in statef, and applies mean() on each set




