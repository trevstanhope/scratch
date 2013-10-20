% MONDAY_P2 Example of solution to Problem 2 on Monday midterm, 2011-01-24
% Temperatures.
% Problem: Generate some artificial temperature values.
% This program calls the function MONDAY_P2_FUN

% CLEAN UP
clc, clear, close;

% Initialize variables
t = linspace(0, 2*pi, 24*60); % Time vector, one value per minute
time = 1:length(t); % Make a vector of number of minutes per day

% Find the signal, stretch, and shift it
temp = sin(t); % Sin of the signal
temp = temp+1; % Shift signal toward positive by one
temp = temp.*10; % Stretch the signal by a factor of 10 (range over 20)
temp = temp-5; % Shift the signal back down by 5 (-5 to 15)

% Call the function to add noise
temp_noisy = monday_p2_fun(temp);

% Plot the result on a graph
plot(time, temp_noisy);
xlabel('Time (min)');
ylabel('Temperature (deg C)');
title('Simulated temperature for one day');
