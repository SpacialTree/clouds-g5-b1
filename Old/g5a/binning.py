from glob import glob
import matplotlib
import matplotlib.pylab as plt
import numpy as np
import astropy

name = 'bins/bin.mom0.smK.tot.12CO.spw17.txt'
def graph_bin(name,**style):
    '''if '17' in name:
        print('skip: '+name)
        return False'''
    '''if '12CO' in name or 'C18O' in name:
        return False'''
    try:
        fil = open(name,'r')
        cont = fil.readlines()
        clean = [y.split() for y in cont]
        #print(clean)
        data = np.array(clean[6:-2]).astype(float)
        x = data[:,0]
        y = data[:,1]
        mole=''
        div = np.arange(0,x.size,int(x.size/10))
        xbar=x[div]
        ybar=y[div]
        if 'snr' not in style:
            snr = 1
        else:
            snr = style['snr']
        print(name)
        #print(len(style)==2)
        if 'bin2' in name:
            st = 1
        else:
            st = 0
        if 'mom0.smK.tot.12CO' in name:
            y = y / 100.
            ybar = ybar / 100.
            snr = snr / 100.
            mole = name[22+st:-10] + '/100'+'-'+name[-6:-4]
        elif 'mom0.smK.tot.13CO' in name:
            y = y / 10.
            ybar = ybar / 10.
            snr = snr / 10.
            mole = name[22+st:-10] + '/10'+'-'+name[-6:-4]
        elif 'mom0' in name:
            mole = name[22+st:-10]+'-'+name[-6:-4]
        elif 'mom' in name:
            mole = name[9+st:13+st]+'-'+name[-6:-4]
        elif 'ratio' in name:
            mole=name[19+st:-4]
            if 'SiO-H2' in name:
                y = y*100.
                mole = mole+'*100'
        elif 'temp' in name:
            mole = name[20+st:-4]
            if 'L' in mole:
                mole = '150km/s Cloud'
            elif 'R' in mole:
                mole = '50km/s Cloud'
        elif 'ratio.tot.1' in name:
            mole=name
        if 'color' in style and 'line' in style:
            plt.plot(x,y,color=style['color'],linestyle=style['line'],label=mole)
            if 'snr' in style:
                plt.errorbar(xbar,ybar,yerr=5*ybar/snr,fmt=',',color=style['color'])
        elif 'color' in style:
            #print(style[0],style[1])
            plt.plot(x,y,color=style['color'],label=mole)
            if 'snr' in style:
                plt.errorbar(xbar,ybar,yerr=1./snr,fmt=',',color=style['color'])
        elif 'line' in style:
            plt.plot(x,y,linestyle=style['line'],label=mole)
            #plt.errorbar(xbar,ybar,yerr=snr,fmt=',')
        else:
            plt.plot(x,y,label=mole)
            #print('err: plotting')
        fil.close()
        #div = np.arange(0,x.size,int(x.size/5))
        #xbar=x[div]
        #ybar=y[div]
        #plt.errorbar(xbar,ybar,yerr=snr,fmt=',')
    except:
        print('err: ' + name)
    return True

#plt.xlabel('Distance (pixels)')
'''#plt.axvspan(xmin=75,xmax=165,color='gray',alpha=0.5,label='Interface')

# Moment 0
plt.figure(1)
plt.axvspan(xmin=75,xmax=165,color='gray',alpha=0.5,label='Interface')
plt.xlabel('Distance (pixels)')
graph_bin('bins/bin.mom0.smK.tot.13CO.spw29.txt',line='dashed',color='tab:blue')
graph_bin('bins/bin.mom0.smK.tot.12CO.spw17.txt',line='dashed',color='tab:orange')
graph_bin('bins/bin.mom0.smK.tot.SiO.spw27.txt',color='tab:green')
graph_bin('bins/bin.mom0.smK.tot.CH3OH.spw21.txt',color='tab:red')
graph_bin('bins/bin.mom0.smK.tot.H2CO.spw23.txt',color='tab:purple')
graph_bin('bins/bin.mom0.smK.tot.H2CO.spw25.txt',color='tab:cyan')
graph_bin('bins/bin.mom0.smK.tot.OCS.spw23.txt',color='tab:brown')
plt.ylabel('K.km/s')
plt.title('Integrated Intensity')
plt.legend()
#graph_bin(name)'''

'''plt.figure(2)
plt.axvspan(xmin=211,xmax=458,color='gray',alpha=0.5,label='Interface')
plt.xlabel('Distance (arcseconds)')
graph_bin('bins/bin2.mom0.smK.tot.13CO.spw29.txt',line='dashed',color='tab:blue')
graph_bin('bins/bin2.mom0.smK.tot.12CO.spw17.txt',line='dashed',color='tab:orange')
graph_bin('bins/bin2.mom0.smK.tot.C18O.spw31.txt',snr=26.336,color='tab:green')
graph_bin('bins/bin2.mom0.smK.tot.SiO.spw27.txt',snr=93.505,color='tab:red')
graph_bin('bins/bin2.mom0.smK.tot.CH3OH.spw21.txt',snr=108.106,color='tab:purple')
graph_bin('bins/bin2.mom0.smK.tot.H2CO.spw23.txt',snr=24.965,color='tab:cyan')
graph_bin('bins/bin2.mom0.smK.tot.H2CO.spw25.txt',color='tab:pink')
graph_bin('bins/bin2.mom0.smK.tot.OCS.spw23.txt',color='brown')
plt.ylabel('K.km/s')
plt.title('Integrated Intensity')
plt.legend()'''

#plt.xlabel('Distance (pixels)')
# Chemsitry Ratios
plt.figure(3)
plt.axvspan(xmin=75,xmax=165,color='gray',alpha=0.5,label='Interface')
graph_bin('bins/bin.ratio.tot.H2COa-13CO.txt',color='tab:green')
graph_bin('bins/bin.ratio.tot.CH3OH-13CO.txt',color='tab:blue')
graph_bin('bins/bin.ratio.tot.OCS-13CO.txt',color='tab:orange')
graph_bin('bins/bin.ratio.tot.H2COb-13CO.txt',color='tab:red')
graph_bin('bins/bin.ratio.tot.SiO-13CO.txt',color='tab:purple')
plt.ylabel('')
plt.xlabel('Distance (pixels)')
plt.title('Chemistry Ratios')
plt.ylim(0,0.12)
plt.legend()

'''# Gas dynamics
##graph_bin('')
# mom1
plt.figure(4)
plt.axvspan(xmin=75,xmax=165,color='gray',alpha=0.5,label='Interface')
plt.ylabel('km/s')
plt.xlabel('Distance (pixels)')
plt.title('VelocityGas Kinematics')
graph_bin('bins/bin.mom1.tot.12CO.spw17.txt')
#graph_bin('bins/bin.mom1.L.12CO.spw17.txt')
#graph_bin('bins/bin.mom1.R.12CO.spw17.txt')
#mom2
#plt.ylabel('km/s')
#plt.title('Velocity Dispersion')
graph_bin('bins/bin.mom2.tot.12CO.spw17.txt')
#graph_bin('bins/bin.mom2.L.12CO.spw17.txt')
#graph_bin('bins/bin.mom2.R.12CO.spw17.txt')
plt.legend()'''

'''plt.figure(5)
plt.axvspan(xmin=211,xmax=458,color='gray',alpha=0.5,label='Interface')
plt.xlabel('Distance (arcseconds)')
plt.ylabel('km/s')
plt.title('Gas Kinematics')
graph_bin('bins/bin2.mom1.tot.12CO.spw17.txt')
graph_bin('bins/bin2.mom2.tot.12CO.spw17.txt')
plt.legend()'''

# temperature
plt.figure(6)
plt.axvspan(xmin=75,xmax=165,color='gray',alpha=0.5,label='Interface')
plt.ylabel('Kelvin')
plt.xlabel('Distance (pixels)')
plt.title('Kinetic Temperature')
#graph_bin('bins/bin.smoothtemp.tot.txt')
graph_bin('bins/bin.smoothtemp.L.txt',color='tab:blue')
graph_bin('bins/bin.smoothtemp.R.txt',color='tab:green')
plt.legend()

# isotopologue ratios
plt.figure(7)
plt.axvspan(xmin=75,xmax=165,color='gray',alpha=0.5,label='Interface')
plt.title('Isotopologue Line Ratios')
plt.xlabel('Distance (pixels)')
graph_bin('bins/bin.ratio.tot.12CO-13CO.txt',color='tab:blue')    
#graph_bin('bins/bin.ratio.tot.12CO-C18O.txt')    
graph_bin('bins/bin.ratio.tot.13CO-C18O.txt',color='tab:green')    
plt.legend()

# shock tracers
plt.figure(8)
plt.xlabel('Distance (pixels)')
plt.axvspan(xmin=75,xmax=165,color='gray',alpha=0.5,label='Interface')
plt.title('Shock Tracer Abundance Ratios')
graph_bin('bins/bin.tot.ratio.CH3OH-H2.txt',color='tab:blue')
graph_bin('bins/bin.tot.ratio.SiO-H2.txt',color='tab:green',line='dashed')
plt.ylim(0,6.5e-9)
plt.legend()


plt.show()

#immoments(imagename='spw17_12CO/g5a.12CO.spw17.im',chans='640~946',moments=[0],outfile='spw17_12CO/vbridge.mom0.12CO.spw17.im',includepix=[1.0,700.0])
#immoments(imagename='spw17_12CO/g5a.12CO.spw17.im',chans='640~946',moments=[1],outfile='spw17_12CO/vbridge.mom1.12CO.spw17.im',includepix=[1.0,700.0])
#immoments(imagename='spw17_12CO/g5a.12CO.spw17.im',chans='640~946',moments=[2],outfile='spw17_12CO/vbridge.mom2.12CO.spw17.im',includepix=[1.0,700.0])



#imrebin(imagename='spw21_CH3OH/g5a.mom0.smK.tot.CH3OH.spw21.im',outfile='bins/try.CH3OH.mom0.im',factor=[1,73,1,1])
#imrebin(imagename='',outfile='bins/',factor=[1,#,1,1])
#imrebin(imagename='spw27_SiO/g5a.mom1.tot.SiO.spw27.im',outfile='bins/bin.mom1.tot.SiO.spw27.im',factor=[1,60,1,1])
#imrebin(imagename='spw29_13CO/g5a.mom2.tot.13CO.spw29.im/',outfile='bins/bin.mom2.tot.13CO.spw29.im/',factor=[1,60,1,1])
#imrebin(imagename='',outfile='bins/',factor=[1,64,1,1])
#imrebin(imagename='spw17_12CO/g5a.mom1.L.12CO.spw17.im',outfile='bins/bin.mom1.L.12CO.spw17.im',factor=[1,64,1,1])
#imrebin(imagename='spw17_12CO/g5a.mom1.R.12CO.spw17.im',outfile='bins/bin.mom1.R.12CO.spw17.im',factor=[1,64,1,1])
#imrebin(imagename='spw17_12CO/g5a.mom1.tot.12CO.spw17.im',outfile='bins/bin.mom1.tot.12CO.spw17.im',factor=[1,64,1,1])
#imrebin(imagename='spw17_12CO/g5a.mom2.L.12CO.spw17.im',outfile='bins/bin.mom2.L.12CO.spw17.im',factor=[1,64,1,1])
#imrebin(imagename='spw17_12CO/g5a.mom2.R.12CO.spw17.im',outfile='bins/bin.mom2.R.12CO.spw17.im',factor=[1,64,1,1])
#imrebin(imagename='spw17_12CO/g5a.mom2.tot.12CO.spw17.im',outfile='bins/bin.mom2.tot.12CO.spw17.im',factor=[1,64,1,1])
#imrebin(imagename='shock/g5a.tot.CH3OHcoldense.im',outfile='bins/bin.tot.CH3OHcoldense.im',factor=[1,60,1,1])
#imrebin(imagename='shock/g5a.tot.SiOcoldense.im',outfile='bins/bin.tot.SiOcoldense.im',factor=[1,60,1,1])
#imrebin(imagename='shock/g5a.tot.ratio.CH3OH-H2.im',outfile='bins/bin.tot.ratio.CH3OH-H2.im',factor=[1,64,1,1])
#imrebin(imagename='shock/g5a.tot.ratio.SiO-H2.im',outfile='bins/bin.tot.ratio.SiO-H2.im',factor=[1,64,1,1])

'''
immath(imagename='spw17_12CO/g5a.12CO.spw17.im', mode='evalexpr', expr='1.222e6*IM0/230.538000^2/40^2', outfile='spw17_12CO/g5a.K.12CO.spw17.im')
imhead(imagename='spw17_12CO/g5a.K.12CO.spw17.im', mode='put', hdkey='bunit', hdvalue='K')

immath(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im', mode='evalexpr', expr='1.222e6*IM0/218.44005^2/40^2', outfile='spw21_CH3OH/g5a.K.CH3OH.spw21.im')
imhead(imagename='spw21_CH3OH/g5a.K.CH3OH.spw21.im', mode='put', hdkey='bunit', hdvalue='K')

immath(imagename='spw23_H2CO/g5a.H2CO.spw23.im', mode='evalexpr', expr='1.222e6*IM0/218.760066^2/40^2', outfile='spw23_H2CO/g5a.K.H2CO.spw23.im')
imhead(imagename='spw23_H2CO/g5a.K.H2CO.spw23.im', mode='put', hdkey='bunit', hdvalue='K')

immath(imagename='spw23_OCS/g5a.OCS.spw23.im', mode='evalexpr', expr='1.222e6*IM0/218.903355^2/40^2', outfile='spw23_OCS/g5a.K.OCS.spw23.im')
imhead(imagename='spw23_OCS/g5a.K.OCS.spw23.im', mode='put', hdkey='bunit', hdvalue='K')

immath(imagename='spw25_H2CO/g5a.H2CO.spw25.im', mode='evalexpr', expr='1.222e6*IM0/218.222192^2/40^2', outfile='spw25_H2CO/g5a.K.H2CO.spw25.im')
imhead(imagename='spw25_H2CO/g5a.K.H2CO.spw25.im', mode='put', hdkey='bunit', hdvalue='K')

immath(imagename='spw27_SiO/g5a.SiO.spw27.im', mode='evalexpr', expr='1.222e6*IM0/217.104980^2/40^2', outfile='spw27_SiO/g5a.K.SiO.spw27.im')
imhead(imagename='spw27_SiO/g5a.K.SiO.spw27.im', mode='put', hdkey='bunit', hdvalue='K')

immath(imagename='spw29_13CO/g5a.13CO.spw29.im', mode='evalexpr', expr='1.222e6*IM0/220.398684^2/40^2', outfile='spw29_13CO/g5a.K.13CO.spw29.im')
imhead(imagename='spw29_13CO/g5a.K.13CO.spw29.im', mode='put', hdkey='bunit', hdvalue='K')

immath(imagename='spw31_C18O/g5a.C18O.spw31.im', mode='evalexpr', expr='1.222e6*IM0/219.560358^2/40^2', outfile='spw31_C18O/g5a.K.C18O.spw31.im')
imhead(imagename='spw31_C18O/g5a.K.C18O.spw31.im', mode='put', hdkey='bunit', hdvalue='K')
'''
