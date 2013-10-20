-module(mapping).
-export([extract/1]).

extract(List) ->
    lists:map(fun extractfromtuple/1, List).

extractfromtuple({_, Second, _}) ->
    Second.
