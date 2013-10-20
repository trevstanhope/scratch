### Arrays, arrays.R
### Trevor Stanhope

## E.g.
z <- 1:1500
dim(z) <- c(3,5,100); dim(z) # can store information backwards

## E.g.
x <- array(1:20, dim=c(4,5)); x
i <- array(c(1:3,3:1), dim=c(3,2)); i
x[i]; x[i] <- 0; x

## E.g. index matrices.
Xb <- matrix(0, n, b)
Xv <- matrix(0, n, v)
ib <- cbind(1:n, blocks)
iv <- cbind(1:n, varieties)
Xb[ib] <- 1
Xv[iv] <- 1
X <- cbind(Xb, Xv)
N <- crossprod(Xb, Xv) # will give you the incidence matrix
N <- table(blocks, varieties) # will also give you the incidence matrix

## The array() function.
h <- 1:24
Z <- array(h, dim=c(3,4,2)) # where: Z <- array(data_vector, dim_vector )
Z <- h
dim(Z) <- c(3,4,2)
# dim(Z) stands for the dimension vector c(3,4,2), and Z[1:24] stands for the data vector as it was in h, and Z[]

## Outer product (dot product).
a <- c(1:10)
b <- c((1:10)+1)
a_dot_b <- a %o% b; a_dot_b
a_dot_b <- outer(a, b, "*"); a_dot_b # same as previous

## moar outer maths
f <- function(x, y) {cos(y)/(1 + x^2)}
z <- outer(x, y, f)

## e.g. determinants density
d <- outer(0:9, 0:9)
fr <- table(outer(d, d, "-"))
plot(as.numeric(names(fr)), 
    fr, 
    type="h", # bar graph
    xlab="Determinant", # sets x axis name
    ylab="Frequency" # sets y axis name
) 

## Transposing arrays
A <- array(1:4, dim=c(2,2)
B <- t(A) 
B <- aperm(A, c(2,1)) # does the same thing

## Matrix multiplication
a <- array(1:4, dim=c(2,2)
b <- array((1:4)+1, dim=c(2,2))
a * b # does dot product
a %*% b # does polynomial (matrix) multiplication

## Index matrices
x <- array(1:20, dim=c(4,5)) # make 4 by 5
i <- array(c(1:3,3:1), dim=c(3,2)) # make 3 by 2
x[i] # exract values from x using rows of i as coordinates

## Solving
solve(A, b) # solves x = [A]*b

## Eigenvalues
# let Sym be a symmetric matrix
ev <- eigen(Sym)
# now ev$val will give the vector of eigenvalues
# and ev$vec will give the matrix of eigenvectors
# to just calculate the values, not the vectors
evals1 <- eigen(Sym)$values
evals2 <- eigen(Sm, only.values = TRUE)$values # less mem

## Concatenation
cbind(A,B) # concatenates A and B column-wise
rbind(A,B) # concaternates A and B row-wise
X <- cbind(1, A, B) # makes X with first columns all ones
vec <- c(A,B) # regards A and B as vectors and concats them dimless
x <- cbind((vec <- as.vector(A),(vec <- as.vector(B)) # same



