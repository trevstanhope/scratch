#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

p_array.exe: p_array.c
	$(CC) $(CFLAGS) -ep_array.exe p_array.c

clean:
	del p_array.exe 
