import sys
import numpy as np
from matplotlib import pyplot as plt

"""
  Command line: % python ticker.py <stock file> n
  where:
        'stcok file' is a filename of one month stock price data
        'n' is an integer to specify size of convolution window
"""

def dovwap(c,v):
    '''
    Calculate Value Weighted Average Price for a stock
    :param c: Input closing value of one month stock data
    :param v: Trade volume
    :return: Value Weighted Average Price
    '''

    return np.average(c, weights=v)

def convolveClosing(c):
    '''
    Convolve closing cost and plot against closing
    :param c: Input closing value of one month stock data
    :return: Nothing, just plot generated for stock file
    '''
    weights = np.ones(winSize) / winSize

    sma = np.convolve(weights, c) [winSize - 1: -winSize + 1]
    t = np.arange(winSize - 1, len(c))

    plt.plot(t, c[winSize - 1:], lw = 1.0)
    plt.plot(t, sma, lw = 2.0)
    plt.show()

if __name__ == '__main__':

    """
    Note there are no fault tolerant checks in this code
    """
    fn = sys.argv[1]
    winSize = int(sys.argv[2])

    # 'c' = stock closing value
    # 'v' = volume trading
    c,v = np.loadtxt(fn, delimiter=',', usecols=(5,6), unpack=True)

    vwap = dovwap(c,v)
    print 'Volume weighted Average Price: ', vwap

    convolveClosing(c)