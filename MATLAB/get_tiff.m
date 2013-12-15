%% Retrieve a geotiff file
function [NORM ARRAY XY FILENAME] = get_tiff()
    FILENAME = uigetfile('.tif');
    TIF = Tiff(FILENAME);
    XY = TIF.read();
    ARRAY = reshape(XY, 1, []);
    NORM = (ARRAY - min(ARRAY)) / (max(ARRAY) - min(ARRAY));
end
