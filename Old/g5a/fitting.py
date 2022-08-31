#import lmfit
from lmfit import minimize, Parameters
import scipy
from scipy.optimize import leastsq
import numpy as np
import astropy
from astropy.io import fits
import matplotlib.pylab as plt
from glob import glob

def sinusoidal_fit(a,t,k,phi):
    # t - time
    # k - wavelength
    # phi - phase
    return a*np.sin(k*t+phi)

def residual(params, x, data, eps_data):
#def residual(params, x, data):
    amp = params['amp']
    phaseshift = params['phase']
    freq = params['frequency']

    #f = np.sum(x*freq,phaseshift)
    model = amp * np.sin(np.sum([x*freq,phaseshift]))

    return (data-model) / eps_data
    #return (data-model)

def plotting():
    x = np.linspace(-np.pi, np.pi, 201)
    plt.plot(x, np.sin(x))
    plt.xlabel('Angle [rad]')
    plt.ylabel('sin(x)')
    plt.axis('tight')
    plt.show()

def plot_all():
    spectra = glob(LOCATION + 'spec*')
    for loc in spectra:
        spec = fits.open(loc)
        data = spec[0].data
        plt.plot(data, label=loc[-6:-5])
        spec.close()

def get_data(pos, ran):
    try:
        loc = LOCATION + 'spec' + str(pos)+'.fits'
        spec = fits.open(loc)
        data = spec[0].data
        for blan in ran:
            minx = blan[0]
            maxx = blan[1]
            if minx < data.size and maxx < data.size and minx >= 0 and maxx >= 0:
                data = chop(data,minx,maxx)
        #plt.plot(data)
        spec.close()
        return data
    except:
        print('err')

def chop(data, minx, maxx):
    while minx < maxx:
        data[minx] = float('NaN')
        #data[minx] = 0.0 ### Testing
        minx+=1
    return data

## spw 27 SiO
LOCATION ='/lustre/aoc/students/sgramze/alma/G5/a/TP/2018.1.00862.S/spw27_SiO/spectr27/'
a= 0.05952#0.07248360812040433#0.07248351333194103
#0.03983#0.07005#0.04532#0.04311#0.05276#0.0739#0.13 # amp
k = 0.1145#0.11535228782078386#0.11535263440035073
#0.1164#0.1215#0.1256#0.1208#0.1215#0.1079#0.1107#0.11 # frequency
phi= -1.171#-0.9411985232341893#-0.9412403247560666
#-1.217#-1.573#-1.497#0.1 # phase
sdev=2.235772e-01#2.7349e-01
rms= 2.350724e-01#2.7304e-01
## dataE = chop(data,150,285)
'''
## spw 25 H2CO
LOCATION ='/lustre/aoc/students/sgramze/alma/G5/a/TP/2018.1.00862.S/spw25_H2CO/spectr25/'
a = 0.0308#0.01604#0.13
k = 0.1068#0.1098#0.11
phi = 0.1068#-0.1754#-0.1131#-0.1142#0.0
sdev=2.133e-01
rms= 2.3500e-01
## dataE = chop(data,150,460)

## spw 23 H3CO
LOCATION ='/lustre/aoc/students/sgramze/alma/G5/a/TP/2018.1.00862.S/spw23_H2CO/spectr23/'
a = 0.02602#0.03086#0.0521#0.0229#0.02383#0.02218#0.02357#0.03983
k = 0.1188#0.1179#0.1153#0.1101#0.1059#0.1078#0.1088#0.1164
phi = -2.651#-2.293#-1.521#-2.267#-2.167#-2.156#-2.184#0.0
sdev=1.587211e-01#2.301693
rms= 1.660949e-01#2.29736

## spw 21 CH3OH
LOCATION ='/lustre/aoc/students/sgramze/alma/G5/a/TP/2018.1.00862.S/spw21_CH3OH/spectr21/'
a = 0.04115#0.0308#0.03213#0.01152#0.01939#0.01895#0.01973#0.01525#0.01673#0.01849#0.3
k = 0.1125#0.1068#0.1136#0.09388#0.08397#0.08428#0.08659#0.08878#0.1027#0.08791#0.1
phi = 0.537#0.5373#0.5442#-2.191#2.04#1.896#0.7765#1.047#-1.942#0.1367#0.0
sdev = 1.392469e-01#4.377464
rms = 1.479303e-01#4.635262

## spw 17 12CO
LOCATION ='/lustre/aoc/students/sgramze/alma/G5/a/TP/2018.1.00862.S/spw17_12CO/spectr17/'
# no obv ripple

## spw 29 13CO
LOCATION ='/lustre/aoc/students/sgramze/alma/G5/a/TP/2018.1.00862.S/spw29_13CO/spectr29/'
# Main problem seems to be a sunken baseline, no obv ripple

## spw 31 C18O
LOCATION ='/lustre/aoc/students/sgramze/alma/G5/a/TP/2018.1.00862.S/spw31_C18O/spectr31/'
a =  0.04083#0.03386#0.0442#0.04008#0.02198#0.01637#0.03514#0.03
k = 0.05185#0.05206#0.0519#0.05183#0.05583#0.04#0.017505#0.0125#0.1
phi = -2.69#-2.748#-2.902#-2.924#-0.7813#-1.318#-0.3013#-1.486#0.0
sdev = 3.145244e-01
rms = 3.145766e-01
'''

eps_data = sdev/rms

params = Parameters()
params.add('amp',value=a,min=0)
params.add('frequency',value=k,min=0,max=np.pi)
params.add('phase',value=phi,min=-np.pi,max=np.pi)

spectra = np.array(glob(LOCATION+'spec*')).size
print(str(spectra) +' Spectra available')
#print(spectra)

data = np.zeros(512)

i = 1
#count = 0.0
#print(spectra+1)
while i < spectra+1:
    print(i)
    dataB = get_data(i,[(300,450),(145,290)])    #spw 27
    #dataB = get_data(i,[(150,280),(300,460)])    #spw 25
    #dataB = get_data(i,[(300,565),(620,910)])    #spw 31
    b = np.linspace(1,dataB.size,dataB.size)
    outB = minimize(residual, params, args=(b, dataB, eps_data),nan_policy='omit')
    outB.params.pretty_print()
    
    #count += 1.0
    i+=1
#print(count)

focus = 5

count=1.0
data = get_data(focus,[(300,450),(145,290)])    #spw 27
#data = get_data(focus,[(150,280),(300,460)])    #spw 25
#data = get_data(focus,[(18,140),(170,280),(325,470)])    #spw 23
#data = get_data(focus,[(0,255),(365,480)])    #spw 21
data = get_data(focus,[(300,565),(620,910)])    #spw 31
#data = get_data(focus,[(300,750)])#(375,485),(50,150)])
#[(160,280)])#[(70,280),(320,460)])#[(150,260),(290,460)])#[(150,280),(320,460)])
t = np.linspace(1,data.size,data.size)
#data = data / count
dataE = data#[]

ch = np.linspace(1,dataE.size,dataE.size)
out = minimize(residual, params, args=(ch, dataE, eps_data),nan_policy='omit')
out.params.pretty_print()

#out = minimize(residual, params, args=(t, data, eps_data))
#out = minimize(residual, params, args=(t, data))
#print(residual(params, t, data, eps_data))
#print(params['frequency'])
change = out.params.valuesdict()
amp = change['amp']#out.params['amp']
phaseshift = change['phase']
freq = change['frequency']
print('Amplitude:',amp,'\nFrequency:',freq,'\nPhase:',phaseshift)

sinFit = sinusoidal_fit(amp,t,freq,phaseshift)
sinGuess = sinusoidal_fit(a,t,k,phi)

data1=get_data(1,[(160,280),(320,440)])
data2=get_data(2,[(320,430)])
data3=get_data(3,[(160,280),(370,430)])
data4=get_data(4,[(150,270),(370,440)])

qPlot = True

if qPlot:
    #plot_all()
    info=get_data(focus,[(-1,-1)])
    re = np.add(info,np.negative(sinFit))
    ro = np.add(info,np.negative(sinGuess))
    plt.plot(info,label='Raw Data')
    #plt.plot(data,label='Useable')
    plt.plot(re+0.5, label='Raw-Fit')
    #plt.plot(ro+0.5, label='Raw-Guess')
    #plt.plot(info,label='Raw Data')
    plt.plot(sinFit,color='darkred',label='Best Fit')
    #plt.plot(sinGuess,label='Guess')

    #plt.plot(data, label='Avg Data')

    #plt.plot(data1,color='grey')
    #plt.plot(data2,color='silver')
    #plt.plot(data3,color='slategrey')
    #plt.plot(data4,color='lightgrey')
    plt.xlabel('channel')
    plt.ylabel('Jy/beam')
    plt.title(LOCATION[-20:-10])
    plt.legend()
    plt.show()


