#!/bin/csh
if ($#argv != 1) then
   echo "Usage is $0 <proto>"
endif
foreach x (*)
    if ((-d $x) && (! -f $x/$argv)) then
	echo $x
	sed -e "s/PROG/$x/g" <$argv >$x/$argv
    endif
end
