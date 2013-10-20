#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

graph.exe: graph.c
	$(CC) $(CFLAGS) -egraph.exe graph.c

clean:
	del graph.exe 
