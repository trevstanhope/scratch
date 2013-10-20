%SPHERE.M Making a sphere with nifty lighting
%Grant Clark
%BREE 252
%2010

%% Set up workspace
clear, clc, close all    
disp('Generating spherical coordinates...')  %Message

%Create equations
n=20; %resolution
Theta = linspace(-pi, pi, n); %Spherical coordinates
Phi = linspace(-pi, pi, n); %Spherical coordinates
[theta, phi] = meshgrid(Theta, Phi); %create grid

%% Cartesion coordinates
disp('Generating Cartesian coordinates...')  %Message

X=cos(phi).*cos(theta); %Create x coordinates
Y=cos(phi).*sin(theta); %Create y coordinates
Z=sin(phi); %Create z coordinates

%% Create baby sphere

disp('Generating baby sphere...')
surf(X,Y,Z);
axis square
axis([-2,2,-2,2,-2,2])
hold on

%% Create mommy sphere
disp('Generating mommy sphere around the baby sphere...')
surf(2*X, 2*Y, 2*Z)

%% Tranparent
disp('Play with transparency of the objects using the menu.')
alpha(0.5)
w=1;
while w==1;
    k=menu('Choose the level of transparency', '0','0.25','0.5', '0.75', '1.0', 'Continue');
    switch k
    case 1
       alpha(0)
    case 2 
       alpha(0.25)
    case 3 
        alpha(0.5)
    case 4 
        alpha(0.75)
    case 5 
        alpha(1)
    case 6
        w=0;
    end
end


%% Lighting

disp('Play with the lighting on the object using the menu.')

w=1; %flag
m=0; %flag
m=light('Visible', 'off');
while w==1; 
    k = menu('Orientation of the light:', 'Left', 'Right', 'Headlight', 'Off', 'Continue');
        
    switch k
    case 1
      set(m,'Visible','on');
      camlight(m, 'left');
      disp('Camlight left')
      drawnow

    case 2 
      set(m,'Visible','on');
      camlight(m, 'right');
      disp('Camlight right')
      drawnow
    
    case 3
      set(m,'Visible','on');
      camlight(m, 'headlight');
      disp('Camlight headlight')
      drawnow

    case 4
      set(m, 'Visible', 'off')
        
    case 5
      w=0;        
      
    end
end
   

%% Hide lines

disp('Redraw spheres as mesh objects.')
disp('Hide or show lines on back surfaces.')

% Redraw the spheres with MESH instead of SURF
hold off
mesh(X,Y,Z);
axis square
axis([-2,2,-2,2,-2,2])
hold on
mesh(2*X, 2*Y, 2*Z)

% Play with hide command
w=1;
while w==1; 
    k = menu('', 'Hide', 'Show', 'Quit');
        
    switch k
    case 1
    hidden on

    case 2 
    hidden off 
    
    case 3
    w=0;        
    end
end

disp('All done! Thanks for playing!') 