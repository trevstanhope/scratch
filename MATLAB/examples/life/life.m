% LIFE.M
% Group 10: Nada Khan, Rodger Liu, Trevor Stanhope, Mei Xiao
% Conways Game of Life Simulator

% house keeping
clc
clear all
   
% prompt user for the matrix size and number of live cells
universe  = input('What is the size of the life universe?: ');
alive = input('How many "live" cells are there at the start of the game?: ');
speed = menu('How fast would you like to run the simulation?: ', 'very slow', 'slow', 'normal', 'fast', 'very fast');

% switch clause for display speed
switch speed
    case 1
      time = 2
    case 2
      time = 1
    case 3
      time = 0.5
    case 4
      time = 0.25
    case 5
      time = 0.1
end

% create the initial sparsed generation with the generation_zero/2 function
generation_n = generation_zero(universe, alive);
   
% initialize checks so it will not interfere with the loop
check_nminus1 = 0
check_nminus2 = 0
 
% begin life simulation while loop
while ((sum(check_nminus1(:)) ~= (m^2)) & (sum(check_nminus2(:)) ~= (m^2)))    

% call rules/1 to return the most recent generation set
generation_nplus1 = rules(generation_n)

% get the lastest 3 generations
Z = cdr(generation_nplus1);
Y = cdr(cdr(generation_nplus1));
X = cdr(cdr(cdr(generation_nplus1)));

% check to see if current generation is same as the last or second to last generations
check_nminus1 = (Z == Y);
check_nminus2 = (Z == X);

% display the current generation and pause for a bit so we can see it. 
imagesc(Z)
pause (time);
end

[i, j, k] = size(generation_n)
fprintf("lasted %d generations", k)
