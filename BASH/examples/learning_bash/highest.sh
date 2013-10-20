#!/bin/sh
# highest filename [how many]
# for highest.list
# sorts $howmany lines of $filename in descending order

filename=$1
filename=${filename:?"missing."}
howmany=$2

sort -nr $filename | head -${howmany:=10}
