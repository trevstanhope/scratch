%% normalize.m
% Returns normalized vector

function output = normalize(vector)
    divisor = norm(vector);
    output = vector/divisor;
