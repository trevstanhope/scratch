function [temp_noisy] = monday_p2_fun(temp);
% MONDAY_P2_FUN Function to add noise to the signal from MONDAY_P2

% Generate vector of uniform random noise
noise = rand(size(temp));
noise = noise - 0.5; % Shift noise down to -.5 + 0.5
temp_noisy = temp + noise; % Add noise to the temperature signal
