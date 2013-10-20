function [ detJ ] = euclid_to_spherical()
%EUCLID_TO_SPHERICAL 
%   Converts euclidean coordinates to spherical coordinates, returning the
%   determinant of the Jacobian.
syms r l f
x = r*cos(l)*cos(f); y = r*cos(l)*sin(f); z = r*sin(l);
J = jacobian([x; y; z], [r l f]) % D(x,y,z)/D(r,l,f)
detJ = simple(det(J))
end

