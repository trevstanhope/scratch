%MOVIE_EX1.M Sample of movie making from Moore.
%This animates a quadratic function.
%Grant Clark
%BREE 252
%2011

%% Housekeeping
clear, clc, clf     %clear workspace, command window, figure

%% Set-up
x=[-10:0.01:10];    %define x values
k=-1;               %set intial k value
y=k*x.^2 - 2;       %calculate first values for y
h=plot(x,y);        %create figure, capture handle for figure
grid on
set(h, 'Erasemode', 'xor')  %this switch causes MATLAB to erase only pixels
                            %that change
axis([-10 10 -10 10])       %sets axis limits

%% Loop
while k<1                   %start loop
    k=k+0.01;               %increment k
    y=k*x.^2 - 2;           %find values of y for x vector and current k
    set(h,'XData', x, 'YData', y);  %reset values in graph with new values
    pause(0.1)
    drawnow                 %don't wait to redraw - do it now!  
end
