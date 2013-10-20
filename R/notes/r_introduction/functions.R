## Function for the two sample t-statistic
tstat2 <- function(arg_1, arg_2) {
    n1 <- length(y1); n2 <- length(y2)
    yb1 <- mean(y1);
    yb2 <- mean(y2)
    s1 <- var(y1);
    s2 <- var(y2)
    s <- ((n1-1)*s1 + (n2-1)*s2)/(n1+n2-2)
    tst <- (yb1 - yb2)/sqrt(s*(1/n1 + 1/n2))
    tst
}

## MATLAB's '\' operator emulation
bslash <- function(X, y) {
    X <- qr(X)
    qr.coef(X, y)
}
regcoeff <- bslash(Xmatrix, Yvector); regcoeff

## Defining a binary operator
"%!%" <- function(X, y) {
X <- qr(X)
qr.coef(X, y)
} # can then be run with: X%!%Y

## Global assignment
function <-(...) {
variable <<- ... # assigns variable globally when function is run
}

## Dropping Dimension Names
# Remove all dimension names from an array for compact printing.
no.dimnames <- function(a) {
    d <- list()
    l <- 0
    for(i in dim(a)) { # for-loop lasts for i<dim(a)b
        d[[l <- l + 1]] <- rep("", i)
    }
    dimnames(a) <- d
    a
}

# Can also be done with:
temp <- X
dimnames(temp) <- list(rep("", nrow(X)), rep("", ncol(X)))
temp; rm(temp)

## Scope, S+ uses static scope, R uses lexical scope
# S+ looks for a global variable called 'n', while R first looks for a variable called 'n' in the environment created when cube was invoked.
f <- function(x) {
    y <- 2*x
    print(x) # formal parameter i.e. argument
    print(y) # local variable
    print(z) # free variable
}

cube <- function(n) {
    sq <- function() { # this function will fail in S/S+ because n is undefined
        n*n
    }
    n*sq()
}

## 
bdeff <- function(blocks, varieties) {
    blocks <- as.factor(blocks) # minor safety move
    b <- length(levels(blocks))
    varieties <- as.factor(varieties) # minor safety move
    v <- length(levels(varieties))
    K <- as.vector(table(blocks)) # remove dim attr
    R <- as.vector(table(varieties)) # remove dim attr
    N <- table(blocks, varieties)
    A <- 1/sqrt(K) * N * rep(1/sqrt(R), rep(b, v))
    sv <- svd(A)
    list(eff=1 - sv$d^2, blockcv=sv$u, varietycv=sv$v)
}

## Recursive Numerical Integration
area <- function(f, a, b, eps = 1.0e-06, lim = 10) {
    fun1 <- function(f, a, b, fa, fb, a0, eps, lim, fun) { # function ‘fun1’ is only visible inside ‘area’
        d <- (a + b)/2
        h <- (b - a)/4
        fd <- f(d)
        a1 <- h * (fa + fd)
        a2 <- h * (fd + fb)
        if(abs(a0 - a1 - a2) < eps || lim == 0)
        return(a1 + a2)
        else {
            return(fun(f, a, d, fa, fd, a1, eps, lim - 1, fun) +
            fun(f, d, b, fd, fb, a2, eps, lim - 1, fun))
        }
    }
    fa <- f(a)
    fb <- f(b)
    a0 <- ((fa + fb) * (b - a))/2
    fun1(f, a, b, fa, fb, a0, eps, lim, fun1)
}

