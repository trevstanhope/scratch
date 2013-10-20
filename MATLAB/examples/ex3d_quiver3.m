%EX3D_QUIVER3.M Demonstrates volumetric plotting quiver3 function
%Grant Clark
%BREE 252
%2011

%% Set up workspace
clear, clc, close all    

% Plot the surface normals of the function z=x.*exp(-x.^2 - y.^2).

figure                                %Open new figure
[X,Y] = meshgrid(-2:0.25:2,-1:0.2:1); %Meshgrid coordinates 
Z = X.* exp(-X.^2 - Y.^2);            %Generate Z values
[U,V,W] = surfnorm(X,Y,Z);            %Find normals to surface
quiver3(X,Y,Z,U,V,W,0.5);             %Plot normals to XYZ
                                      %Scales the arrows by 1/2  
%% Create the surface             
hold on
surf(X,Y,Z);                

%% Change the colormap, view, and scale axes
colormap hsv                %Set the colors
view(-35,45)                %Set the view angle
axis ([-2 2 -1 1 -.6 .6])   %Scale the axes
title('3-D quiver map of normals to surface.')
xlabel('Arbitrary units')
hold off

disp('All done! Thanks for playing!') 