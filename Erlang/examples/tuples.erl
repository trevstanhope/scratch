% nested tuples
Person = {person,
			{name, joe},
			{height, 1.8},
			{footsize, 10},
			{eyecolor, green}}.
			
% constructing nests			
First = {firstname, joe}.
Last = {lastname, smith}.
Person = {person, First, Last}.

% extracting values
Point = {point, 10, 20}.
{point, X, Y} = Point. % X bound to 10, Y bound to 20

Someone = {person, {name, {first, joe}, {last, smith}, {eyecolor, green}}}.
{_,{_,{_,Who},_,_}} = Someone. % Who bound to joe

