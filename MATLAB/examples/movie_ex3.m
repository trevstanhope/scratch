%MOVIE_EX3.M Sample of movie making from Moore.
%This one does a surface with the movie function.
%Grant Clark
%BREE 252
%2011

%% Housekeeping
clear, clc, close     %clear workspace, command window, figure

%% Set-up
disp('Creating the movie...')

x=0:pi/100:4*pi;    %define x vector
y=x;                %set intial y vector
[X Y]=meshgrid(x,y);%generate mesh of coordinates
z=3*sin(X)+cos(Y);  %calculate 'height' values for each point

%% First plot
h=surf(z);          %generate figure and capture handle
axis tight;         %set axis property to tight spacing
set(gca, 'nextplot', 'replacechildren') %replace the 'child objects' on axes, but not axes
shading interp
colormap(jet)

%% Loop to generate the movie
m=1;
for k=0:pi/50:2*pi;        %start loop
    z=(sin(X)+cos(Y)).*sin(k);
    set(h,'ZData',z);
    M(m)=getframe;          %store the image in a big matrix
    m=m+1;                  %increment m
end
disp('Done creating the movie.')
