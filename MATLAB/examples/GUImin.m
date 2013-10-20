function GUImin
% GUImin M-file to create a minimalist GUI from the command line.
% Read more details about a GUI similar to this one, and the programming
% of GUIs generally in the MATLAB documentation: "Creating a Simple GUI
% Programmatically".

% Create figure window
h_figure = figure('Visible', 'off', 'Position', [360,500,450,285]);

% Create GUI elements as child objects in figure window
%Push buttons
h_button1 = uicontrol('Style','pushbutton',...  
    'String','Surf',...
    'Position',[315,220,70,25],...
    'Callback',{@button1_Callback});
h_button2 = uicontrol('Style','pushbutton',...  
    'String','Mesh',...
    'Position',[315,190,70,25],...
    'Callback',{@button2_Callback});

% Popup menu
h_popup = uicontrol('Style','popupmenu',... 
    'String',{'Peaks','Membrane'},...
    'Position',[300,50,100,25],...
    'Callback',(@popup_Callback));

h_axes = axes('Units','Pixels','Position',[50,60,200,185]); % Axes

% Line everything up to look nice
align([h_button1, h_button2, h_popup],'Center','None')

% Change units to normalized so components resize automatically.
set([h_figure,h_button1,h_button2,h_popup,h_axes],'Units','normalized');

% Generate the data to plot.
peaks_data = peaks(35);
membrane_data = membrane;

% Create a plot in the axes.
current_data = peaks_data;
surf(current_data);

set(h_figure,'Name','Simple GUI') % Assign the GUI a name 
movegui(h_figure,'center')% Move the GUI to the center of the screen.

set(h_figure,'Visible','on');% Make the GUI visible.

%  Pop-up menu callback. 
function popup_Callback(source,eventdata) 
   % Determine the selected data set.
   str = get(source, 'String');
   val = get(source,'Value');
   
   % Set current data to the selected data set.
   switch str{val};
   case 'Peaks' % User selects Peaks.
      current_data = peaks_data;
   case 'Membrane' % User selects Membrane.
      current_data = membrane_data;
   end
end

% Push button callbacks. Each callback plots current_data in the
% specified plot type.

function button1_Callback(source,eventdata) 
% Display surf plot of the currently selected data.
     surf(current_data);
end

function button2_Callback(source,eventdata) 
% Display mesh plot of the currently selected data.
     mesh(current_data);
end

end