### Grouping, Loops and Conditions, grouping_loops_conditions.R
### Trevor Stanhope

## If Statements
# if (expr_1) expr_2 else expr_3 # where expr 1 must evaluate to a single logical value

## Loops (For, Repeat, While)
# for (name in expr_1 ) expr_2 # 'name' is the loop variable, 'expr_1' is a vector like 1:20
xc <- split(x, ind)
yc <- split(y, ind)
for (i in 1:length(yc)) {
    plot(xc[[i]], yc[[i]])
    abline(lsfit(xc[[i]], yc[[i]]))
}

# repeat expr
# while(condition) expr
