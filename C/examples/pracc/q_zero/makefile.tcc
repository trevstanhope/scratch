#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

q_zero.exe: q_zero.c
	$(CC) $(CFLAGS) -eq_zero.exe q_zero.c

clean:
	del q_zero.exe 
