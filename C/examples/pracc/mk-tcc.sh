#!/bin/csh
echo "echo Start>tcc.log" >mk-tcc.bat
foreach x (*)
  if (-d $x) then
     echo "echo -------------- $x ----------------- >>tcc.log" >>mk-tcc.bat
     echo "cd $x" >>mk-tcc.bat
     echo "make  -f makefile.tcc clean >>..\tcc.log" >>mk-tcc.bat
     echo "make  -f makefile.tcc  >>..\tcc.log" >>mk-tcc.bat
     echo "cd .." >>mk-tcc.bat
  endif
end
