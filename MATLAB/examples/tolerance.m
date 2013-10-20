    N=0.0001;
    K=1;
    h=[10 0 0 0 0 0 0 0 0 0 5];
    h_old=[10 0 0 0 0 0 0 0 0 0 5];
    tolerance=1;
    dx=100;

    while tolerance > 1e-6
        for i=2:1:10
            h(i) = sqrt((((-N/K)-((h(i+1)-h(i-1))/(2*dx)).^2 )*(dx.^2 ) -h(i)*h(i-1) -h(i)*h(i+1))/(-2));
            tolerance(i-1) = abs((h(i)-h_old(i))./h(i));
        end
        tolerance=max(tolerance);
        h_old=h;

    end

    x2=linspace(0,1000,11);
    h=h';
    plot(x2,h, 'r o --')
