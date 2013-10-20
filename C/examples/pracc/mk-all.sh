#!/bin/csh
foreach x (*)
  if (-d $x) then
     echo "-------------- $x -----------------"
     (cd $x;make -f makefile.gcc clean;make -f makefile.gcc)
  endif
end
