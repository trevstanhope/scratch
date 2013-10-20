% VIRTUALFRUIT.M creates a numerical model of a fruit
% Grant Clark
% BREE 252 F2009 Computing for Engineers
% 2009-11-24

%% Tidy up and say Hi'!
clear, clc, close all

% Intro
disp('Welcome to Virtual Fruit!')
disp('We will step you through the creation of your virtual fruit.')
disp('You will virtually never be hungry again!')
fprintf('\n')

%% Load the fruit picture
% Menu to get figure name
% Figure file must be in the MATLAB directory path
k = menu('Choose an image to load:', 'Apples', 'Oranges', 'Gourd', 'Other');
switch k;
    case 1
        figname = 'apples.jpg';
    case 2 
        figname = 'oranges.jpg';
    case 3
        figname = 'gourd.jpg';
    case 4
        fprintf('\n');
        figname = input('Type the name of your figure, including extension: ', 's');
end

% Load the figure data and display figure
fig = imread(figname);
figure(1);
image(fig);
axis image; %Scale the axes so that the figure is not stretched weirdly

%% Trace the outline of the figure and mesh

% Indicate the centerline of the object, which will be the axis of rotation
% when the virtual model is generated. This is especialy important if the 
% object is not exactly straight up and down in the picture.
fprintf('\n');
disp('Pick two points on the figure to demark the centreline of the fruit.');
title('Pick two points to demark the centreline');

% Store the x coordinates in one vector and the y coordinates in another
[endpoint_x endpoint_y] = ginput(2); 
line(endpoint_x, endpoint_y); %Draw the centreline on the picture

% Ask how may points to pick along one edge of the object, to define its
% perimeter line for rotation. The points should be picked in order from
% top to bottom, since they are stored this way in the vector, and will be
% used in the order they are picked when the model is generated.
disp('Please pick some points to delineate ONE ''edge'' of the fruit.');
npoints = input('How many points would you like to pick? ');
fprintf('Please pick the points from top to bottome in order.\n\n');

% Set up the two vectors, one for the X coordinates and the Y coordinates
% The first and last points in each will be the 'end points' picked
% previously
edge_x = [endpoint_x(1);zeros(npoints, 1);endpoint_x(2)];
edge_y = [endpoint_y(1);zeros(npoints, 1);endpoint_y(2)];

% Add two points to the number of points in the vectors (the end points)
npoints = npoints+2; 

% Set up the figure
% Remind user to pick the points in order from top to bottom in order!
title('Pick the points along ONE edge of the fruit, in order from TOP to bottom.');
hold on;

% Pick each point and plot it on the figure after it is picked
% Start at index 2 to leave the starting endpoint in the vector
% Finish at npoints-1 to leave the finishing endpoint in the vector
for k=[2:npoints-1];
     [edge_x(k) edge_y(k)] = ginput(1); % Get the x an y coordinate for the point
     plot(edge_x(k), edge_y(k), 'ob'); % Plot a blue circle at the point
end

% Interpolate X on the fruit's axis for each edge point that was picked
% Note that the 'independent' data here are the Y values at the ends of the
% object's axis. We are finding the X values for each of the Y values of
% the points that were picked. This locates the start of each radius of
% rotation on the axis of the object, so that we can then calculate the
% length of each of those radii, from the axis to the perimeter of the
% object. 
center_x = interp1(endpoint_y, endpoint_x, edge_y); 

% Find radius corresponding to each edge point, from the axis to the edge
radius = edge_x-center_x; 

% Interpolate a new, regular outline based on the edge points selected
% This is important because the CYLINDER function evenly spaces the radii 
% passed as an input vector). We need to use our vector of unevenly spaced
% radii that we picked, and generate a vector of evenly spaced radii.
% Otherwise the model of the object is likely to have an odd shape.

% Find 20 new y-values. We could change this to be more Y values if we
% desire better resolution of the edge (shape) of the object. The
% resolution of the shape that we generate will also depend on how many
% points we picked from the picture.
new_y = linspace(min(edge_y), max(edge_y), 20); 

% We now need to repeat our interpolation step, as above 
new_radius = interp1(edge_y, radius, new_y); 

% Now we generate the coordinates on the model surface. 
% We need to flip the radius vector upside down, depending on the
% order in which the points were picked (top to bottom, or bottom to top)
% and the function used to generate the model surface. The model will
% otherwise be upside-down.
[X,Y,Z]=cylinder(new_radius); % Generate the coordinates
Z=flipud(Z); % Flip the vector

% Scale the height of the fruit size. The CYLINDER fucntion creates an
% object that has a unit height, so we need to scale this to the height of
% the object in our picture, by number of pixels. Otherwise the object will
% be very short and flat!
Z=Z.*(max(edge_y)-min(edge_y));  

% Plot the object in three-space
figure(2);
h_fruit = surf(X,Y,Z);
axis image;
hold on;

%% Colors
% Select corners of a square patch on the picture, that has a nice color in
% it to paint the model with.

fprintf('Select two points at opposite corners of an attractive color patch.\n\n')

figure(1);
title('Select opposite corners of a sample color patch.');
[cols rows]=ginput(2);

% Round the index numbers that were selected
cols=round(cols);
rows=round(rows);

% Get the color values of the patch that was sampled
sample = fig(rows(1):rows(2), cols(1):cols(2), :);
figure(3);
image(sample); % Display the patch that was sampled

% Find the mean color values of the patch that was sampled
red = mean(mean(sample(:, :, 1)));
green = mean(mean(sample(:, :, 2)));
blue = mean(mean(sample(:, :, 3)));

% Set the new color based on the mean color values of the sample patch
newcolor=([red green blue]./256);
figure(2);
colormap(newcolor); % Set the color of the model using the new color

%% Set up light properties, Light object, Lighting, Reflectance

fprintf('\n');

% Set up light properties
set(h_fruit,'FaceLighting','phong','FaceColor','interp','AmbientStrength',0.5)

% Create a light object
h_light = light('Position',[1 0 0],'Style','infinite');
disp('Light source created');
pause(2);
disp('Pick a light position from the menu.');

% Set position of light
w=1;
while w==1
  k=menu('Set position', 'Left of camera', 'Right of camera', 'Headlight', 'None', 'Continue');
  switch k
    case 1
        lighting(gca, 'phong')
        camlight(h_light, 'left')
    case 2
        lighting(gca, 'phong')
        camlight(h_light, 'right')
    case 3
        lighting(gca, 'phong')
        camlight(h_light, 'head')
    case 4
        lighting(gca, 'none')
    case 5 %Exit menu
        w=0;
  end    
end

% Set reflectance
disp('Pick a reflectance style from the menu.');
w=1;
while w==1
  k=menu('Set reflectance', 'Metal', 'Shiny', 'Dull', 'Default', 'Continue');
  switch k
    case 1
        material metal
    case 2
        material shiny
    case 3
        material dull
    case 4
        material default
    case 5 %Exit menu
        w=0;
  end     
end
fprintf('\n');

%% Say goodbye!

title('My virtual fruit!')

fprintf('\n')
disp('Thanks for using Virtual Fruit!')
