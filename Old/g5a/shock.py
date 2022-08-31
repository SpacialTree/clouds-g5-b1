#### TRUE Column Densities of SiO and CH3OH
# N_sio(total) [cm^-2] = (1.54e10)*(T*exp(31.26/T))*I_sio54(K km/s)
# N_ch3oh(total) [cm^-2] = (1.95e11)*(T^1.5 *exp(45.46/T))*I_ch3oh4231(K km/s)
# beamsize 35arcsec

imregrid(imagename='shock/g5a.mom0.smK.L.CH3OH.spw21.im',template='shock/smoothtemp.L.im',interpolation='cubic',output='shock/g5a.mom0.smK.reL.CH3OH.spw21.im',overwrite=True)
imregrid(imagename='shock/g5a.mom0.smK.R.CH3OH.spw21.im',template='shock/smoothtemp.R.im',interpolation='cubic',output='shock/g5a.mom0.smK.reR.CH3OH.spw21.im',overwrite=True)
imregrid(imagename='shock/g5a.mom0.smK.tot.CH3OH.spw21.im',template='shock/smoothtemp.tot.im',interpolation='cubic',output='shock/g5a.mom0.smK.retot.CH3OH.spw21.im',overwrite=True)

immath(imagename=['shock/g5a.mom0.smK.reL.CH3OH.spw21.im','shock/smoothtemp.L.im'], mode='evalexpr',expr='(1.95e11)*(IM1^1.5 *exp(45.46/IM1))*IM0',outfile='shock/g5a.L.CH3OHcoldense.im')
immath(imagename=['shock/g5a.mom0.smK.reR.CH3OH.spw21.im','shock/smoothtemp.R.im'], mode='evalexpr',expr='(1.95e11)*(IM1^1.5 *exp(45.46/IM1))*IM0',outfile='shock/g5a.R.CH3OHcoldense.im')
immath(imagename=['shock/g5a.mom0.smK.retot.CH3OH.spw21.im','shock/smoothtemp.tot.im'], mode='evalexpr',expr='(1.95e11)*(IM1^1.5 *exp(45.46/IM1))*IM0',outfile='shock/g5a.tot.CH3OHcoldense.im')
imhead(imagename='shock/g5a.L.CH3OHcoldense.im', mode='put', hdkey='bunit', hdvalue='cm-2')
imhead(imagename='shock/g5a.R.CH3OHcoldense.im', mode='put', hdkey='bunit', hdvalue='cm-2')
imhead(imagename='shock/g5a.tot.CH3OHcoldense.im', mode='put', hdkey='bunit', hdvalue='cm-2')


imregrid(imagename='shock/g5a.mom0.smK.L.SiO.spw27.im',template='shock/smoothtemp.L.im',interpolation='cubic',output='shock/g5a.mom0.smK.reL.SiO.spw27.im',overwrite=True)
imregrid(imagename='shock/g5a.mom0.smK.R.SiO.spw27.im',template='shock/smoothtemp.R.im',interpolation='cubic',output='shock/g5a.mom0.smK.reR.SiO.spw27.im',overwrite=True)
imregrid(imagename='shock/g5a.mom0.smK.tot.SiO.spw27.im',template='shock/smoothtemp.tot.im',interpolation='cubic',output='shock/g5a.mom0.smK.retot.SiO.spw27.im',overwrite=True)

immath(imagename=['shock/g5a.mom0.smK.reL.SiO.spw27.im','shock/smoothtemp.L.im'], mode='evalexpr',expr='(1.54e10)*(IM1*exp(31.26/IM1))*IM0',outfile='shock/g5a.L.SiOcoldense.im')
immath(imagename=['shock/g5a.mom0.smK.reR.SiO.spw27.im','shock/smoothtemp.R.im'], mode='evalexpr',expr='(1.54e10)*(IM1*exp(31.26/IM1))*IM0',outfile='shock/g5a.R.SiOcoldense.im')
immath(imagename=['shock/g5a.mom0.smK.retot.SiO.spw27.im','shock/smoothtemp.tot.im'], mode='evalexpr',expr='(1.54e10)*(IM1*exp(31.26/IM1))*IM0',outfile='shock/g5a.tot.SiOcoldense.im')
imhead(imagename='shock/g5a.L.SiOcoldense.im', mode='put', hdkey='bunit', hdvalue='cm-2')
imhead(imagename='shock/g5a.R.SiOcoldense.im', mode='put', hdkey='bunit', hdvalue='cm-2')
imhead(imagename='shock/g5a.tot.SiOcoldense.im', mode='put', hdkey='bunit', hdvalue='cm-2')
