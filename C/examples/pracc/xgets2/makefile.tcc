#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

xgets2.obj: xgets2.c
	$(CC) $(CFLAGS) -c xgets2.c

clean:
	del xgets2.obj
