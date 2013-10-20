function [start_data] = get_data(str_conversion, str_start_unit)
% GET_DATA Gets data from the user and passes it back to the main program.
% Inputs are two strings indicating which unit conversion was requested
% and which unit is used for input data.
% Output is one vector of numeric values.
% This function is called by CLARK_L5

fprintf('You have chosen to convert %s. ', str_conversion)
k = input('How many value would you like to convert? '); % Get number of values
start_data = zeros(k,1); % Initialize column vector with zeros
for i = 1:k; % Start FOR loop to get values
    start_data(i) = input(['Enter a value in ' str_start_unit ': ']);
end % End FOR loop to get values