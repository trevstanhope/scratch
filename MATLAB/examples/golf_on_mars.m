%% Golf on Mars
% Problem: Find trajectory of golf ball on different planetary bodies.
% Trevor Stanhope

% Prepare Environment
clc, clear, close;

% Initilize Variables
angle_deg = 45; % Start angle 45 deg
angle_rad = pi*angle_deg/180; % Change to rads
v0 = 40; % Intitial velocity (m/s)
vx = 40* cos(angle_rad); % Find initial x velocity (m/s)
vy = 40* sin(angle_rad); % Find initial y velocity (m/s)
t = [0:0.1:1000]; % Create time vector
x = zeros(size(t)); y = zeros(size(t)); % Initialize x and y vectors

% Main Menu
choice = menu('Where will you play golf?', ...
    'Earth',...
    'Moon', ...
    'Mercury',...
    'Venus', ...
    'Mars');

switch choice % Determine g for choice
    case 1
        g = 9.81 % acceleration due to gravity (m/s2) Earth
    case 2 
        g = 1.62; % Moon     
    case 3
        g = 3.70; % Mercury
    case 4 
        g = 8.87; % Venus
    case 5 
        g = 3.71; % Mars
end

% Calculations
x = t.*vx; % no acceleration in x direction
y = t.*vy - 0.5.*(t.^2).*g; % acceleration in y direction
yfinal = y(find(y>=0)); % Truncate vectors where y hits the ground
xfinal = x(find(y>=0));

% Plot Results
plot(xfinal,yfinal);
title('Trajectory of Ball')
xlabel('x displacment (m)');
ylabel('y displacment (m)');

% Print Distance
fprintf('The highest distance traveled was %4.2f meters.\n', max(y));
fprintf('The farthest distance traveled was %4.2f meters.', xfinal(end));

