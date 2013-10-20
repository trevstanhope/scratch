### Lists, lists.R
### Trevor Stanhope

## E.g.
Family <- list(name="Fred", wife="Mary", no.children=3, child.ages=c(4,7,9))
Family [[1]]; Family[[2]]; Family[[3]]; Family[[4]] # Family[[4]] is a vector subscripted array
Family [[4]][1] # gives the first value in Family[[4]]
Family$child.names[1] # same as Family$child.ages[1]
Family$name # same as Family[[1]]
Family[["name"]] # same as Family$name
length(Family) # gives the length of top-level components

## Useful techniques
x <- "name"; Lst[[x]]

## Pattern Matching
Words <- list(coefficients="leading numbers", covariance="similar differences")
Words$coe # will match for Words$coefficients
Words$cov # will match for Words$covariance

## Augment
Family[5] <- list(matrix=Mat)

## Concatenate
list.ABC <- c(list.A, list.B, list.C)

## Data Frames
# There are specific rules for being a data.frame.
# 1. The components must be vectors (numeric, character, or logical), factors, numeric matrices, lists, or other data frames.
# 2. Matrices, lists, and data frames provide as many variables to the new data frame as they have columns, elements, or variables, respectively.
# 3. Numeric vectors, logicals and factors are included as is, and character vectors are coerced to be factors, whose levels are the unique values appearing in the vector.
# 4. Vector structures appearing as variables of the data frame must all have the same length, and matrix structures must all have the same row size.
accountants <- data.frame(home=statef, loot=incomes, shot=incomef)
as.data.frame(List) # if a list meets the requirements

## The function, attach()
# Makes a dataframe's components available as variables.
lentils <- list(u=1, v=2, w=3)
attach(lentils); x <- u - v+w
lentils$u <- v+w # will change the component in the dataframe

## The function, detach()
# Makes a dataframe's variables non-available.
detach(lentils)

## The function, search()
search() # lists all attached data.frames, lists and packages are included in the R path
attach(lentils)
ls("lentils") # same as ls(2)
detach("lentils")
