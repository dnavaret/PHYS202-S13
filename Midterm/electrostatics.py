import numpy as np

def pointPotential(x,y,q,posx,posy):
    """returns the potential at x,y"""
    k=8.9875518*10**9
    q=1*10**-9
    d=1
    Vyx = (k*q)/((x-posx)**2 + (y-posy)**2)**(1./2.)
    return Vyx


def pointField(x,y,q,Xq,Yq):
    """ Takes arguments of (x,y) arrays, the charge, and position (Xq,Yq)
        and returns a tuple of the electric field components"""
    k=8.9875518*10**9
    q=1*10**-9
    Ex=((k*q*(x-Xq))/(((x-Xq)**2+(y-Yq)**2))**0.5)
    return Ex
    Ey=((k*q*(y-Yq))/(((x-Xq)**2+(y-Yq)**2))**0.5)
    return Ey

