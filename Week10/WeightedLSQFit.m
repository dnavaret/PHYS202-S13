

function [m, b, dx, slerr, interr] = WeightedLSQFit(x,y,w) 

%varying data and performs a linear least 
%squares regression. Return the resulting slope 
%and intercept pparamenters of the best fit line 
%with their uncertainties.

for i=1:(len(x))
    if w(i) == 1
    m = ((mean(x*y))-(mean(x)*mean(y)))/(mean(x^2) - (mean(x)^2));
    b = (mean(x^2)*mean(y) - (mean(x)*mean(x*y)))/(mean(x^2)- (mean(x)^2)); 
    dx = y - (m*x + b);
    slerr = sqrt((1/(length(x)-2.))*mean(dx^2))/(mean(x^2) - (mean(x)^2));
    interr = sqrt((1/(length(x)-2.))*mean(dx^2)*mean(x^2))/(mean(x^2) - (mean(x)^2));
    else
    slerr = (((w)*(x*y*w)) - ((w*x)*(w*y)))/((w)*(w*(x^2))-((w*x))^2);
       b = (((w*(x^2))*(w*y))-((w*x)*(w*x*y)))/(((w)*(w*(x^2))-((w*x)^2)));
       m = sqrt(((w)/(((w)*(w*(x^2))) - (w*x)^2)));
            interr = sqrt(((w*(x^2)))/(((w)*(w*(x^2))) - ((w*x))^2));
    end
end