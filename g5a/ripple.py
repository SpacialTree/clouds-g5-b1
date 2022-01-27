#from lmfit import minimize, Parameters
import scipy
import numpy as np
import astropy
from astropy.io import fits
import matplotlib.pylab as plt
from glob import glob

LOC = '/lustre/aoc/students/sgramze/alma/G5/a/TP/2018.1.00862.S/fitsImages/'
SPW17 = LOC + 'g5a.12CO.spw17.fits'
SPW19 = LOC + 'g5a.Ha.spw19.fits'
SPW21 = LOC + 'g5a.HC3N.spw21.fits'
SPW23 = LOC + 'g5a.H2CO.spw23.fits'
SPW25 = LOC + 'g5a.H2CO.spw25.fits'
SPW27 = LOC + 'g5a.SiO.spw27.fits'
SPW29 = LOC + 'g5a.13CO.spw29.fits'
SPW31 = LOC + 'g5a.C18O.spw31.fits'

def sinusoidal_fit(a,t,k,phi):
    # t - time
    # k - wavelength
    # phi - phase
    return a*np.sin(k*t+phi)

def getData(location):
	file = fits.open(location)
	data = np.array(file[0].data)
	file.close()
	return data

## SiO
sio = getData(SPW27)
a= 0.03983#0.07005#0.04532#0.04311#0.05276#0.0739#0.13 # amp
k = 0.1164#0.1215#0.1256#0.1208#0.1215#0.1079#0.1107#0.11 # frequency
phi= -1.217#-1.573#-1.497#0.1 # phase
sdev=2.235772e-01#2.7349e-01
rms= 2.350724e-01#2.7304e-01
size = sio[0].shape[0]
#print(sio[0].shape[0])#(1, 512, 256, 186)
#fit = np.ones(sio.shape)
t = np.linspace(1,size,size)

print(sio[0,0])

