### Read Data, read_data.R
### Trevor Stanhope

## read.table()
HousePrice <- read.table("houses.data") # assumings there's a file, houses.data, in the path

## scan()
inp <- scan("input.dat", list("",0,0))
label <- inp[[1]]; x <- inp[[2]]; y <- inp[[3]]; label, x, y
inp <- scan("input.dat", list(id="", x=0, y=0))
label <- inp$id; x <- inp$x; y <- inp$y; label; label, x, y
a <- scan("light.dat", 0) # read as a vector from position 0
A <- matrix(a, ncol=5, byrow=TRUE) # convert back to matrix

## Reading Data Sets
data()
data(infert)
data(package="rpart")
data(Puromycin, package="datasets")

## Editting Data Sets
xnew <- edit(xold)
fix(xold) # same idea as 'xold <- edit(xold)'
xnew <- edit(data.frame()) # add new data with spreadsheet interface




