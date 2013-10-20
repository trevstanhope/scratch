% GENERATION_ZERO.M
% Group 10: Nada Khan, Rodger Liu, Trevor Stanhope, Mei Xiao

function X = generation_zero(universe, alive)

% Generate random matrix
Matrix = rand(universe);
   
% Take the (alive) smallest numbers and make them all into (1) in the
% matrix. This will assure it is random.
S = sort(Matrix(:));
A = S(alive);

% If elements in A are less than or equal to live, set values in Matrix = to 1
% If elements in A are greater than or equal to 1, set values in M = to 0
Matrix((Matrix<=A)) = 1;
Matrix((Matrix~=1)) = 0;

% Generate 3D Matrix, Generation_0
A = zeros(universe)
B = zeros(universe)
X(:,:,1) = scarse(A)
X(:,:,2) = scarse(B)
X(:,:,3) = scarse(Matrix);
end