%% eigenvectors.m
% Returns eigenvectors for a n-by-n matrix
function output = eigenvectors(A)

    lambda = roots(poly(A)); % the eigenvalues
	n = length(A); % size of the matrix
	I = eye(n); % identity matrix
	P = []; % orthogonal matrix

    for i = 1:n;
        B = (A - I*lambda(i)); % [A-I*lamba]
        C = rref(B);
        D = C(1,:);
        P = cat(1,P,D); % append eigenvector to P
    end
    
    output = P;
    