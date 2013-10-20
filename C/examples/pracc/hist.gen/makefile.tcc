#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

all:	data.txt data.out
 
data.out: ..\ia\hist.exe data.txt
	..\ia\hist data.txt >data.out

data.txt: gen.exe
	gen >data.txt

gen.exe: gen.c
	$(CC) $(CFLAGS) -egen.exe gen.c

clean:
	del data.txt 
	del gen.exe 
	del hist.obj 
	del ia.obj
