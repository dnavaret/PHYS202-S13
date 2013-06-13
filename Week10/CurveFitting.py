
import numpy as np
def LinearLeastSquaresFit(x,y):
    import numpy as np
    """Take in arrays representing (x,y) values for a set of linearly 
    varying data and preform a linear least squares regression.  
    Return the resulting slope and intercept parameters of the best 
    fit line with their uncertainties."""
    averageX = np.sum(x)/len(x) #x average
    averageX2 = np.sum(x**2)/len(x**2) #x^2 average
    averageY = np.sum(y)/len(y) #y average
    averageXY = np.sum(x*y)/len(x*y) #x*y average
    slope = (averageXY-(averageX*averageY))/(averageX2-(averageX**2)) #slope formula
    intercept = (averageX2*averageY - (averageX*averageXY))/(averageX2-(averageX**2)) #intercept formula
    deviation = y - (slope*x + intercept) #deviation to get deviation^2
    deviation2 = np.sum(deviation**2)/len(x) #deviation^2 formula
    slerr = np.sqrt((1/(len(x)-2.))*(deviation2/(averageX2 - (averageX**2)))) #slope uncertainty
    interr = np.sqrt((1/(len(x)-2.))*((deviation2*averageX2)/(averageX2 - (averageX**2)))) #intercept uncertainty
    return slope,intercept,slerr,interr



def WeightedLinearLeastSquaresFit(x,y,w):
    """Take in arrays representing (x,y) values for a set of linearly varying data
    and an array of weights w.  Preform a weighted linear least squares regression.
    Return the resulting slope and intercept parameters of the best fit line with
    their uncertainties."""
    wsum = sum(w)
    wx = sum(x*w)
    wx2 = sum(w*(x**2))
    wy = sum(w*y)
    wxy = sum(w*x*y)
    m = (wsum*wxy-wx*wy)/(wsum*wx2 - (wx**2))
    b = (wx2*wy-wx*wxy)/(wsum*wx2 - (wx**2))
    if sum(w)/len(w) == 1:#if this equals 1, should behave like question 2
        averagex = average(x)
        averagey = average(y)
        averagex2 = average(x**2)
        averagexy = average(x*y)
        dev = y - (m*x+b)
        dev1 = average(dev**2)
        slerr = ( (1.0/(len(x)-2)) * (dev1/((averagex2 - averagex**2))) )**(0.5)
        interr = ( (1.0/(len(x)-2)) * ((dev1*averagex2)/((averagex2 - averagex**2))) )**(0.5)
    else:
        slerr = (wsum/((wsum*wx2) - (wx**2)))**0.5 #weighted slope error
        interr = (wx2/(wsum*wx2 - wx**2))**0.5 #weighted intercept error
    return m,b,slerr,interr

