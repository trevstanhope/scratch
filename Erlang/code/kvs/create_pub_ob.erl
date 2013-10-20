%%% Create Public Object, create_pub_ob.erl
%%% Trevor Stanhope
%% Head
-module(create_pub_ob.erl).
-export([all]).

%% Body
Node = 'riak@127.0.0.1'
{ok, Client} = riak:client_connect(Node)

loop() ->
    receive 
	Pub_ob = riak_object:new(Content)
	Client:put(Pub_ob, 1).


