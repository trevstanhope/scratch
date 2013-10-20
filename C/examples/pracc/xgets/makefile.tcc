#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

xgets.obj: xgets.c
	$(CC) $(CFLAGS) -c xgets.c

clean:
	del xgets.obj
