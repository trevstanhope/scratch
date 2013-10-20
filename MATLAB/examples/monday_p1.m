%% Animal Poop
% by Trevor Stanhope
% Problem: Given amount of poop and amount of nutrients per animal per unit
% time, find totals per year.

% Clean Environment
clc, clear, close;

% Initialize Variables
mass = [4500 560 439 6.5]; % mass of poop (kg)
N = [25 4.7 0.053 0.062]; % nitrogen in poop  (kg)
P = [3.3 0.76 0.016 0.022]; % phosphorous in poop (kg)
lifetime = [153 120 48 39]; % lifetime array of animals (days)

% Menu
animal = menu('What kind of animals do you keep? ',...
    'cows',...
    'pigs', ...
    'chickens',...
    'ducks');

switch animal % Set name of animal
    case 1; name = 'cows';
    case 2; name = 'pigs';
    case 3; name = 'chickens';
    case 4; name = 'ducks';
end

number = input('How many animals do you keep at one time? ');

% Change the amounts per animal per lifetime to the amount per animal per year.
mass_y = 365.*mass./lifetime;
N_y = 365.*N./lifetime;
P_y = 365.*P./lifetime;

% Find the amounts produced on the farm per year
mass_farm_y = mass_y(animal)*number; % Mass of manure per year for whole farm
N_farm_y = N_y(animal)*number; % Mass of nitrogen per year for whole farm
P_farm_y = P_y(animal)*number; % Mass of phosphorous per year for whole farm

% Print Results
fprintf(['The %6.0f %s that you keep on your farm will produce %5.2f kg \n'...
    'of manure per year.\n'], number, name, mass_farm_y);
fprintf('In the manure there will be %5.2f kg of nitrogen, \n', N_farm_y);
fprintf('and there will be %5.2f kg of phosphorous. \n', P_farm_y);