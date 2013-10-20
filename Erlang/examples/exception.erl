% exception.erl
% operators
-module(exception).
-compile([export_all]).
% functions
return(X) when is_integer(X) ->
    catch return_error(X).
return_error(X) when X < 0 ->
    throw({'EXIT', {badarith, [{exception,return,error,1},
			       {erl_eval,do,apply,5},
			       {shell,exprs,6},
			       {shell,eval_,exprs,6},
			       {shell,eval_loop,3}]}});
return_error(X) when X == 0 ->
    1/X;
return_error(X) when X > 0 ->
    {'EXIT', {badarith, [{exception,return,error,1},
			       {erl_eval,do,apply,5},
			       {shell,exprs,6},
			       {shell,eval_,exprs,6},
			       {shell,eval_loop,3}]}}.
try_return(X) when is_integer(X) ->
    try return_error(X) of
	Val ->
	    {normal, Val}
		catch
		    exit:Reason ->
			{exit, Reason};
		    throw:Throw  ->
			{throw, Throw};
		    error:Error ->
			{error, Error}
			    end.
