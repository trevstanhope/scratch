%% Print Table
% DESCRIPTION: Prints a table of values
% INPUT:  strings indicating quantity, start units, end units
%                   numeric values of starting data and ending data
% OUTPUT: None
%
function print_table(str_conversion,str_start_unit, str_end_unit,start_data, end_data);
    fprintf('\nConversion of %s.\n', str_conversion);  % Print title
    fprintf('\t%s\t\t\t%s\n', str_start_unit, str_end_unit);   % Print headings
    fprintf('\t%6.2f\t\t%6.2f\n', [start_data'; end_data']); % Print data
    fprintf('\n') % Extra blank line at end of table