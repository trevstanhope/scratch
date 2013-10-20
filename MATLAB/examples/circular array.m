% Clean
clc, clear

% Values
ETO = ones(1,12);
K_init = 1.75;
K_mid = 1.5;
K_end = 1.25;
T_init = 1;
T_mid = 2;
T_end = 3;
month = 10;

% Build circular array
for i = 0:11
    if month+i > 12;  
        circular(i+1) = abs(month+i)-12 ;
    else
        circular(i+1) = month+i;
    end
end        

% Find IWR Init
IWR = zeros(1,12);
j = 0;
for i = circular
    j = j + 1;
    if (j >= 1) && (j <= T_init)
        IWR(i) = K_init*ETO(i);
    elseif (j >= T_init) && (j < T_init + T_mid)
        IWR(i) = K_mid*ETO(i);
    elseif (j >= T_init + T_mid) && (j < T_init + T_mid + T_end)
        IWR(i) = K_end*ETO(i);
    else
        IWR(i) = 0;
    end
end
disp(IWR);