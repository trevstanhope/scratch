-module(count).
-export([count/1]).

count(String) ->
    lists:foldl(fun (Element, Acc) ->
			case Element of
			    $a ->
				Acc + 1;
			    _ ->
				Acc
				    end
			    end,
		0,
		String).
				
