%% Import Data
function [CSV FILENAME] = import_csv()
    FILENAME = uigetfile('.csv');
    CSV = csvread(FILENAME);
end

