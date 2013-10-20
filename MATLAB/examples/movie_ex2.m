%MOVIE_EX2.M Sample of movie making from Moore.
%This one does a surface by redrawing parts of a figure.
%Grant Clark
%BREE 252
%2011

%% Housekeeping
clear, clc, clf     %clear workspace, command window, figure

%% Set-up
x=0:pi/100:4*pi;    %define x vector
y=x;                %set intial y vector
[X Y]=meshgrid(x,y);%generate mesh of coordinates (remember meshgrid?)
z=3*sin(X)+cos(Y);  %calculate 'height' values for each point

%% Create figure, set properties
h=surf(z);          %generate figure and capture handle
axis tight;         %set axis property to tight spacing

set(gca, 'nextplot', 'replacechildren') %replace the 'child objects' on axes, but not axes
shading interp
colormap(jet)

%% Loop
for k=0:pi/100:2*pi;            %start loop
    z=(sin(X)+cos(Y)).*sin(k);  %find new z data
    set(h,'ZData',z);           %Set z-data property of surface
    drawnow                     %don't wait to redraw - do it now!
end
disp('All done!')
