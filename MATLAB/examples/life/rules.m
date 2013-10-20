% RULES.M
% Group 10: Nada Khan, Rodger Liu, Trevor Stanhope, Mei Xiao
% Conways Game of Life Simulator

function [generation_nplus1] = life_rules(universe, generation_n)

% whether cells stay alive, die, or generate new cells depends
% upon how many of their eight possible neighbors are alive.
% Here we generate index vectors for four of the eight neighbors.
% We use periodic (torus) boundary conditions at the edges of the
% universe. This will be used when finding which neighbours are on and
% which are off.
n = [m 1:m-1];
e = [2:m 1];
s = [2:m 1];
w = [m 1:m-1];

% get the current generation
Y = cdr(generation_n);

% how many of eight neighbors are alive.
N = Y(n,:) + Y(s,:) + Y(:,e) + Y(:,w) + Y(n,e) + Y(n,w) + Y(s,e) + Y(s,w);
      
% create newest generation
Z = Y & (N == 2) | (N == 3);
        
% concatate Z as the last page of generation_n
generation_nplus1 = cat(3, generation_n, Z);

end
