%% trevorstanhope_project_1.m
% Trevor Stanhope, ID260399515
% Engineering Mathematics, Project 1
% Calculations and helpful output to explain determinants,
% eigenvalues, eigenvectors, and matrix diagonalization using MATLAB.

% house keeping
clc;
clear all;

%% Problem 1, Overview
disp('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~');
disp('Problem 1, Overview');
% example matrices
A = [8, 11, 2, 8; 0, -7, 2, -1; -3, -7, 2, 1; 1, 1, 2, 4];
B = [1, -2, 0, 5; 0, 7, 1, 5; 0, 4, 4, 0; 0, 0, 0, 2];
disp('For matrix A equal to: ')
disp(A);
disp('And matrix B equal to: ')
disp(B);

% 1a, determinants of A and B
disp('det(A) is:')
disp(det(A));
disp('det(B) is:')
disp(det(B));

% 1b, deteminants of operational combinations of A and B
disp('det(A+B) is:')
disp(det(A+B)); % the determinant is zero
disp('det(A-B) is:')
disp(det(A-B));
disp('det(A*B) is:')
disp(det(A*B));
disp('det(inv(A)) is:')
disp(det(inv(A)));
disp('det(transpose(B)) is:')
disp(det(transpose(B)));

% 1c and 1d, please see the accompanying PDF (trevorstanhope_project_1.pdf)

% 1e, find b
b = roots(poly(B)); % array of eigenvalues
disp('The eigenvalues of B are:');
disp(b);

% 1f, find P and D
[P D] = eig(B);
if rank(P) == length(b) % if there are n-eigenvectors for n-eigenvalues
    D = inv(P)*B*P; % diagonalize A
    disp('The orthogonal matrix of B (denoted P) is: ');
    disp(P);
    disp('The diagonal matrix of B (denoted D) is: ')
    disp(D);
else
    disp('There ARE NOT n linearly independent eigenvectors.');
end

% 1g, Solutions for Ax = lx
x = P(:,2);
disp('The 2nd column of P (denoted x) is an eigenvector of B, and equals:');
disp(x);
disp('Therefore B*x - 8*x = 0');
result = B*x - 8*x;
disp(result);
disp(' This is because x is an eigenvector of B,');
disp('and 8 is the eigenvalue of B corresponding to x.');
disp('Therefore they form a solution of Bx = lx');

%% Problem 2, Basic Analysis
disp('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~');
disp('Problem 2, Basic Analysis');
% example matrices
A = [-9, -3, -16; 13, 7, 16; 3, 3, 10];
B = [0, 0, 2; 1, 0, 1; 0, 1, 1];
disp('For matrix A equal to:');
disp(A)
disp('And matrix B equal to:');
disp(B)

disp('The characteristic equation is of the form:');
disp('C1x^0 + ... + Cnx^n = 0, where C[] is a list of coefficients.');
disp('For matrix A, the characterisitc polynomial coefficients are:')
disp(poly(A));
disp('And the eigenvalues/roots of the characteristic are:')
disp(roots(poly(A)));
disp(' ');
disp('For matrix B, the characterisitc polynomial coefficients are:')
disp(poly(B));
disp('And the eigenvalues/roots of the characteristic are:')
disp(roots(poly(B)));
disp(' ');

% test with eigs()
% for A
disp('To test roots(poly(X)), let us compare it to the m-function eigs(X)');
disp('eigs(A) is:');
disp(eigs(A));
disp('roots(poly(A)) is:');
disp(roots(poly(A)));

% for B
disp('eigs(B) is:');
disp(eigs(B));
disp('roots(poly(B)) is:');
disp(roots(poly(B)));

%% Problem 3, Diagonalization
disp('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~');
disp('Problem 3, Diagonalization Methods');
% example matrix
A = [9, 1, 1; 1, 9, 1; 1, 1, 9];
disp('For matrix A equal to:');
disp(A);

% 3a, diagonalize A
a = roots(poly(A)); % vector of eigenvalues
disp('The eigenvalues of A are:')
disp(a)

% find the orthogonal and diagonal
[P D] = eig(A); 
disp('The orthogonal matrix of A (denoted P) is equal to:');
disp(P);
disp('The diagonal matrix of A (denoted D) is equal to:');
disp(D);

% are there n-unknowns in n-equations?
if rank(P) == length(a)
    D = inv(P)*A*P; % diagonalize A
else
    disp('There ARE NOT n linearly independent eigenvectors.');
end

U = P*D*inv(P); % check reverse
disp('The undiagonalized matrix (denoted U), is equal to: ');
disp(U)
disp('As can be seen, A = U.');
disp('Therefore D = inv(P)*A*P and U = A = P*D*inv(P) are both true.');
disp('Thus, the diagonal matrix D can be undiagonalized back to A.');

% 3b, A to the n-th power
disp('A to the 5th power is equal to:')
disp(A^5)
disp('D to the 5th power and then undiagonalized by P is equal to:')
disp((P*(D^5)*inv(P)));
disp('This demonstrates that A^n is equal to P*D^n*inv(P).');

%% Problem 4, Analyzing the Cayley-Hamilton Theorem
disp('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~');
disp('Problem 4, Cayley-Hamilton Theorem');
% example matrix
A = [5, 7, -5; 0, 4, -1; 2, 8, -3];
disp('For matrix A, equal to:');
disp(A);
% 4a and 4b, please see the accompanying PDF (trevorstanhope_project_1.pdf)
% 4c, the inverse
disp('The inverse of A is equal to: ');
disp(inv(A));
disp('This result is the same as when using the Cayley-Hamilton Method.');


