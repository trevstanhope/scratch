% with an expression
expression = sym('x-2')
solution = solve(expression)
result = double(solution)

% with an equation
solution2 = solve('y = x - 2')
double(ans)
