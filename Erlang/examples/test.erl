% operators
-module(test).
-compile([export_all]).
% includes
% definitions
% functions
factorial(N) when N > 0 ->
    N * factorial(N-1);
factorial(0) -> 1.

test1(N) ->
    case N of
	-1 ->
	     false;
	1 ->
	    true
		end.

test2(N) ->
    if N < 0 ->
	     false;
       N >0 ->
	    true
		end.
