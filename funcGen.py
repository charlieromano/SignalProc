import numpy as np
import scipy.signal as sc
import matplotlib.pyplot as plt
from numpy import pi as pi


def sigSin(f,T):
    """ Usage example plt.plot(sigSin(1e3,10));plt.show() """
    x = np.arange(0,T,1/f)
    y = np.sin(2*pi*x)
    return y


def sigTrian(f,T):
    """ Usage example plt.plot(sigTrian(2e3,15));plt.show() """    
    x = np.arange(0,T,1/f)
    y = sc.sawtooth(2*pi*x)
    return y


def sigSquare(f,T):
    """ Usage example plt.plot(sigSquare(1e3,20));plt.show() """
    x = np.arange(0,T,1/f)
    y = sc.square(2*pi*x,0.5)
    return y


